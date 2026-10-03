import json, urllib.request, base64
from pathlib import Path
choices={
'speedyapply/JobSpy':['jobspy/__init__.py','jobspy/model.py'],
'Julien-ser/job-search-skill':['SKILL.md'],
'AkbarDevop/ai-job-agent':[],
'DanielPan12/JobHuntBot':['SKILL.md','dashboard/server.js','references/safety-and-boundaries.md'],
'galiprandi/job-seeker':['.agents/skills/apply/SKILL.md','scripts/db.js'],
'SimplifyJobs/Summer2027-Internships':['CONTRIBUTING.md','list_updater/listings.py']}
for repo,paths in choices.items():
 p=Path('sources/tools')/(repo.replace('/','_')+'.json');d=json.loads(p.read_text())
 print(repo,d['pushed_at'],(d['license'] or {}).get('spdx_id','未标明'),'branch',d['default_branch'])
 if not paths:paths=[x for x in d['tree'] if x.endswith('SKILL.md')][:2]
 if repo.endswith('job-search-skill') and 'SKILL.md' not in d['tree']:paths=[x for x in d['tree'] if x.endswith('SKILL.md')][:1]
 print('SELECTED',paths)
 print('README',d['readme'][:2200])
 d['reviewed_files']={}
 for path in paths:
  try:
   url='https://api.github.com/repos/'+repo+'/contents/'+path
   data=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research-read-only'}),timeout=20))
   body=base64.b64decode(data['content']).decode(errors='replace');d['reviewed_files'][path]=body
   selected=[x for x in body.splitlines() if any(k in x.lower() for k in ['submit','allow','approval','license','proxy','linkedin','dsn','neon','http','dedup','duplicate','degree','deadline','postgres','auto','site_name','job_url'])]
   print('CODE',path,'\n'.join(selected[:35]))
  except Exception as e:print(path,str(e))
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
