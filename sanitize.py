import re
BANNED = {"subscribe", "giveaway", "18+"}

def clean(text: str) -> str:
    out = re.sub(r"\s{3,}", "  ", text)
    if any(w in out.lower() for w in BANNED):
        out = out.replace("subscribe", "join us")
    return out
