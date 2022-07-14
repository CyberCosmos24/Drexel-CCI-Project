
import requests

print("1 - GET Method ")
print("2 - POST Method")
print("3 - DELETE Method")
web = input("Enter the url: ")
m = input("Enter the method number you want to use: ")


if m == 1:
    r = requests.get(web)
    print("Status Code:", r.status_code)
    print("URL:", r.url)
    print(r.content)

elif m == 2:
    r = requests.post(web)
    print("Status Code:", r.status_code)
    print("URL:", r.url)
    print(r.json())
else: 
    r = requests.head(web)
    print("Status Code:", r.status_code)
    print("URL:", r.url)
    print(r.headers)
    print(r.content)
    