"""Add native links for URL cells; artifact-tool does not evaluate HYPERLINK."""
import re, sys
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import xml.etree.ElementTree as ET

p = Path(sys.argv[1])
main = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
rels = 'http://schemas.openxmlformats.org/package/2006/relationships'
office_rels = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
ET.register_namespace('', main)
ET.register_namespace('r', office_rels)
with ZipFile(p) as z:
    parts = {name: z.read(name) for name in z.namelist()}
strings = []
if 'xl/sharedStrings.xml' in parts:
    strings = [''.join(si.itertext()) for si in ET.fromstring(parts['xl/sharedStrings.xml'])]
count = 0
for name in list(parts):
    if not re.fullmatch(r'xl/worksheets/sheet\d+\.xml', name):
        continue
    tree = ET.fromstring(parts[name])
    links = ET.Element(f'{{{main}}}hyperlinks')
    relpath = str(Path(name).parent / '_rels' / (Path(name).name + '.rels'))
    reltree = ET.fromstring(parts[relpath]) if relpath in parts else ET.Element(f'{{{rels}}}Relationships')
    used = {r.get('Id') for r in reltree}
    for cell in tree.findall(f'.//{{{main}}}c'):
        value = cell.find(f'{{{main}}}v')
        if cell.get('t') == 's' and value is not None:
            url = strings[int(value.text)]
        elif cell.get('t') == 'inlineStr':
            url = ''.join(cell.find(f'{{{main}}}is').itertext())
        elif cell.get('t') == 'str' and value is not None:
            url = value.text or ''
        else:
            continue
        if not re.fullmatch(r'https?://\S+', url):
            continue
        rid = 'rIdHyperlink' + str(len(links) + 1)
        assert rid not in used
        ET.SubElement(links, f'{{{main}}}hyperlink', {'ref': cell.get('r'), f'{{{office_rels}}}id': rid})
        ET.SubElement(reltree, f'{{{rels}}}Relationship', {'Id': rid, 'Type': office_rels + '/hyperlink', 'Target': url, 'TargetMode': 'External'})
        used.add(rid)
        count += 1
    if len(links):
        after = {'printOptions', 'pageMargins', 'pageSetup', 'headerFooter', 'rowBreaks', 'colBreaks', 'customProperties', 'cellWatches', 'ignoredErrors', 'smartTags', 'drawing', 'legacyDrawing', 'legacyDrawingHF', 'picture', 'oleObjects', 'controls', 'webPublishItems', 'tableParts', 'extLst'}
        insert = next((i for i, node in enumerate(tree) if node.tag.split('}')[-1] in after), len(tree))
        tree.insert(insert, links)
        parts[name] = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
        parts[relpath] = ET.tostring(reltree, encoding='utf-8', xml_declaration=True)
assert count == 103, count
temp = p.with_suffix('.tmp.xlsx')
with ZipFile(temp, 'w', ZIP_DEFLATED) as z:
    for name, data in parts.items():
        z.writestr(name, data)
temp.replace(p)
print(f'Added {count} native hyperlinks; visible cells retain plain URLs')
