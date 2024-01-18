import requests
import sys
import json
import pandas as pd

# Init vars and load vars with file content
url = f"https://vwc.cinesa.es/WSVistaWebClient/ocapi/v1/showtimes/by-business-date/{sys.argv[2]}"
cines_ids = {}
headers = {}
films = []
shotime = []
with open("cines.json", "r") as f:
    cines_ids = json.load(f)
with open("headers.json", "r") as f:
    headers = json.load(f)
querystring = {"siteIds":cines_ids[sys.argv[1]]}


# make the request
response = requests.request("GET", url, headers=headers, params=querystring)
#convert the response content in bytes to json
response = response.content.decode('utf-8')
response = json.loads(response)

# loop throught films
films_len = len(response["relatedData"]["films"])
for f in range(0,films_len):
    films.append(
        {
            "id":f"{response['relatedData']['films'][f]['id']}",
            "Movie":f"{response['relatedData']['films'][f]['title']['text'].strip()}",
            "Duration":"{}:{}:00".format(*divmod(response['relatedData']['films'][f]['runtimeInMinutes'],60)) #"{response['relatedData']['films'][f]['runtimeInMinutes']}" 
        }
    )

shotime_len = len(response["showtimes"])
for s in range(0,shotime_len):
    shotime.append(
        {
            "id":f"{response['showtimes'][s]['filmId']}",
            "Session":f"{response['showtimes'][s]['schedule']['startsAt'].split('T')[1].split('+')[0]}",
        }
    )

df = pd.json_normalize(films)
df2 = pd.json_normalize(shotime)
df = df.merge(df2, on="id")
df = df.drop(columns=["id"])
df.to_csv(f"{sys.argv[1]}_{sys.argv[2]}.csv", index=False)