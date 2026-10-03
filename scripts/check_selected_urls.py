"""Read-only check of curated URLs, preserving source text and access limits."""
import json,hashlib,urllib.request,concurrent.futures
from html.parser import HTMLParser
from pathlib import Path
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.parts.append(d.strip())
d=json.loads(Path('sources/research_data.json').read_text())
urls=list(dict.fromkeys(x['source'] for x in d['jobs']+d['companies']))
def check(url):
 r={'url':url,'checked':'2026-09-29'}
 try:
  h=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=18)
  s=h.read().decode(errors='replace');p=Text();p.feed(s);t='\n'.join(p.parts)
  r.update(status=h.status,resolved=h.url,characters=len(t),text=t)
 except Exception as e:r.update(error=str(e))
 key=hashlib.sha256(url.encode()).hexdigest()[:12]
 Path('sources/verified').mkdir(exist_ok=True)
 Path('sources/verified',key+'.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
 return {k:v for k,v in r.items() if k!='text'}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(check,urls))
Path('qa/url_checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps({'total':len(results),'http200':sum(r.get('status')==200 for r in results),'limited':[r for r in results if r.get('status')!=200 or r.get('characters',0)<500]},ensure_ascii=False))
