# YouTube Kids Uploader

CLI tool that:
1. Generates a kid‑friendly title & description with OpenAI.
2. Uploads a video to YouTube as **public** and **made for kids**.
3. Caches OAuth token for painless re‑runs.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install poetry
poetry install --no-dev

# add keys
cp .env.example .env    # fill OPENAI_API_KEY
# place Google OAuth client as credentials.json

python -m uploader.cli path/to/video.mp4
```
