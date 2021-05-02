import weatherfrcst as wf

location = "jamshedpur Jharkhand"


d=wf.forecast(place = location)


print(d)





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
       'narrative': 'Partly cloudy. Hazy. Low 26ºC. Winds SSW and variable.'}}'''