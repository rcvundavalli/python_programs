import requests
import json

status = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
if status.status_code == 200:
    li = status.json()
    print(li)
    for i in li:
        print(i["body"])
        print("=====================")
