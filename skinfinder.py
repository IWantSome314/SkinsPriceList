import requests
gun=str(input("Please enter the gun: "))
skinnameuser=str(input("Please enter the skin name: "))
skinname = skinnameuser.replace(" ", "%20")
wearuser=str(input("Please enter the wear: "))
if wearuser == "Factory New":
    wear=wearuser.replace(" ", "%20")
else:
    wear=wearuser.replace(" ", "-")
gunSelected= requests.get(f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={gun}%20%7C%20{skinname}%20({wear})")
print(f"Here is your {skinnameuser} {gun} in {wearuser}")
print(gunSelected.text)
