import requests

def fetch_data():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=41.72&longitude=44.78"
        "&hourly=temperature_2m,precipitation"
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

        # Combine into list of records
        records = []
        for i in range(len(times)):
            record = {
                "timestamp": times[i],
                "temperature_2m": temperatures[i],
                "precipitation": precipitation[i]
            }
            records.append(record)

        return records

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")
