import boto3
import json
from datetime import datetime

s3 = boto3.client("s3")
BUCKET = "my-data-pipeline-landing-zone"

def write_to_s3(records):
    if not records:
        return

    first_ts = records[0]["timestamp"]
    dt = datetime.fromisoformat(first_ts)

    key = f"raw/open-meteo/{dt.year}/{dt.month:02}/{dt.day:02}/data.json"
    body = json.dumps(records)

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=body.encode("utf-8"),
        ContentType="application/json"
    )
