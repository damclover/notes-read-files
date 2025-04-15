# IMPORT
import sys
import requests

# FUNCTION
def get_payloads(raw_url):
    try:
        response = requests.get(raw_url, stream=True, timeout=5)
        if response.status_code == 200:
            for line in response.iter_lines():
                payload = line.decode("utf-8").strip()
                if payload:
                    yield payload
        else:
            print("[X] Error accessing the payloads.")
            sys.exit(1)
    except requests.RequestException:
        print("[X] Failed to connect to the payloads URL.")
        sys.exit(1)

# ARRAY (treat the function as an array)
payloads = get_payloads("https://raw.githubusercontent.com/payloadbox/xss-payload-list/refs/heads/master/Intruder/xss-payload-list.txt")
for payload in payloads:
  # code here.........
