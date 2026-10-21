#!/home/box/.venvs/whisper/bin/python
"""Usage: transcribe.py <audio.wav> <out.txt> [--model small|medium|large-v3-turbo] [--threads N]
Transcribes Vietnamese audio on CPU (int8) with faster-whisper; writes "MM:SS text" lines
(HH:MM:SS once past an hour). Models cache in ~/.cache/huggingface."""
import argparse, sys, time
from faster_whisper import WhisperModel

def ts(sec: float) -> str:
    s = int(sec); h, rem = divmod(s, 3600); m, s = divmod(rem, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("out")
    ap.add_argument("--model", default="medium")
    ap.add_argument("--threads", type=int, default=6)
    ap.add_argument("--beam", type=int, default=1)
    ap.add_argument("--prompt", default="Bài giảng lập trình Java Spring Boot, Kafka, Redis, Saga, Outbox, idempotency, microservices.",
                    help="initial prompt to bias technical vocabulary")
    a = ap.parse_args()
    t0 = time.time()
    model = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=a.threads)
    segs, info = model.transcribe(a.audio, language="vi", beam_size=a.beam, vad_filter=True,
                                  initial_prompt=a.prompt, condition_on_previous_text=False)
    n = 0
    with open(a.out, "w", encoding="utf-8") as f:
        for s in segs:
            line = f"{ts(s.start)} {s.text.strip()}"
            f.write(line + "\n"); f.flush(); n += 1
            print(line, flush=True)
    el = time.time() - t0
    print(f"[done] {n} segments, audio {info.duration:.0f}s, wall {el:.0f}s, "
          f"RTF {el/max(info.duration,1):.2f}, model {a.model}", file=sys.stderr)

if __name__ == "__main__":
    main()
