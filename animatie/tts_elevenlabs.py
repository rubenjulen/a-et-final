#!/usr/bin/env python3
"""Spreek de zinnen van een clip in met ElevenLabs (stem Matilda).

Gebruik:  python3 tts_elevenlabs.py <zinnen.json> <public/aud_map> [--dry]
- zinnen.json: lijst van [sleutel, tekst, pauze]
- de uitspraaklijst uitspraak.json (regex -> uitspraak) wordt alleen op de stemtekst toegepast;
  de ondertitels houden de gewone schrijfwijze
- bestaande mp3's worden overgeslagen, zodat herkansingen alleen de gewiste zinnen opnieuw maken
- de sleutel komt uit de omgevingsvariabele ELEVENLABS_API_KEY; in de cloudsessie zet de proxy
  de echte sleutel in de header en volstaat een placeholder
"""
import json, os, re, sys, urllib.request

VOICE = "XrExE9yKIg1WjnnlVkGX"   # Matilda
MODEL = "eleven_v3"
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128"
HERE = os.path.dirname(os.path.abspath(__file__))


def lexicon():
    p = os.path.join(HERE, "uitspraak.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


def spoken(text, lex):
    for pat, rep in lex.items():
        text = re.sub(pat, rep, text)
    return text


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    zinnen, outdir, dry = sys.argv[1], sys.argv[2], "--dry" in sys.argv
    os.makedirs(outdir, exist_ok=True)
    lex, key = lexicon(), os.environ.get("ELEVENLABS_API_KEY", "proxy-injected")
    total = 0
    for k, txt, _ in json.load(open(zinnen, encoding="utf-8")):
        out = os.path.join(outdir, f"{k}.mp3")
        if os.path.exists(out):
            continue
        t = spoken(txt, lex)
        total += len(t)
        if dry:
            print(f"{k}: {t}")
            continue
        body = json.dumps({"text": t, "model_id": MODEL, "language_code": "nl",
                           "voice_settings": {"stability": 0.5}}).encode()
        req = urllib.request.Request(URL, data=body, method="POST", headers={
            "xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f:
            f.write(r.read())
        print("ok", k)
    print(f"tekens {'te spreken' if dry else 'gesproken'}: {total}")


if __name__ == "__main__":
    main()
