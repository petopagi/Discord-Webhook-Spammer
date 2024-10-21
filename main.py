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
    # Replace webhook sem s webhook linkom
    webhook_url = 'https://discord.com/api/webhooks/1171917799451545620/4vIld5YItk_gqjeTZRVuYwN_zAxRuPkaJFIAU9K2U-r2TCkp7jv8bQnt43sy9zhwT3mg'
    
    while True:
        # Replace text sem s contentom
        content = '@everyone TENTO ANTICHEAT JE SCAM ! JE TO CISTA RATKA / GAMESENSE.PUB'

        response = send_discord_webhook(webhook_url, content)

        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(response.text)

        # 
        time.sleep(0.01)
