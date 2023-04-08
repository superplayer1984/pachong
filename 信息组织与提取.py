import requests
import re
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
# for link in soup.find_all('a'):
#     print(link.get('href'))


# print(soup.find_all(['a','b']))
#
# for tag in soup.find_all(True):
#     print(tag.name)


# for tag in soup.find_all(id = re.compile("link")):
#     print(tag)

soup.find_all(id = re.compile("link"))
print(soup(id = re.compile("link")))
