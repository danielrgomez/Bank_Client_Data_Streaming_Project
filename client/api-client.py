import linecache
import json
import requests


start = 1
end = 5000

i = start

with open('./output.txt') as f:
    json_data = json.load(f)
response = requests.post('http://localhost:80/post_bank_clients', json=json_data)
