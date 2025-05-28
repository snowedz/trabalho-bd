import pandas as pd
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

df = pd.read_csv('twitchdata-update.csv')

for _, row in df.iterrows():
    channel = row['Channel'].lower()

    r.zadd("tempo assistido", {channel: row['Watch time(Minutes)']})
    r.zadd("seguidores", {channel: row['Followers']})

