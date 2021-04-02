# Watanuki
A discord prank bot for april's first. It will change the name of all users in discord each x minutes using a list.

Uses python 3.5+, asyncpg, pendulum and discord.py 1.6.0

You need to set a CONFIG.PY file in the root folder with the following fields:

```py
PREFIX = ""  # The prefix you wanna use
TOKEN = ""  # Your bot token

#Increment example
TIME_INCREMENT_IN_MINUTES = 10   #Increment that will be added for the next update calculation

#PostgreSQL config production
USERNAME = ''
PASSWORD = ''
DATABASE = ''
HOST = ''
```

# Why Watanuki?
In xxxHolic, Watanuki was born in April's first, and there is a running joke about it. [Video in portuguese]

[![Watanuki primeiro de abril](https://img.youtube.com/vi/5lU1tHM6n0A/0.jpg)](https://www.youtube.com/watch?v=5lU1tHM6n0A)
