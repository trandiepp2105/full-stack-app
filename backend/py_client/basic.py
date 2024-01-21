import requests


endpoint = "http://localhost:8000/api/product/"
# endpoint = "https://httpbin.org/anything"
get_response = requests.get(endpoint, json={"productId": "1"}) # HTTP Request
print(get_response)
print(get_response.json()) # print raw text response
# # print(get_response.status_code)
# print(get_response.text) # print raw text response

# # print(get_response.json())
# print(get_response.status_code)