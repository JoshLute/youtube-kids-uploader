import os, toml, openai
from dotenv import load_dotenv   # ← new

load_dotenv()                    # ← new (MUST come before you read the key)

_cfg = toml.load("config.toml")
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate(video_name: str):
    prompt = _cfg["prompt"].format(filename=video_name)
    resp = openai.ChatCompletion.create(
        model=_cfg["model"],
        messages=[{"role": "user", "content": prompt}]
    )
    raw = resp.choices[0].message.content.strip()
    title, *desc = raw.splitlines()
    description = "\n".join(desc).strip() or title
    return title[:100], description[:5000]
