import linecache
import json
import requests


start = 1
end = 10000

i = start

while i < end:
    # read a specific line
    line = linecache.getline('./output.txt', i)
    #print(line)
    # write the line to the API
    myjson = json.loads(line)
    
    print(myjson)
    
    response = requests.post('http://localhost:80/post_bank_clients', json=myjson)

    # Use this for dedbugging
    #print("Status code: ", response.status_code)
    #print("Printing Entire Post Request")
    print(response.json())

    # increase i
    i+=1
