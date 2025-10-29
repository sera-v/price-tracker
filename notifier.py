import requests

def send_ntfy_notification(topic, url):
    print("sending notif...")
    requests.post(f"https://ntfy.sh/{topic}",
        data = f"Your target price on {topic} has been reached!".encode(encoding='utf-8'))