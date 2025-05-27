import argparse, pathlib
from .auth import get_service
from .gpt import generate
from .sanitize import clean
from .youtube import upload

def main():
    ap = argparse.ArgumentParser(description="Upload kid‑safe video in one line")
    ap.add_argument("video", type=pathlib.Path)
    ap.add_argument("--dry", action="store_true", help="preview only, no upload")
    args = ap.parse_args()

    title, desc = generate(args.video.name)
    title, desc = clean(title), clean(desc)

    print("TITLE:", title, "\nDESC:", desc, "\n")
    if args.dry:
        return

    yt = get_service()
    vid_id = upload(yt, str(args.video), title, desc)
    print("✅ Uploaded: https://youtu.be/{}".format(vid_id))

if __name__ == "__main__":
    main()
