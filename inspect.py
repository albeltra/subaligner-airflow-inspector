import json
import os

mediaFile = os.environ.get("mediaFile")
mediaInfo = os.environ.get("mediaInfo")
stream_index = os.environ.get("stream_index", "0")
audio_channel = os.environ.get("audio_channel", "0")

if mediaInfo and mediaFile:
    media_path = mediaFile.get("path")

if media_path is not None:
    with open("/airflow/xcom/return.json", "w") as f:
        json.dump({"MEDIA_PATH": media_path, "STREAM_INDEX": stream_index, "AUDIO_CHANNEL": audio_channel}, f)
