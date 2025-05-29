import pandas as pd
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

df = pd.read_csv('twitchdata-update.csv')

# CREATE
def create():
    for _, row in df.iterrows():
        channel = row['Channel'].lower()

        r.zadd("tempo assistido", {channel: row['Watch time(Minutes)']})
        r.zadd("seguidores", {channel: row['Followers']})


# READ
def read():
    top_assistidos = r.zrevrange("tempo assistido", 0, 9, withscores=True)
    for rank, (channel, score) in enumerate(top_assistidos, 1):
        print(f"{rank}. {channel.decode()} - {int(score)} minutos")

    top_seguidores = r.zrevrange("seguidores", 0, 9, withscores=True)
    for rank, (channel, score) in enumerate(top_seguidores, 1):
        print(f"{rank}. {channel.decode()} - {int(score)} seguidores")

    canal = 'ninja'
    rank = r.zrevrank("seguidores", canal)
    if rank is not None:
        print(f"{canal} está em {rank + 1}º lugar em seguidores.")
    else:
        print("Canal não encontrado.")

# UPDATE
def update():
    r.zincrby("tempo assistido", 5000, "ninja")

# DELETE
def delete():
    r.zrem("tempo assistido", "ninja")
    r.zrem("seguidores", "ninja")

