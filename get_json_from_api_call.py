import requests

# build the API URL
api_url = 'http://someAPIaddress/?lon='+str(-112.57027151831147)+'&lat='+str(35.41778464478152)
# execute the API call and store the returned response
response = requests.get(api_url)
# print the response as JSON
print(response.json())
