
import requests

url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?'
url += 'api_key=2931c2b78a4d736c57f88750b643483fc9c55bce'
url += '&Accept-Language=ja'
url += '&version=2016-05-20'
url += '&url=http://nichibi-ogaki.sakura.ne.jp/robothackathon/tmp.jpeg'

res = requests.get(url)
print(res.text)