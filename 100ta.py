import requests
l=[]
for i in range(100):
    x=requests.get("https://randomuser.me/api/")
    data=x.json()
    lst=data['results'][0]['name']
    dct={'firstname':lst['first'],'lastname':lst['last']}
    l.append(dct)
print(l)