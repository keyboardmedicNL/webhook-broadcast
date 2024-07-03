# what is it
Webhook-broadcast is a simple tool that allows you to broadcast a message to multiple webhooks to for example inform users of your server your rebooting your server.

# how to use it
- take the example config from the config folder and copy it, rename the copy to ```config.json```
- fill in the config as needed with your details:
```
{
  "debug":"true or false(makes the script extra verbose for troubleshooting)",
    "discord_webhooks":[
      {
          "name":"discord_webhook",
          "url":"https://yourdiscordwebhookurl.com",
          "title":"title",
          "color":"1523940",
          "pingid":""
      }
    ],
    "telegram_webhooks":[
      {
          "name":"telegram_webhook",
          "token":"yourtoken",
          "chat_id":"yourchatid"
      }
    ],
    "gotify_webhooks":[
      {
          "name":"gotify_webhook",
          "url":"https://yourgotifyurl",
          "token":"yourgotifyapptoken",
          "title":"title",
          "priority":"0"
      }
    ]
  }
  ```
  - if you want to not use a group just delete the objects within the list, for example the user below does not use telegram
  ```
  {
    "discord_webhooks":[
      {
          "name":"discord_webhook",
          "url":"https://yourdiscordwebhookurl.com",
          "title":"title",
          "color":"1523940",
          "pingid":""
      }
    ],
    "telegram_webhooks":[
    ],
    "gotify_webhooks":[
      {
          "name":"gotify_webhook",
          "url":"https://yourgotifyurl",
          "token":"yourgotifyapptoken",
          "title":"title",
          "priority":"0"
      }
    ]
  }
  ```
  - run the application and input the message to broadcast, hit enter to send
  - you can press ctrl+C at any time to stop the script
  - additionally if your on linux you can create a quick alias by editing ```~/.bashrc``` and by adding the following line at the bottom of the file ``` alias your_alias_name="cd /path/to/your/script && /usr/bin/python broadcast.py && cd -" ``` followed by ```source ~/.bashrc``` to reload your enviroment and activate the alias