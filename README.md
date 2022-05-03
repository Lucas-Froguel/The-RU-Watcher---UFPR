# The-RU-Watcher---UFPR
This project does a webscraping of the daily menu at the RU of UFPR and sends to a group on Telegram.

If you want to use it, you will need to create your own Telegram bot and set up its key (as well as the group id) in the `.env` file following the `.env.template`.

I have setup a cronjob to run the code every weekday at 10am. In order to do that, type `crontab -e` and add the following:
```
0 10 * * 1-5 python path_to_code/src/main.py
```
