import json,datetime,sys
sys.path.insert(0,'tools'); from topics import TOPICS, topic
e=json.load(open('videos.json'))['entries']
def d(x):
  t=x.get('timestamp'); return datetime.datetime.fromtimestamp(t,datetime.UTC).strftime('%Y-%m') if t else '?'
def dur(s):
  if not s: return '?'
  s=int(s); return f"{s//3600}:{s%3600//60:02d}:{s%60:02d}" if s>=3600 else f"{s//60}:{s%60:02d}"
groups={k:[] for k,_,_ in TOPICS}
for i,x in enumerate(e,1): groups[topic(x['title'])].append((i,x))
L=["# anonystick YouTube channel: full video list, grouped by topic","",
f"Source: https://www.youtube.com/@anonystick (Vietnamese backend/dev channel, credit: anonystick / Tips Javascript). Pulled {datetime.date.today()} with `yt-dlp --flat-playlist`.","",
f"**Total videos on the /videos tab: {len(e)}.** Grouped into {len(TOPICS)} topic areas below, in the suggested learning order (foundations first). Each video is in exactly one group (first matching topic wins), so a few cross-topic videos sit in an earlier group.","",
"Notes on the data:","- Titles are as YouTube returned them; YouTube auto-translates some titles into English, others stay Vietnamese.",
"- Upload month is approximate (YouTube only shows \"x months/years ago\").",
"- Views `?` = YouTube hid the count. Almost all of these are **members-only** videos (channel membership required): subtitles for those can't be fetched without signing in, which we don't do.",
"- Playlists: [WeekDaily - Con đường Lập Trình Viên](https://www.youtube.com/playlist?list=PLw0w5s5b9NK5xdGY8OyU9OrUl8Zkb7k3M), [Git vs GitHub](https://www.youtube.com/playlist?list=PLw0w5s5b9NK7dTWqY1li4u4_dZMNeSjQv). The channel also has YouTube \"Courses\", which yt-dlp can't list yet.",
"- Processing status per video: see [PROGRESS.md](PROGRESS.md).","","## Topic areas","",]
for k,l,_ in TOPICS: L.append(f"- [{l}](#{k}) ({len(groups[k])} videos)")
for k,l,_ in TOPICS:
  L+=["",f'<a id="{k}"></a>',f"## {l}","","| # | Upload (approx.) | Title | Duration | Views | Link |","|---|---|---|---|---|---|"]
  for i,x in groups[k]:
    t=x['title'].replace('|','\\|')
    L.append(f"| {i} | {d(x)} | {t} | {dur(x.get('duration'))} | {x.get('view_count') if x.get('view_count') is not None else '?'} | https://www.youtube.com/watch?v={x['id']} |")
open('video-list.md','w').write("\n".join(L)+"\n")
# queue: learning order; public first; within topic oldest first (series order)
order={k:n for n,(k,_,_) in enumerate(TOPICS)}
pri=["aJ5kLfn8AtI","inUimYVAGv0","DQN0pRV8RnU","9kpISaXHBvM","GLqyIqWtRiA"]
rows=[]
for k in groups:
  for i,x in groups[k]: rows.append((x.get('view_count') is None, order[k], -i, x['id'], k, x['title']))
rows.sort()
q=[r for r in rows if r[3] in pri]; q.sort(key=lambda r: pri.index(r[3])); q+= [r for r in rows if r[3] not in pri]
json.dump([{"id":r[3],"topic":r[4],"title":r[5],"members_guess":r[0]} for r in q],open('tools/queue.json','w'),ensure_ascii=False,indent=0)
for k,l,_ in TOPICS: print(l,len(groups[k]))
