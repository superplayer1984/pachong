import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
tap = soup.head

# print(type(tap.contents))
# print(soup.body.children)
# for item in soup.body.children:
#     print(item)

# print(soup.title.parent)

print(soup.a.next_sibling)
print(soup.a.previous_sibling)

