import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    website_content = response.text
    
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("title")
    if title_tag:
        title_text = title_tag.text.strip()
        print("Page title:", title_text)
    else:
        print("Title tag not found.")
    

else:
    print("Request failed with status code:", response.status_code)
