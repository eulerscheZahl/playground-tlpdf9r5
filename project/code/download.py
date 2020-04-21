import json
import requests

game_id = 453253378
r = requests.post('https://www.codingame.com/services/gameResultRemoteService/findByGameId', json = [str(453253378), None])
replay = r.json()
print(replay)
