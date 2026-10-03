"""Read selected public repository metadata and documents; never execute them."""
import urllib.request, json, concurrent.futures, base64
from pathlib import Path
repos=['speedyapply/JobSpy','Julien-ser/job-search-skill','AkbarDevop/ai-job-agent','DanielPan12/JobHuntBot','galiprandi/job-seeker','SimplifyJobs/Summer2027-Internships']
out=Path('sources/tools'); out.mkdir(parents=True,exist_ok=True)
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research-read-only'}),timeout=30))
def read(repo):
    try:
        meta=get('https://api.github.com/repos/'+repo)
        readme=get('https://api.github.com/repos/'+repo+'/readme')
        text=base64.b64decode(readme['content']).decode(errors='replace')
        tree=get('https://api.github.com/repos/'+repo+'/git/trees/'+meta['default_branch']+'?recursive=1')
        record={k:meta.get(k) for k in ['full_name','html_url','pushed_at','archived','license','default_branch','stargazers_count']}
        record['checked']='2026-09-29'; record['tree']=[x['path'] for x in tree.get('tree',[]) if x['type']=='blob'];record['readme']=text
        (out/(repo.replace('/','_')+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))
        return {**{k:v for k,v in record.items() if k not in ['readme','tree']},'files':record['tree'][:55],'readme':text[:7000]}
    except Exception as e:return {'repo':repo,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(read,repos): print(json.dumps(result,ensure_ascii=False))
