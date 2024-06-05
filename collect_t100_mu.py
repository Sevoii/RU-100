import requests
from bs4 import BeautifulSoup
import json
import re
import os

with open("data/t100.json") as f:
    t100_data = json.load(f)


def get_recent_matches(player_id, char_id):
    urls = ["http://ratingupdate.info/", "https://puddle.farm/"]

    matches = []

    for u in urls:
        full_url = f"{u}/player/{player_id}/{char_id}/history?offset="

        offset = 0
        flag = True
        while flag:
            flag = False

            resp = requests.get(full_url + str(offset * 100))
            soup = BeautifulSoup(resp.text, "html.parser")

            if not soup.find("table"):
                break

            for i in soup.find("table").children:
                if "opponent_column" in str(i):
                    flag = True
                    match = re.findall(r"href=\"/player/(.+?)/(..)\"", str(i))

                    if match:
                        matches.append(
                            (match[0][0], match[0][1], tuple(int(i) for i in list(i.children)[15].text.split("-"))))

            offset += 1

    return matches


collected = [i[:-5] for i in os.listdir("data/matches")]
blacklist = []
whitelist = []

for i in t100_data:
    if i in collected or i in blacklist or (whitelist and i not in whitelist):
        continue

    all_matches = []

    for j, k in enumerate(t100_data[i]):
        print(j, k, i)

        all_matches += get_recent_matches(k, i)

    with open(f"data/matches/{i}.json", "w") as f:
        json.dump(all_matches, f)
