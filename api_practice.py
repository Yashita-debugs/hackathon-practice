import requests


try:
    response = requests.get("https://api.github.com/users/Yashita-debugs")
    data = response.json()
    if response.status_code==200:
        print(data)
        print(data["login"])
        print(data["public_repos"])
    else:
        print("Error: ",response.status_code)
except requests.exceptions.RequestException:
    print("Could not connect")
