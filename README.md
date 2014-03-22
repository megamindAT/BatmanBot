## Python bot for IRC
Batmanbot s a simple IRCbot wrote by Python. It can be used to log channel chat, to talk or to calculate maths problem.

## Installation
* First create the db 
```bash
sqlite3 db/irclog.db << db/initdb.sql
```
* Create config file ```config.py``` in top level directory
```python
SERVER = ["irc.freenode.org"]
CHANNEL = "#YOUR_CHANNEL_NAME"
PASSWORD = "YOUR_CHANNEL_PASS"
NICKNAME = ["BatmanBot"]
MAIN_SERVER = "irc.freenode.org"
```

* Run the bot
```bash
python BatmanBot.py
```
