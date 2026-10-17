import json
student=[{"name":"Yashita","Branch":"BCA","Year":2},{"City":"Gurgaon","age":19,"Profession":"student"}]
with open("data.json","w") as f:
    json.dump(student,f)
try:
    with open("data.json1","r") as f:
        loaded=json.load(f)
        print(loaded)
        print(loaded[0]["name"])
except FileNotFoundError:
    print("Pls enter the correct file name ")
