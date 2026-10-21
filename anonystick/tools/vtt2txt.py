import re,sys
def parse(path):
    """Return list of (start_seconds, text) with rolling auto-caption duplicates removed."""
    out=[];seen_last=""
    blocks=open(path,encoding='utf-8').read().split("\n\n")
    for b in blocks:
        m=re.search(r"(\d+):(\d+):(\d+)\.\d+ -->",b)
        if not m: continue
        s=int(m[1])*3600+int(m[2])*60+int(m[3])
        lines=[re.sub(r"<[^>]+>","",l).strip() for l in b.split("\n")[1:] if "-->" not in l]
        lines=[l for l in lines if l]
        for l in lines:
            if l==seen_last or (out and l==out[-1][1]): continue
            out.append((s,l)); seen_last=l
    # dedupe lines that repeat anywhere in a 3-line window
    res=[]
    for s,l in out:
        if any(l==x[1] for x in res[-3:]): continue
        res.append((s,l))
    return res
def to_text(path, every=30):
    rows=parse(path); buf=[];cur=None;out=[]
    for s,l in rows:
        if cur is None or s-cur>=every:
            if buf: out.append(f"[{cur//60:02d}:{cur%60:02d} | t={cur}s] "+" ".join(buf))
            buf=[];cur=s
        buf.append(l)
    if buf: out.append(f"[{cur//60:02d}:{cur%60:02d} | t={cur}s] "+" ".join(buf))
    return "\n".join(out)+"\n"
if __name__=="__main__": print(to_text(sys.argv[1]))
