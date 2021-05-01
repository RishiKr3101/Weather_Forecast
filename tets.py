import weatherfrcst as wf

location = "jamshedpur Jharkhand"



d=wf.forecast(place = location)

print(d['place'])





'''{'date': '2021-05-01',
 'day': {'humidity': None,
         'narrative': None,
         'phrases': None,
         'precipitate': None,
         'temperature': None,
         'uv_description': None,
         'wind_speed': None},
 'night': {'humidity': 68,
           'narrative': 'Generally clear. Hazy. Low 25ºC. Winds SSE at 10 to '
                        '15 km/h.',
           'phrases': 'Mostly Clear',
           'precipitate': 3,
           'temperature': 25,
           'uv_description': 'Low',
           'wind_speed': 10},
 'place': 'jamshedpur Jharkhand',
 'time': '19:29:42'}
None'''