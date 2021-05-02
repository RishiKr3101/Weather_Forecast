from flask import Flask, render_template, redirect, url_for
import weatherfrcst as wf


def weather(usr):

    d=wf.forecast(place = usr)
    c="Network Error"
    try:
        place= d['place']
        time = d['time']
        date = d['date']
        d_temp , d_prep, d_uv, d_ws, d_humid, d_phrase, d_summary = d['day']['temperature'],d['day']['precipitate'],d['day']['uv_description'],d['day']['wind_speed'],d['day']['humidity'],d['day']['phrases'],d['day']['narrative'],

        n_temp , n_prep, n_uv, n_ws, n_humid, n_phrase, n_summary = d['night']['temperature'],d['night']['precipitate'],d['night']['uv_description'],d['night']['wind_speed'],d['night']['humidity'],d['night']['phrases'],d['night']['narrative']

        return time, date, d_temp , d_prep, d_uv, d_ws, d_humid, d_phrase, d_summary, n_temp , n_prep, n_uv, n_ws, n_humid, n_phrase, n_summary
    
    except:
        return c, c, c , c, c, c, c, c, c, c , c, c, c, c, c, c





app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def search():
    if request.method == "POST":
	    user = request.form["address"]
	    return redirect(url_for("user", usr=user))
    else:
	    return render_template("home.html")


@app.route("/<usr>")
def user(usr):
    time, date, d_temp , d_prep, d_uv, d_ws, d_humid, d_phrase, d_summary, n_temp , n_prep, n_uv, n_ws, n_humid, n_phrase,n_summary =weather(usr)
    
    return render_template("results.html", content=usr, time = time, date= date, d_temp= d_temp , d_prep= d_prep, d_uv= d_uv, d_ws= d_ws, d_humid= d_humid, d_phrase= d_phrase, d_summary= d_summary, n_temp= n_temp , n_prep= n_prep, n_uv= n_uv, n_ws= n_ws, n_humid= n_humid, n_phrase= n_phrase, n_summary= n_summary)
    
    








if __name__ == "__main__":
    app.run(debug=True)

