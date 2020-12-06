import requests
import json

def SendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {
        "authorization": "nUYIufzDstXgeEcjHhmpNJTy0aZ6wxQLdqRk3C184OKM5bSGWvfpoCHAstWwNe0yx6VMPKIZhjl5YBc3",
        "sender_id": "FSTSMS",
        "message": message,
        "language": "english", "route": "p",
        "numbers":contactno
    }

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data=response.text
    s=json.loads(json_data)

    return  s['return']

