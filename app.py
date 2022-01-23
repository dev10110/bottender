import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect

from bottender import BotTender


app = Flask(__name__)
bot = BotTender()



@app.route("/")
def main_page():
    # this is where the drinks will live
    # and s
    return render_template("main.html")

@app.route("/custom")
def custom_page():
    # this is for custom drinks
    return render_template("custom.html")


@app.route("/setup", methods=["GET", "POST"])
def setup_page():
    if request.method == "POST":
        req = request.form
        print(req)

        
        drinks = []
 
        drinks.append(req["drink1"])
        drinks.append(req["drink2"])
        drinks.append(req["drink3"])
        drinks.append(req["drink4"])        
        bot.set_drinks(drinks)
 
        return redirect(request.url)
    
    return render_template("setup.html", bot=bot)






@app.route("/<motor>/<action>")
def action(motor, action):
    motor = int(motor)
    if action == "forward":
        bot.forward(motor)
    if action == "reverse":
        bot.reverse(motor)
    if action == "stop":
        bot.stop(motor)
    
    return custom_page()




  

