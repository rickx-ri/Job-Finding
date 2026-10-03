import fs from 'node:fs/promises';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root=path.resolve(import.meta.dirname,'..');
const data=JSON.parse(await fs.readFile(path.join(root,'sources/research_data.json'),'utf8'));
const output=path.join(root,'outputs/recruiting_2027');
await fs.mkdir(output,{recursive:true});await fs.mkdir(path.join(root,'qa/workbook'),{recursive:true});
const wb=Workbook.create();
const jobs=wb.worksheets.add('岗位清单');
const companies=wb.worksheets.add('公司观察');
const directions=wb.worksheets.add('方向与简历对应');
const cols=[
 ['id','ID',9],['priority','优先级',11],['company','公司',24],['title','职位/团队',58],['direction','方向',9],['category','筛选结论',30],['country','国家',11],['location','地点/办公方式',34],['season','实习季节',35],['duration','时长/日期安排',52],['status','招聘状态',48],['deadline','日期（按右列解释）',19],['deadline_type','日期类型',22],['deadline_note','日期说明',60],['degree','学位要求',38],['phd','PhD要求',26],['graduation','毕业年份要求',40],['return_school','返校要求',44],['summary','职责摘要',66],['required','必需技能/条件',70],['preferred','加分项',56],['fit','简历匹配依据',60],['gap','缺口/待确认',70],['authorization','JD工作授权条件（不推断个人）',70],['kind','职位/项目性质',32],['req_id','官方岗位编号',42],['checked','核验日期',15],['resume','简历版本',13],['verification','核验层级',45],['discovery','发现渠道',46],['source','官方来源链接',100]
];
const alphabet=n=>{let s='';for(n++;n;n=Math.floor((n-1)/26))s=String.fromCharCode(65+(n-1)%26)+s;return s;};
function base(sheet,title,subtitle){sheet.showGridLines=false;sheet.getRange('A1').values=[[title]];sheet.getRange('A1').format.font={name:'Arial',size:16,bold:true,color:'#183047'};sheet.getRange('A2').values=[[subtitle]];sheet.getRange('A2').format.font={name:'Arial',size:10,italic:true,color:'#4B5563'};sheet.getRange('A1:A3').format.rowHeight=23;sheet.tabColor='#243E57';}
function table(sheet,rows,fields,name){
 const last=alphabet(fields.length-1),end=rows.length+4;
 sheet.getRange(`A4:${last}${end}`).values=[fields.map(x=>x[1]),...rows.map(r=>fields.map(([key])=>['checked','deadline'].includes(key)&&r[key]?new Date(r[key]+'T00:00:00Z'):(r[key]??null)))];
 const r=sheet.getRange(`A4:${last}${end}`);r.format.font={name:'Arial',size:11,color:'#1F2937'};r.format.verticalAlignment='top';r.format.wrapText=true;
 const h=sheet.getRange(`A4:${last}4`);h.format.fill='#243E57';h.format.font={name:'Arial',size:11,bold:true,color:'#FFFFFF'};h.format.horizontalAlignment='center';h.format.verticalAlignment='center';h.format.rowHeight=34;
 fields.forEach((f,i)=>sheet.getRange(`${alphabet(i)}4:${alphabet(i)}${end}`).format.columnWidth=f[2]);
 sheet.getRange(`A5:${last}${end}`).format.rowHeight=46;
 const t=sheet.tables.add(`A4:${last}${end}`,true,name);t.showFilterButton=true;t.style='TableStyleLight1';
 sheet.freezePanes.freezeRows(4);sheet.freezePanes.freezeColumns(sheet===jobs?3:1);
 for(let i=0;i<fields.length;i++)if(['checked','deadline'].includes(fields[i][0]))sheet.getRange(`${alphabet(i)}5:${alphabet(i)}${end}`).setNumberFormat('yyyy-mm-dd');
 // Preserve readable URL values; native hyperlink relationships are added after export.
 const sourceIndex=fields.findIndex(x=>x[0]==='source');
 if(sourceIndex>=0)sheet.getRange(`${alphabet(sourceIndex)}5:${alphabet(sourceIndex)}${end}`).format.font={name:'Arial',size:11,color:'#174A76'};
 return {last,end};
}
const ordered=[...data.jobs].sort((a,b)=>a.category.localeCompare(b.category,'en')||a.priority.localeCompare(b.priority,'en')||a.company.localeCompare(b.company,'en')||a.id.localeCompare(b.id));
base(jobs,'2027 暑期实习 · 岗位清单','CMU MSR · Expected 2028 · 约3个月 · 美国优先/中国备选 · 核验 2026-09-29；A仅指学位+季节，不代表全部资格通过');
const jr=table(jobs,ordered,cols,'Jobs2027');
jobs.getRange(`F5:F${jr.end}`).conditionalFormats.add('beginsWith',{text:'B',format:{fill:'#FFF4D5',font:{color:'#7A4A00'}}});
jobs.getRange(`F5:F${jr.end}`).conditionalFormats.add('beginsWith',{text:'C',format:{fill:'#FDE8E7',font:{color:'#943737'}}});
jobs.getRange(`F5:F${jr.end}`).conditionalFormats.add('beginsWith',{text:'T',format:{fill:'#EAF0F7',font:{color:'#425A75'}}});
jobs.getRange('A3').values=[['记录数']];jobs.getRange('B3').formulas=[[`=COUNTA(A5:A${jr.end})`]];jobs.getRange('C3').values=[['学位+暑期匹配数']];jobs.getRange('D3').formulas=[[`=COUNTIF(F5:F${jr.end},"A 学位与暑期匹配")`]];
jobs.getRange('F3').values=[['T=人才/项目池；B=待确认；C=排除/对照']];
base(companies,'公司观察 · 46家公司','检索范围与入口审计；“未确认”不等于未开放。公司主页和历史职位不计入可申请岗位数。');
table(companies,data.companies,[['company','公司',24],['region','地区',15],['finding','本次核验结论',70],['direction','方向',20],['next_action','限制与下一检查点',80],['verification','核验层级',50],['checked','核验日期',15],['source','官方入口/线索',95]],'CompanyWatch');
companies.tabColor='#667B8B';
base(directions,'方向与简历对应','D1–D3为主要方向；D4/D5为相邻强方向。只用已有事实改写，不把JD关键词补写成经历。');
table(directions,data.directions,[['id','版本',10],['name','方向',42],['level','定位',35],['focus','简历重点',65],['evidence','现有证据',75],['jd','代表JD',68],['gap','主要缺口',70],['resume','可编辑LaTeX路径（相对工作区）',75]],'ResumeMap');
directions.getRange('A5:H9').format.rowHeight=50;directions.tabColor='#7D738C';
wb.recalculate();
const validation=await wb.inspect({kind:'table',range:'岗位清单!A3:H9',include:'values,formulas',tableMaxRows:7,tableMaxCols:8,maxChars:4000});
await fs.writeFile(path.join(root,'qa/workbook/inspection.json'),validation.ndjson);
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},summary:'Final error scan',maxChars:2000});
await fs.writeFile(path.join(root,'qa/workbook/errors.json'),errors.ndjson);
const xlsx=await SpreadsheetFile.exportXlsx(wb);await xlsx.save(path.join(output,'2027_Internship_Research.xlsx'));
execFileSync('/home/ziyu/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',[path.join(root,'scripts/add_xlsx_hyperlinks.py'),path.join(output,'2027_Internship_Research.xlsx')],{stdio:'inherit'});
for(const [s,range,name] of [['岗位清单','A1:H10','jobs'],['公司观察','A1:E11','companies'],['方向与简历对应','A1:F9','directions'],['岗位清单','I4:R10','jobs_dates'],['岗位清单','S4:X10','jobs_fit'],['岗位清单','Y4:AE10','jobs_sources'],['公司观察','F4:H11','companies_sources'],['方向与简历对应','G4:H9','directions_paths']]){
 const image=await wb.render({sheetName:s,range,scale:1.5,format:'png'});await fs.writeFile(path.join(root,`qa/workbook/${name}.png`),new Uint8Array(await image.arrayBuffer()));
}
console.log(JSON.stringify({jobs:data.jobs.length,companies:data.companies.length,file:path.join(output,'2027_Internship_Research.xlsx'),inspection:validation.ndjson,errors:errors.ndjson}));
