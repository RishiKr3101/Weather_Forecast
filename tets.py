import weatherfrcst as wf





time, date, d_temp , d_prep, d_uv, d_ws, d_humid, d_phrase, d_summary, n_temp , n_prep, n_uv, n_ws, n_humid, n_phrase, n_summary=weather('jamshedpur jharkhand')


@app.route("/<usr>")
def user(usr):
    time, date, d_temp , d_prep, d_uv, d_ws, d_humid, d_phrase, d_summary, n_temp , n_prep, n_uv, n_ws, n_humid, n_phrase, n_summary=weather(usr)
    
    return render_template("results.html", content=usr, time = time, date= date, d_temp= d_temp , d_prep= d_prep, d_uv= d_uv, d_ws= d_ws, d_humid= d_humid, d_phrase= d_phrase, d_summary= d_summary, n_temp= n_temp , n_prep= n_prep, n_uv= n_uv, n_ws= n_ws, n_humid= n_humid, n_phrase= n_phrase, n_summary= n_summary)

'''{'place': 'jamshedpur Jharkhand', 
'time': '13:45:26', 
'date': '2021-05-02',
 'day': {'temperature': 38,
  'precipitate': 15,
   'uv_description': 'Very High',
    'wind_speed': 8,
     'humidity': 35,
      'phrases': 'Partly Cloudy',
       'narrative': 'Partly cloudy. Hazy. High 38ºC. Winds SSE and variable.'}, 
 'night': {'temperature': 26,
  'precipitate': 5,
   'uv_description': 'Low',
    'wind_speed': 7,
     'humidity': 61,
      'phrases': 'Partly Cloudy',
       'narrative': 'Partly cloudy. Hazy. Low 26ºC. Winds SSW and variable.'}}
       
       
       
       <div id="result">

        <h2>Time : {{time}}</h2>
        <h2>Date : {{date}}</h2>
        <br>
        <br>
        <h2>Day</h2>
        <br>
        <p>Temperature : {{d_temp}}</p>
        <p>Precipitation : {{d_prep}}</p>
        <p>UV description : {{d_uv}}</p>
        <p>Wind Speed : {{d_ws}}</p>
        <p>Humidity : {{d_humid}}</p>
        <p>Phrases : {{d_phrase}}</p>
        <p>Summary : {{d_summary}}</p>
        <br>
        <br>
        <h2>Night</h2>
        <br>
        <p>Temperature : {{n_temp}}</p>
        <p>Precipitation : {{n_prep}}</p>
        <p>UV description : {{n_uv}}</p>
        <p>Wind Speed : {{n_ws}}</p>
        <p>Humidity : {{n_humid}}</p>
        <p>Phrases : {{n_phrase}}</p>
        <p>Summary : {{n_summary}}</p>


    </div>
       '''