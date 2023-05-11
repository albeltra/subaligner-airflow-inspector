import json
import os

media_path = os.environ.get("MEDIA_PATH")
with open("/airflow/xcom/return.json", "w") as f:
    json.dump({"MEDIA_PATH": media_path, "STREAM_INDEX": "0", "AUDIO_CHANNEL": "0"}, f) 