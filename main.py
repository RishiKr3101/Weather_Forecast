from flask import Flask, render_template, redirect, url_for, request
import weather_forecast as wf

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
	    user = request.form["nm"]
	    return redirect(url_for("user", usr=user))
    else:
	    return render_template("home.html")


@app.route("/<usr>")
def user(usr):
    return render_template("results.html", content=usr)


if __name__ == "__main__":
    app.run(debug=True)

