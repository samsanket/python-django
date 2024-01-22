import requests;


endpoint = "https://httpbin.org/status/200/";

endpoint = "https://httpbin.org";

get_response = requests.get(endpoint)      #HTTP GET REQUEST
print(get_response.text)
print(get_response.request)
print(get_response.url)
