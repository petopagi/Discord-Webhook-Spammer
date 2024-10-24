import requests
import json
import time

def send_discord_webhook(webhook_url, content):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        'content': content
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))

    return response

# Example usage:
if __name__ == "__main__":
    # Replace LINK with webhook
    webhook_url = 'LINK'
    
    while True:
        # Replace TEXT with text that you want to spam
        content = 'TEXT'

        response = send_discord_webhook(webhook_url, content)

        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(response.text)

        # 
        time.sleep(0.01)
