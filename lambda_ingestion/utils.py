import time
import logging

def retry(func, retries=2, delay=5):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            logging.warning(f"Retry {attempt+1} failed: {e}")
            time.sleep(delay)
    raise Exception("All retries failed")
