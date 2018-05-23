import requests
import b

def age(x):
    return x * 365 * 24 * 3600


x = 30
dict = {"name1" : "Zeeshan Mulk",
        "name2" : "Adrita Mulk"}

r = requests.get("http://www.google.ca")
content = r.content()
soup = beautifulsoup4(content, "html.parser")


# <span id="priceblock_ourprice" class="a-size-medium a-color-price">CDN$ 94.88</span>


print ("name5" in dict)