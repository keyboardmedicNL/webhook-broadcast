# what is it
Webhook-broadcast is a simple tool that allows you to broadcast a message to multiple webhooks to for example inform users of your server your rebooting your server.

# how to use it
- take the example config from the config folder and copy it, rename the copy to ```config.json```
- fill in the config as needed with your details:
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