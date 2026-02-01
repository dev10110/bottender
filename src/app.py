import os
import time

from flask import (Flask, flash, jsonify, make_response, redirect,
                   render_template, request)

# DEBUG_MODE = TRUE

# os.environ['DUMMY_MODE'] = 'TRUE'
# os.environ['DUMMY_MODE'] = 'FALSE'


print(os.environ.get("DUMMY_MODE"))
from bottender import BotTender

app = Flask(__name__)
app.secret_key = "wow so secure"
# app.config['SERVER_NAME'] = 'bot.tender:5000'
bot = BotTender()


@app.route("/gif_test")
def gif_test():
    return render_template("gif.html")


@app.route("/hover_test")
def hover_test():
    return render_template("hover.html")


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
        bot.dispense_oz(motor, 1.0)

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


@app.route("/staged/<uuid>")
def staged_start(uuid):
    # redirect to stage 0
    if bot.get_next_drink_uuid() != uuid:
        return redirect("/")
    return redirect(f"/staged/{uuid}/0")


@app.route("/staged/<uuid>/<int:stage_id>")
def staged_page(uuid, stage_id):
    # render a stage for the next queued drink
    if bot.get_next_drink_uuid() != uuid:
        return redirect("/")

    drink_id = bot.drink_queue[0][0]
    d = bot.find_drink(drink_id)
    if not d:
        return redirect("/")

    stages = d.stages

    if stage_id < 0 or stage_id >= len(stages):
        return redirect("/")

    s = stages[stage_id]
    return render_template(
        "staged.html", bot=bot, drink=d, stage_index=stage_id, stage=s, uuid=uuid
    )


@app.route("/pour_stage/<uuid>/<int:stage_id>", methods=["POST"])
def pour_stage(uuid, stage_id):

    print(f"Pouring stage {stage_id} for drink with UUID {uuid}")

    # ensure this is the next queued drink
    if bot.get_next_drink_uuid() != uuid:
        return redirect("/drink_queue")

    drink_id = bot.drink_queue[0][0]
    d = bot.find_drink(drink_id)
    print("Found drink: ", d.name)
    stages = getattr(d, "stages", None)

    # perform the stage pour (BLOCKING)!!
    bot.pour_stage(drink_id, stage_id)

    print(f"Done pouring stage {stage_id}, redirecting...")

    # if last stage, dequeue and go home
    if stage_id >= len(stages) - 1:
        bot.deque(uuid)
        print("Done with all stages, going home")
        return redirect("/")
    # otherwise go to next stage
    print(f"Going to next stage: {stage_id+1}")
    return redirect(f"/staged/{uuid}/{stage_id+1}")


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
    print("DONE! Redirecting to home!")
    return redirect("/")


@app.route("/test_release", methods=["POST"])
def test_pour():

    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "message received"}), 200)

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

    res = make_response(jsonify({"message": "message received"}), 200)

    return res


@app.route("/honey_shot_release", methods=["POST"])
def honey_shot_release():

    req = request.get_json()

    print(req)

    bot.pour("honey_shot")
    print("Poured honey shot")

    res = make_response(jsonify({"message": "message received"}), 200)

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
        bot.dispense(req["motor_id"], 1000) # ms

    res = make_response(jsonify({"message": "message received"}), 200)

    return res


@app.route("/get_motor_state")
def get_motor_state():

    states = {}
    print(bot.num_motors())
    for i in range(bot.num_motors()):
        states[i] = bot.motors[i].get_state()

    res = make_response(jsonify(states), 200)

    return res
