import requests
import json

# functions used in script:

def send_telegram(telegram_token,telegram_chat_id,telegram_message):
    telegram_request = requests.post(
        url=f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}&parse_mode=html&text={telegram_message}').json()
    return(telegram_request)

def send_discord(discord_url,discord_title,discord_color,discord_description,discord_ping):
    discord_request = requests.post(discord_url, json={
    "content": discord_ping, "embeds": [
        {
            "title": discord_title,
            "color": discord_color,
            "description": discord_description,
        }]}, params={'wait': 'true'})
    return(discord_request)

def send_gotify(gotify_url,gotify_token,gotify_title,gotify_message,gotify_priority):
    gotify_request = requests.post(f'{gotify_url}/message?token={gotify_token}', json={
        "title": gotify_title,
        "message": gotify_message,
        "priority": gotify_priority
    })
    return(gotify_request)

# load config
with open("config/config.json") as config:
    configJson = json.load(config)
    discord_webhooks = configJson["discord_webhooks"]
    telegram_webhooks = configJson["telegram_webhooks"]
    gotify_webhooks = configJson["gotify_webhooks"]
print("succesfully loaded config")

# main

message_input = input("\nwrite the message to broadcast and hit enter...\n")

# discord webhooks
print("starting sending to discord webhooks")
for discord_hook in discord_webhooks:
    name = discord_hook["name"]
    url = discord_hook["url"]
    title = discord_hook["title"]
    color = int(discord_hook["color"])
    discord_ping = discord_hook["pingid"]
    print(f"sending message to discord webhook: {name}")
    response = send_discord(url,title,color,message_input,discord_ping)
    print(f"webhook response is {str(response)}")
print("finished sending to discord webhooks\n")

# telegram webhooks
print("starting sending to telegram webhooks")
for telegram_hook in telegram_webhooks:
    name = telegram_hook["name"]
    token = telegram_hook["token"]
    chatid = telegram_hook["chat_id"]
    print(f"sending message to telegram webhook: {name}")
    response = send_telegram(token,chatid,message_input)
    print(f"webhook response is {str(response)}")
print("finished sending to telegram webhooks\n")

# gotify webhooks
print("starting sending to gotify webhooks")
for gotify_hook in gotify_webhooks:
    name = gotify_hook["name"]
    url = gotify_hook["url"]
    token = gotify_hook["token"]
    title = gotify_hook["title"]
    priority = int(gotify_hook["priority"])
    print(f"sending message to gotify webhook: {name}")
    response = send_gotify(url,token,title,message_input,priority)
    print(f"webhook response is {str(response)}")
print("finished sending to gotify webhooks\n")