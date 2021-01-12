import requests

#Gets the current version of requests package
version = requests.__version__

#Gets the google Homepage
google = requests.get("https://www.google.com")

#Gets the prints the script.py file uploaded on Github
github = requests.get("https://raw.github.com/kli885/CMPUT404-Lab1/master/script.py")
print(github.text)