import json
import os
import base64

print(os.environ.get("mediaFile"))
print(os.environ.get("mediaInfo"))
mediaFile = json.loads(os.environ.get("mediaFile"))
print(mediaFile)
mediaInfo = json.loads(os.environ.get("mediaInfo"))
stream_index = os.environ.get("stream_index") if os.environ.get("stream_index") else "0"
audio_channel = os.environ.get("audio_channel") if os.environ.get("audio_channel") else "0"

if mediaInfo and mediaFile:
    media_path = mediaFile.get("path")

if media_path is not None:
    with open("/airflow/xcom/return.json", "w") as f:
        json.dump({"MEDIA_PATH": media_path, "STREAM_INDEX": stream_index, "AUDIO_CHANNEL": audio_channel}, f)
