"""Validate exported artifacts and render every final PDF for review."""
import json,re,subprocess,hashlib,math,sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from pypdf import PdfReader
import pdfplumber
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1];data=json.loads((ROOT/'sources/research_data.json').read_text())
qa=ROOT/'qa';render=qa/'final_renders';render.mkdir(exist_ok=True)
pdfs=sorted(list((ROOT/'resumes').rglob('*.pdf'))+list((ROOT/'output/pdf').glob('*.pdf')))
records=[]
if '--reuse-pdf-checks' in sys.argv:
 records=json.loads((qa/'artifact_validation.json').read_text())['pdfs']
 assert {r['file'] for r in records}=={str(p.relative_to(ROOT)) for p in pdfs}
 assert all(hashlib.sha256((ROOT/r['file']).read_bytes()).hexdigest()==r['sha256'] for r in records)
for p in ([] if records else pdfs):
 reader=PdfReader(p); texts=[page.extract_text() or '' for page in reader.pages]
 if not all(len(x.strip())>20 for x in texts):raise AssertionError(f'Blank or nonextractable PDF: {p}')
 if re.fullmatch(r'Ziyu_Xu_D[1-5]\.pdf',p.name):assert len(reader.pages)<=2,(p,len(reader.pages))
 bounds=[]
 with pdfplumber.open(p) as doc:
  for n,page in enumerate(doc.pages):
   outside=[c for c in page.chars if c.get('text','').strip() and (c['x0'] < 8 or c['x1'] > page.width-8 or c['top'] < 8 or c['bottom']>page.height-8)]
   if outside:bounds.append({'page':n+1,'chars':len(outside)})
 assert not bounds,(str(p),bounds)
 subprocess.run(['/usr/bin/pdftoppm','-scale-to','1350','-png',str(p),str(render/p.stem)],check=True,capture_output=True)
 records.append({'file':str(p.relative_to(ROOT)),'pages':len(reader.pages),'chars':sum(map(len,texts)),'text_extractable':True,'page_edge_check':True,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 # One contact sheet per artifact, retaining every page at a readable review scale.
 pages=sorted(render.glob(p.stem+'-*.png'),key=lambda x:int(x.stem.rsplit('-',1)[1]))
 w=620; h=900; ncol=min(3,len(pages)); canvas=Image.new('RGB',(w*ncol,h*math.ceil(len(pages)/ncol)),'#e3e8ee');draw=ImageDraw.Draw(canvas)
 for i,page in enumerate(pages):
  im=Image.open(page).convert('RGB');im=ImageOps.contain(im,(w-12,h-32));x=(i%ncol)*w+6;y=(i//ncol)*h+26;canvas.paste(im,(x,y));draw.text((x,y-20),page.name,fill='black')
 canvas.save(qa/(p.stem+'_contact.png'))
z=ZipFile(ROOT/'outputs/recruiting_2027/2027_Internship_Research.xlsx');ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
sheets=[x for x in z.namelist() if re.fullmatch(r'xl/worksheets/sheet\d+\.xml',x)]
tables=[x for x in z.namelist() if re.fullmatch(r'xl/tables/table\d+\.xml',x)]
assert len(sheets)==3 and len(tables)==3
xchecks=[]
for p in sheets:
 tree=ET.fromstring(z.read(p));pane=tree.find('.//m:pane',ns);assert pane is not None and pane.get('ySplit')=='4'
 xchecks.append({'sheet':p,'panes':pane.attrib})
for p in tables:
 tree=ET.fromstring(z.read(p));assert tree.find('m:autoFilter',ns) is not None
 xchecks.append({'table':p,'filter':tree.find('m:autoFilter',ns).attrib})
native_links=0
for p in sheets:
 tree=ET.fromstring(z.read(p));links=tree.findall('.//m:hyperlink',ns)
 if links:
  relpath=str(Path(p).parent/'_rels'/(Path(p).name+'.rels'))
  relations={r.get('Id'):r for r in ET.fromstring(z.read(relpath))}
  for link in links:
   rel=relations[link.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')]
   assert rel.get('TargetMode')=='External' and rel.get('Target','').startswith('https://')
  native_links+=len(links)
 assert 'HYPERLINK is not implemented' not in z.read(p).decode()
assert native_links==len(data['jobs'])+len(data['companies'])
tree=ET.fromstring(z.read('xl/worksheets/sheet1.xml'));cells={c.get('r'):c for c in tree.findall('.//m:c',ns)}
for addr in ['B3','D3']:
 val=cells[addr].find('m:v',ns);assert val is not None
 assert float(val.text)==(len(data['jobs']) if addr=='B3' else sum(j['category'].startswith('A') for j in data['jobs']))
datecells=[]
for addr,cell in cells.items():
 if re.fullmatch(r'(L|AA)\d+',addr) and int(re.search(r'\d+',addr).group())>=5:
  val=cell.find('m:v',ns)
  if val is not None and val.text and cell.get('t') not in ['s','inlineStr']:
   value=float(val.text);assert 45000<value<48000;datecells.append((addr,value))
assert len(datecells)>=len(data['jobs'])
assert len({(j['company'],j['req_id']) for j in data['jobs']})==len(data['jobs'])
assert len({j['source'] for j in data['jobs']})==len(data['jobs'])
assert all(j['resume'] in ['D1','D2','D3','D4','D5'] for j in data['jobs'])
for d in data['directions']:assert (ROOT/d['resume']).exists()
red=json.loads((qa/'redline_coverage.json').read_text());assert len(red)==6 and all(x['exact_original_and_new_reconstruction'] for x in red)
warnings=[]
for p in (ROOT/'resumes').rglob('*.log'):
 warnings.extend([str(p.relative_to(ROOT))+': '+s for s in p.read_text(errors='replace').splitlines() if 'Overfull' in s])
result={'pdfs':records,'xlsx':xchecks,'native_hyperlinks':native_links,'numeric_date_cells':len(datecells),'dates_sortable_numeric':True,'duplicate_job_ids':0,'duplicate_official_urls':0,'resume_mapping_valid':True,'redline_token_reconstruction':True,'latex_overfull':warnings,'native_excel_interaction':'未使用桌面Excel；验证导出XML与artifact-tool渲染/重算'}
(qa/'artifact_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({'pdf_count':len(pdfs),'pages':sum(r['pages'] for r in records),'numeric_dates':len(datecells),'latex_overfull':warnings,'status':'all structural checks passed; rendered pages ready for visual inspection'},ensure_ascii=False))
