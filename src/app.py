from flask import Flask, render_template, request, redirect, flash
import time

from bottender import BotTender


app = Flask(__name__)
app.secret_key = "wow so secure"
# app.config['SERVER_NAME'] = 'bot.tender:5000'
bot = BotTender()



@app.route("/")
def main_page():
    get_messages(bot)
    # this is where the drinks will live
    return render_template("main.html", bot=bot)

@app.route("/custom")
def custom_page():
    get_messages(bot)
    # this is for custom drinks
    return render_template("custom.html", bot=bot)


@app.route("/setup", methods=["GET", "POST"])
def setup_page():
    get_messages(bot)
    if request.method == "POST":
        req = request.form
        print(req)

        drinks = []

        for i in range(bot.num_motors()):
            drinks.append(req[f"drink{i}"])

        ret = bot.set_drinks(drinks)

        if ret == True:
            flash("Saved!")
        else:
            flash("ERROR Saving!")

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
    if action == "dispense":
        bot.dispense_oz(motor, 0.5)

        
    # time.sleep(0.1)    
    return redirect("/custom")




@app.route("/pour/<drink>")
def pour(drink):
    
    print("DRINK REQUESTED: " + drink)
    poured = bot.pour_parallel(drink)
    flash("Done! I poured: " + poured)
    return redirect("/")
    
def get_messages(bot):
    for m in bot.messages:
        flash(m)

