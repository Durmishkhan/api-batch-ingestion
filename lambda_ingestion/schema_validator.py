REQUIRED_FIELDS = ["timestamp", "temperature_2m", "precipitation"]

def validate_records(records):
    valid = []
    for record in records:
        if all(field in record and record[field] is not None for field in REQUIRED_FIELDS):
            valid.append(record)
    return valid
