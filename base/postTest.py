import urllib2
import json


url="http://localhost/shop/userC/login"
headers = {"Content-Type": "application/json"}

for i in range(1,30):
    data = {
        "username": i,
        "password": i
    }
    data = json.dumps(data)
    request = urllib2.Request(url,data)
    request.add_header("Content-Type","application/json")
    try:
        response = urllib2.urlopen(request)
        print response.info()
        print response.read()
    except urllib2.HTTPError,e:
        print e.getcode()
        print e.reason





# data = {
#     "username": "admin",
#     "password": "123456"
# }


