import requests
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
def requestuser(username):
    response = requests.get('https://api.chess.com/pub/player/' + username,headers=headers)
    response = json.loads(response.content)
    if 'code' in response:
        if response['code'] == 0:
            return(False)
        else:
            return(True)
    else:
        return(True)    