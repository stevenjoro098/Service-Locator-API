import requests
url = 'http://127.0.0.1:8000'
headers = {'Accept': 'application/json'}
data = {'category':"Programming",
        'owner':'cars',
        'name':'Test',
        'contact':12345,
        'email':'s@gmail.com',
        'lat':1.0,
        'lon':1.0,
        'description':'Test Description'}
req = requests.post(url=url+'/services/', data=data,headers=headers)
print(req.json())