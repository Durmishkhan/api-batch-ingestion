import boto3
import json
from datetime import datetime

s3 = boto3.client("s3")
BUCKET = "my-data-pipeline-landing-zone"

def write_hourly_records(records):
    if not records:
        return

    first_record = records[0]
    ts = datetime.fromisoformat(first_record["timestamp"])
    
    partition = f"{ts.year}/{ts.month:02}/{ts.day:02}/{ts.hour:02}"
    
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    s3_key = f"raw/open-meteo/{partition}/data_{timestamp_str}.json"
    
    body = json.dumps(records, indent=2)
    
    s3.put_object(
        Bucket=BUCKET,
        Key=s3_key,
        Body=body.encode("utf-8"),
        ContentType="application/json"
    )
    
    print(f" Written {len(records)} records to {s3_key}")