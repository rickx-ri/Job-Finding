"""Fetch explicitly selected public source URLs; no account cookies or crawling."""
import json, hashlib, sys, concurrent.futures
from pathlib import Path
import urllib.request, urllib.error
from html.parser import HTMLParser

class VisibleText(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip = max(0, self.skip-1)
    def handle_data(self, data):
        if not self.skip and data.strip(): self.parts.append(data.strip())

ROOT = Path(__file__).resolve().parents[1] / 'sources' / 'public'
ROOT.mkdir(parents=True, exist_ok=True)

def read(url):
    key = hashlib.sha256(url.encode()).hexdigest()[:12]
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=35)
        raw = r.read().decode('utf-8', errors='replace'); status=r.status; resolved=r.url
    except Exception as e:
        return {'url':url,'error':str(e)}
    parser=VisibleText(); parser.feed(raw); text='\n'.join(parser.parts)
    record = {'url': url, 'resolved_url': resolved, 'http_status':status,
              'checked':'2026-09-29', 'text':text}
    (ROOT / (key + '.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))
    start = 0
    for marker in ['You will:', 'What You', 'The Role', 'Job Description', 'Description', 'Minimum qualifications:', 'Responsibilities']:
        at = text.find(marker)
        if at >= 0:
            start = at; break
    excerpt=text[start:start+8000]
    for end in ['The expected hourly rate','We appreciate your interest','Equal Opportunity','About the Company','Apply for this job']:
        if end in excerpt: excerpt=excerpt.split(end)[0]
    return {'file': key + '.json', 'url':url, 'status':status,'text':excerpt}

urls = json.loads(Path(sys.argv[1]).read_text())
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for url, future in zip(urls, pool.map(read, urls)):
        print(json.dumps(future, ensure_ascii=False))
