from googleapiclient.http import MediaFileUpload
import math, time, tqdm, googleapiclient.errors, toml

_cfg = toml.load("config.toml")

def upload(service, path, title, description):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": _cfg["tags"],
            "categoryId": str(_cfg["category_id"]),
        },
        "status": {
            "privacyStatus": _cfg["privacy"],
            "selfDeclaredMadeForKids": True
        }
    }
    media = MediaFileUpload(path, resumable=True)
    request = service.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    pbar = tqdm.tqdm(total=math.ceil(media.size()/256_000), unit="chunks")
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                pbar.update(status.resumable_progress/256_000 - pbar.n)
        except googleapiclient.errors.HttpError as e:
            if e.resp.status in [500, 502, 503, 504]:
                time.sleep(2)
                continue
            raise
    pbar.close()
    return response["id"]
