import requests

def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text)

    except:
        return "产生异常"
if __name__ == "__main__":
    url = "https://python123.io/ws/demo.html"
    getHTMLText(url)