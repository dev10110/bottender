# BotTender [mk1]

A relatively simple bartending bot, made using a raspi and a few peristaltic pumps. 

The idea is that my friends would be able to connect to the raspi using their phones, and order drinks that get served!

To make my life easier, I just used an LM298N motor driver module to drive tthe pumps. The pumps operate at 12V, from a dc switching power supply. 

The `src` folder contains the flask app that I created to be able to remotely control the bot. 

## Adding more recipes
Just modify `recipes.py`

## Testing Env
Raspi3B+
Python 3.9.2
Flask 2.0.2
Werkzeug 2.0.2

check the pin mappings are correct (defined in the constructor for bottender.py)

## Running Flask 
(optional)
`export FLASK_ENV=development`

`flask run --host=0.0.0.0`

## running it without ip address
in `/etc/hosts`
add 
```
127.0.0.1 bot.tender localhost
```
which will redirect any requests (from the current computer) from bot.tender to localhost

then launch flask with port 80:
```
flask run --host=0.0.0.0 --port=80
```

and now navigate to `bot.tender/`
