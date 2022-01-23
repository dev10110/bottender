import RPi.GPIO as GPIO
from flask import Flask, render_template, request

from bottender import BotTender


app = Flask(__name__)
bot = BotTender()



@app.route("/")
def main():
    # this is where the drinks will live
    # and s
    return render_template("main.html")


@app.route("/<motor>/<action>")
def action(motor, action):
    motor = int(motor)
    if action == "forward":
        bot.forward(motor)
    if action == "reverse":
        bot.reverse(motor)
    if action == "stop":
        bot.stop(motor)
    
    return main()




  

