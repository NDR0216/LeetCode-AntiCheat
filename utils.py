import json
import random
import sys
import urllib.error
import urllib.request

headers1 = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"126.0.6478.127"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

headers2 = headers1.copy()
headers2['referer'] = 'https://leetcode.com/contest/'

def get_question_id(CONTEST_URL):
    status = 0
    for _ in range(10):
        try:
            req = urllib.request.Request(CONTEST_URL, headers=random.choice([headers1, headers2]))
            r = urllib.request.urlopen(req)
            response = json.loads(r.read())
        except urllib.error.HTTPError as e:
            status = e.code
        except:
            pass
        else:
            break
    else:
        print("Status", status, CONTEST_URL)
        sys.exit()

    return response