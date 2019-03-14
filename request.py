import requests
res = requests.post('http://localhost:5000/api/sink/', json={"mytext":"lalala"})
if res.ok:
    print(res.text)
