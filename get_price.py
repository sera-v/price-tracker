import requests
import random
from bs4 import BeautifulSoup
import re

def get_ebay_price(url):

    USER_AGENTS = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    , "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    , "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    , "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0"
    , "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
    , "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    ]
    HEADERS = {"User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    response = requests.get(url, headers=HEADERS)

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    price_container = soup.find("div", {"class":"x-price-primary"})
    price = price_container.find("span", {"class": "ux-textspans"})

    #clean the prices
    price_text = price.get_text().replace(",","").strip()

    *currency, amount = price_text.split()
    currency = ''.join(currency)
    amount_clean = re.sub(r'[^\d.]', '', amount)
    amount_float= float(amount_clean)


    return currency, amount_float
