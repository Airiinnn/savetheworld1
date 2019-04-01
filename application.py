from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("DHS_Directory.html")


@app.route("/home")
def about():
    return render_template("home.html")


@app.route("/directions", methods=["POST"])
def directions():
    location1 = request.form.get("Current Location")
    location2 = request.form.get("Destination")
    if not location1 or not location2:
        return "Please select your current location and destination."
    elif location1 == location2:
        return "You are already at your destination..."

    elif location1 == "audi":
        if location2 == "can":
            return render_template("audi_can.html")
        elif location2 == "go":
            return render_template("audi_go.html")
        elif location2 == "hall":
            return render_template("audi_hall.html")
        elif location2 == "ish":
            return render_template("audi_ish.html")
        elif location2 == "lib":
            return render_template("audi_lib.html")
        elif location2 == "low":
            return render_template("audi_low.html")
        elif location2 == "pac":
            return render_template("audi_pac.html")
        elif location2 == "sh":
            return render_template("audi_sh.html")
        elif location2 == "tf":
            return render_template("audi_tf.html")
        elif location2 == "up":
            return render_template("audi_up.html")

    elif location1 == "can":
        if location2 == "audi":
            return render_template("can_audi.html")
        elif location2 == "go":
            return render_template("can_go.html")
        elif location2 == "hall":
            return render_template("can_hall.html")
        elif location2 == "ish":
            return render_template("can_ish.html")
        elif location2 == "lib":
            return render_template("can_lib.html")
        elif location2 == "low":
            return render_template("can_low.html")
        elif location2 == "pac":
            return render_template("can_pac.html")
        elif location2 == "sh":
            return render_template("can_sh.html")
        elif location2 == "tf":
            return render_template("can_tf.html")
        elif location2 == "up":
            return render_template("can_up.html")

    elif location1 == "go":
        if location2 == "audi":
            return render_template("go_audi.html")
        elif location2 == "can":
            return render_template("go_can.html")
        elif location2 == "hall":
            return render_template("go_hall.html")
        elif location2 == "ish":
            return render_template("go_ish.html")
        elif location2 == "lib":
            return render_template("go_lib.html")
        elif location2 == "low":
            return render_template("go_low.html")
        elif location2 == "pac":
            return render_template("go_pac.html")
        elif location2 == "sh":
            return render_template("go_sh.html")
        elif location2 == "tf":
            return render_template("go_tf.html")
        elif location2 == "up":
            return render_template("go_up.html")

    elif location1 == "hall":
        if location2 == "audi":
            return render_template("hall_audi.html")
        elif location2 == "can":
            return render_template("hall_can.html")
        elif location2 == "go":
            return render_template("hall_go.html")
        elif location2 == "ish":
            return render_template("hall_ish.html")
        elif location2 == "lib":
            return render_template("hall_lib.html")
        elif location2 == "low":
            return render_template("hall_low.html")
        elif location2 == "pac":
            return render_template("hall_pac.html")
        elif location2 == "sh":
            return render_template("hall_sh.html")
        elif location2 == "tf":
            return render_template("hall_tf.html")
        elif location2 == "up":
            return render_template("hall_up.html")

    elif location1 == "ish":
        if location2 == "audi":
            return render_template("ish_audi.html")
        elif location2 == "can":
            return render_template("ish_can.html")
        elif location2 == "go":
            return render_template("ish_go.html")
        elif location2 == "hall":
            return render_template("ish_hall.html")
        elif location2 == "lib":
            return render_template("ish_lib.html")
        elif location2 == "low":
            return render_template("ish_low.html")
        elif location2 == "pac":
            return render_template("ish_pac.html")
        elif location2 == "sh":
            return render_template("ish_sh.html")
        elif location2 == "tf":
            return render_template("ish_tf.html")
        elif location2 == "up":
            return render_template("ish_up.html")

    elif location1 == "lib":
        if location2 == "audi":
            return render_template("lib_audi.html")
        elif location2 == "can":
            return render_template("lib_can.html")
        elif location2 == "go":
            return render_template("lib_go.html")
        elif location2 == "hall":
            return render_template("lib_hall.html")
        elif location2 == "ish":
            return render_template("lib_ish.html")
        elif location2 == "low":
            return render_template("lib_low.html")
        elif location2 == "pac":
            return render_template("lib_pac.html")
        elif location2 == "sh":
            return render_template("lib_sh.html")
        elif location2 == "tf":
            return render_template("lib_tf.html")
        elif location2 == "up":
            return render_template("lib_up.html")

    elif location1 == "low":
        if location2 == "audi":
            return render_template("low_audi.html")
        elif location2 == "can":
            return render_template("low_can.html")
        elif location2 == "go":
            return render_template("low_go.html")
        elif location2 == "hall":
            return render_template("low_hall.html")
        elif location2 == "ish":
            return render_template("low_ish.html")
        elif location2 == "lib":
            return render_template("low_lib.html")
        elif location2 == "pac":
            return render_template("low_pac.html")
        elif location2 == "sh":
            return render_template("low_sh.html")
        elif location2 == "tf":
            return render_template("low_tf.html")
        elif location2 == "up":
            return render_template("low_up.html")

    elif location1 == "pac":
        if location2 == "audi":
            return render_template("pac_audi.html")
        elif location2 == "can":
            return render_template("pac_can.html")
        elif location2 == "go":
            return render_template("pac_go.html")
        elif location2 == "hall":
            return render_template("pac_hall.html")
        elif location2 == "ish":
            return render_template("pac_ish.html")
        elif location2 == "lib":
            return render_template("pac_lib.html")
        elif location2 == "low":
            return render_template("pac_low.html")
        elif location2 == "sh":
            return render_template("pac_sh.html")
        elif location2 == "tf":
            return render_template("pac_tf.html")
        elif location2 == "up":
            return render_template("pac_up.html")

    elif location1 == "sh":
        if location2 == "audi":
            return render_template("sh_audi.html")
        elif location2 == "can":
            return render_template("sh_can.html")
        elif location2 == "go":
            return render_template("sh_go.html")
        elif location2 == "hall":
            return render_template("sh_hall.html")
        elif location2 == "ish":
            return render_template("sh_ish.html")
        elif location2 == "lib":
            return render_template("sh_lib.html")
        elif location2 == "low":
            return render_template("sh_low.html")
        elif location2 == "pac":
            return render_template("sh_pac.html")
        elif location2 == "tf":
            return render_template("sh_tf.html")
        elif location2 == "up":
            return render_template("sh_up.html")

    elif location1 == "tf":
        if location2 == "audi":
            return render_template("tf_audi.html")
        elif location2 == "can":
            return render_template("tf_can.html")
        elif location2 == "go":
            return render_template("tf_go.html")
        elif location2 == "hall":
            return render_template("tf_hall.html")
        elif location2 == "ish":
            return render_template("tf_ish.html")
        elif location2 == "lib":
            return render_template("tf_lib.html")
        elif location2 == "low":
            return render_template("tf_low.html")
        elif location2 == "pac":
            return render_template("tf_pac.html")
        elif location2 == "sh":
            return render_template("tf_sh.html")
        elif location2 == "up":
            return render_template("tf_up.html")

    elif location1 == "up":
        if location2 == "audi":
            return render_template("up_audi.html")
        elif location2 == "can":
            return render_template("up_can.html")
        elif location2 == "go":
            return render_template("up_go.html")
        elif location2 == "hall":
            return render_template("up_hall.html")
        elif location2 == "ish":
            return render_template("up_ish.html")
        elif location2 == "lib":
            return render_template("up_lib.html")
        elif location2 == "low":
            return render_template("up_low.html")
        elif location2 == "pac":
            return render_template("up_pac.html")
        elif location2 == "sh":
            return render_template("up_sh.html")
        elif location2 == "tf":
            return render_template("up_tf.html")


if __name__ == "__main__":
    app.run(debug=True)