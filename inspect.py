import json
with open("/airflow/xcom/return.json", "w") as f:
    json.dump({"MEDIA_PATH": "", "STREAM_INDEX": "0", "AUDIO_CHANNEL": "0"}, f)