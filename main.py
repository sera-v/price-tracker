import json
from notifier import send_ntfy_notification
from get_price import get_ebay_price
from datetime import datetime

def load_config():
    with open('config.json', 'r') as cfile:
        data = json.load(cfile)
        return data

def save_price(price):
    with open('price_history.json', 'r') as pfile:
        data = json.load(pfile)

    data[datetime.now().isoformat()] = price

    with open('price_history.json', 'w') as pfile:
        json.dump(data, pfile, indent=4)

def main():
    config = load_config()
    url = config['ebay_url']
    target = config['target_price']

    currency, price = get_ebay_price(url)
    
    #save it
    save_price(price)
    
    print(f"Current price: {currency} {price:.2f}")

    if price <= target:
        print("Target reached.")
        send_ntfy_notification(config['ntfy_topic_name'], url)
    else:
        print("Target not reached...")



if __name__ == "__main__":
    main()
