import re

url = input("Enter a URL: ")

pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/.*)?$"

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")