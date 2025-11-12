import requests
from datetime import datetime, timedelta

def fetch_data():
    """
    Fetch ONLY current hour's weather data
    """

    now = datetime.utcnow()
    current_hour = now.replace(minute=0, second=0, microsecond=0)
    
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=41.72&longitude=44.78"
        "&hourly=temperature_2m,precipitation"
        "&forecast_days=1"
    )
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Extract hourly records
        hourly = data.get("hourly", {})
        times = hourly.get("time", [])
        temperatures = hourly.get("temperature_2m", [])
        precipitation = hourly.get("precipitation", [])

        records = []
        for i in range(len(times)):
            # Parse timestamp
            timestamp_str = times[i]
            
            # Handle ISO format (2025-11-12T14:00)
            if "T" in timestamp_str:
                record_time = datetime.fromisoformat(timestamp_str)
            else:
                record_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
            
            # Round to hour
            record_hour = record_time.replace(minute=0, second=0, microsecond=0)
            
            if record_hour == current_hour:
                record = {
                    "timestamp": times[i],
                    "temperature_2m": temperatures[i],
                    "precipitation": precipitation[i]
                }
                records.append(record)
        
        print(f"📥 Fetched {len(records)} records for hour: {current_hour}")
        return records

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")