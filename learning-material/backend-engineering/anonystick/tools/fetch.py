import json,subprocess,os,glob,time,sys
sys.path.insert(0,'tools'); from vtt2txt import to_text
Q=json.load(open('tools/queue.json')); SF='tools/state.json'
st=json.load(open(SF)) if os.path.exists(SF) else {}
YT=os.path.expanduser('~/.local/bin/yt-dlp')
limit=int(sys.argv[1]) if len(sys.argv)>1 else 10**9
consec=0;n=0
for v in Q:
    vid=v['id']
    if st.get(vid,{}).get('status') in ('transcript','members_only','no_subs','unavailable'): continue
    if n>=limit: break
    have=glob.glob(f'subs/{vid}.vi*.vtt')
    err=""
    if not have:
        p=subprocess.run([YT,'--js-runtimes','node','--extractor-args','youtube:player_client=web_safari,android',
            '--sleep-requests','1','--sleep-interval','2','--skip-download','--write-subs','--write-auto-subs',
            '--sub-langs','vi','--sub-format','vtt','-o','subs/%(id)s.%(ext)s',f'https://www.youtube.com/watch?v={vid}'],
            capture_output=True,text=True,timeout=180)
        err=(p.stderr or "")
        have=glob.glob(f'subs/{vid}.vi*.vtt')
    n+=1
    if have:
        vtt=sorted(have,key=len)[0]
        open(f'transcripts/{vid}.vi.txt','w').write(f"# {v['title']}\n# https://www.youtube.com/watch?v={vid}\n# Vietnamese auto-captions (may contain errors), from {os.path.basename(vtt)}\n\n"+to_text(vtt))
        st[vid]={'status':'transcript','topic':v['topic']}; consec=0
    elif 'members-only' in err or 'Join this channel' in err:
        st[vid]={'status':'members_only','topic':v['topic']}; consec=0
    elif 'not a bot' in err or '429' in err:
        consec+=1; st[vid]={'status':'blocked_retry','topic':v['topic'],'err':err.strip().splitlines()[-1][:200]}
        print('BLOCK',vid,st[vid]['err'],flush=True)
        if consec>=3: print('STOP: repeated blocks',flush=True); json.dump(st,open(SF,'w'),indent=0); break
        time.sleep(60*consec)
    elif 'Video unavailable' in err or 'Private video' in err:
        st[vid]={'status':'unavailable','topic':v['topic']}
    else:
        st[vid]={'status':'no_subs','topic':v['topic'],'err':(err.strip().splitlines() or [''])[-1][:200]}
    print(n,vid,st[vid]['status'],flush=True)
    json.dump(st,open(SF,'w'),indent=0)
    time.sleep(3)
print('DONE batch',flush=True)
