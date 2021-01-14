import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'0':'abroad', '1': 'capital','2':
       'court', '3':'covid19-update', '4':'cricketworldcup2019', '5':'economy',
       '6':'education', '7':'entertainment',
       '8':'national', '9':'politics',  '10':'scienceandtechnology', '11':'sports',
       '12':'wholecountry', '13':'worldnews'})

print(r.json())
