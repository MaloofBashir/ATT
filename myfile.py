import time
import requests

# Replace with your actual website URL
URL = "https://collegedext.onrender.com"

def keep_alive():
    while True:
        try:
            response = requests.get(URL)
            print(f"Pinged {URL} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        
        # Wait for 14 minutes (14 * 60 seconds)
        time.sleep(10 * 60)

if __name__ == "__main__":
    keep_alive()