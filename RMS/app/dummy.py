import requests
import json
url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"nUYIufzDstXgeEcjHhmpNJTy0aZ6wxQLdqRk3C184OKM5bSGWvfpoCHAstWwNe0yx6VMPKIZhjl5YBc3",
               "sender_id":"FSTSMS",
               "message":"happy sunday","language":"english","route":"p","numbers":"7801016383"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

x=response.text
print(json.loads(x))