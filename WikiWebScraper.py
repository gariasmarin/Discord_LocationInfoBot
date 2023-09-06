import requests
from bs4 import BeautifulSoup


page = requests.get("https://en.wikipedia.org/wiki/Raleigh,_North_Carolina")

soup = BeautifulSoup(page.content, 'html.parser')

list(soup.children)

# find all occurrence of p in HTML
# includes HTML tags
print(soup.find_all('p'))

print('\n\n')

# return only text
# does not include HTML tags
print(soup.find_all('p')[0].get_text())