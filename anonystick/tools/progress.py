import json,os,sys,datetime
sys.path.insert(0,'tools'); from topics import TOPICS, topic; from indexes import NAMES
e=json.load(open('videos.json'))['entries']; st=json.load(open('tools/state.json')) if os.path.exists('tools/state.json') else {}
Q=[v['id'] for v in json.load(open('tools/queue.json'))]
byid={x['id']:x for x in e}
def status(i):
  s=st.get(i,{}).get('status','pending')
  if s=='transcript' and os.path.exists(f'{i}.md'): return 'note_done'
  return s
cnt={}
for i in byid: cnt[status(i)]=cnt.get(status(i),0)+1
lab={'note_done':'✅ note written','transcript':'📝 transcript fetched, note pending','members_only':'🔒 members-only (skipped: needs channel membership + sign-in)',
'no_subs':'⚠️ no Vietnamese captions available','unavailable':'❌ unavailable','blocked_retry':'⏳ rate-limited (429), retry later','pending':'⬜ not attempted yet'}
L=["# anonystick: processing progress","",f"Updated: {datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M UTC')}. Channel: https://www.youtube.com/@anonystick. Total videos: **{len(e)}**.","",
"## Summary",""]+[f"- {lab[k]}: **{cnt.get(k,0)}**" for k in lab]+["",
"## How to continue","","```bash","cd /workspace/research/teaching-material/anonystick",
"python3 tools/fetch.py        # resumes from tools/state.json; polite pace (--sleep-requests 1 --sleep-interval 2, 3s between videos, backs off on 429, stops after 3 blocks in a row)",
"python3 tools/progress.py     # regenerates this file","```","",
"Then write notes for 📝 rows: read `transcripts/<id>.vi.txt` and write `<id>.md` in the Obsidian literature-note format (see any existing note). The order below is the suggested learning order (foundations first).","",
"## Queue (learning order)","","| Order | Status | Topic index | Title | Video | Transcript | Note |","|---|---|---|---|---|---|---|"]
for n,i in enumerate(Q,1):
  x=byid[i]; s=status(i); k=topic(x['title'])
  tr=f"[txt](transcripts/{i}.vi.txt)" if os.path.exists(f'transcripts/{i}.vi.txt') else ""
  nt=f"[[{i}]]" if os.path.exists(f'{i}.md') else ""
  L.append(f"| {n} | {lab[s].split(' ')[0]} {s} | [[{NAMES[k]}]] | {x['title'].replace('|','/')} | https://www.youtube.com/watch?v={i} | {tr} | {nt} |")
open('PROGRESS.md','w').write("\n".join(L)+"\n"); print(cnt)
