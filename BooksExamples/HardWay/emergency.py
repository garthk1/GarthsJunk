import urllib.request
import time



def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return(text[start_of_price:end_of_price])

price = float(get_price())


while price > 4.74:
    time.sleep(900)
    price = float(get_price())

print(price)
print("Buy!")

'''
# http://beans.itcarlow.ie/prices-loyalty.html
'''