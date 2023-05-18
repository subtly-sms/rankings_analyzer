import requests
from bs4 import BeautifulSoup

response = requests.get("")

print(response.status_code)
soup = BeautifulSoup(response, 'html.parser')
print(soup.prettify())