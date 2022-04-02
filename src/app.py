from flask import Flask, render_template, request, redirect, flash, jsonify, make_response
import time
import os

# DEBUG_MODE = TRUE


os.environ['DUMMY_MODE'] = 'TRUE'
os.environ['DUMMY_MODE'] = 'FALSE'


print(os.environ.get('DUMMY_MODE'))
from bottender import BotTender    


app = Flask(__name__)
app.secret_key = "wow so secure"
# app.config['SERVER_NAME'] = 'bot.tender:5000'
bot = BotTender()

@app.route("/gif_test")
def gif_test():
    return render_template("gif.html")



@app.route("/")
def main_page():
    get_messages(bot)
    # this is where the drinks will live
    uuid = bot.generate_uuid()
    print("NEW UUID: " + uuid)
    return render_template("main.html", bot=bot, uuid=uuid)

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




@app.route("/pour/<drink>/<uuid>")
def pour(drink, uuid):
    
    print("DRINK REQUESTED: " + drink + " with UUID: " + uuid)

    bot.enque(drink, uuid)

    return redirect("/drink_queue")

    # poured = bot.pour_parallel(drink)
    # flash("Done! I poured: " + poured)
    # return redirect("/")

@app.route("/drink_queue")
def show_drink_queue():
    return render_template("queue.html", bot=bot)

    
def get_messages(bot):
    for m in bot.messages:
        flash(m)


@app.route("/release/<uuid>")
def validated_pour(uuid):
    print("Trying to pour: " + uuid)
    # check the UUID
    if bot.get_next_drink_uuid() == uuid:
        bot.pour_parallel_next()
    else:
        print("ERRR!")
    print( "DONE! Redirecting to home!" )
    return redirect("/")
    


@app.route("/test_release", methods=["POST"])
def test_pour():


    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "message received" }), 200)

    return res
    # print("Trying to pour: " + uuid)
    # # check the UUID
    # if bot.get_next_drink_uuid() == uuid:
    #     bot.pour_parallel_next()
    # else:
    #     print("ERRR!")
    # print( "DONE! Redirecting to home!" )
    # return redirect("/")
    


@app.route("/drink_release", methods=["POST"])
def drink_release():

    req = request.get_json()

    print(req)

    bot.pour_parallel_next()

    res = make_response(jsonify({"message": "message received" }), 200)

    return res

@app.route("/honey_shot_release", methods=["POST"])
def honey_shot_release():

    req = request.get_json()

    print(req)

    
    bot.pour("honey_shot")
    print("Poured honey shot")

    res = make_response(jsonify({"message": "message received" }), 200)

    return res

@app.route("/skip/<uuid>")
def skip_drink(uuid):
     bot.deque(uuid)

     return redirect("/drink_queue")

@app.route("/custom/drive_motor", methods=["POST"])
def drive_motor():

    req = request.get_json()

    print(req)

    if req["action"] == "forward":
        bot.forward(req["motor_id"])
    if req["action"] == "reverse":
        bot.reverse(req["motor_id"])
    if req["action"] == "stop":
        bot.stop(req["motor_id"])     
    if req["action"] == "dispense":
        bot.dispense_oz(req["motor_id"], 0.5)

    res = make_response(jsonify({"message": "message received" }), 200)

    return res


@app.route("/get_motor_state")
def get_motor_state():


    states = {}
    print(bot.num_motors())
    for i in range(bot.num_motors()):
       states[i] = bot.motors[i].get_state()
    
    res = make_response(jsonify(states), 200)

    return res


