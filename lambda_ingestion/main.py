import logging
from api_client import fetch_data
from schema_validator import validate_records
from s3_writer import write_to_s3
from metrics import emit_metric
from utils import retry

def lambda_handler(event, context):
    try:
        records = retry(fetch_data, retries=2, delay=5)

        valid_records = validate_records(records)

        write_to_s3(valid_records)
        
        emit_metric(len(valid_records))

        logging.info(f"Ingestion succeeded: {len(valid_records)} records written")

    except Exception as e:
        logging.error(f"Ingestion failed: {e}")
        raise e
