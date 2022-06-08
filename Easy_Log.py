import requests
import time

#Message
key = input("license key: ")

#Put here the Url with the passwords in a list#
url = "https://pastebin.com/raw/FBsrcriE"

#Get The Url
r = requests.get(url)

#print the passwords in the list
print(f"Key is {r.text}")

#try request the url and get and confirm if the passwords exists
try:

    if key in r.text:
        print("valid key")
        pass
    else:
        print("invalid key!")
        time.sleep(30)
        exit()
except:
    print("somthing went worng")
    time.sleep(30)
    exit()
