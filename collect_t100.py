import requests
from bs4 import BeautifulSoup
import re
import json

chars = ["SO", "KY", "MA", "AX", "CH", "PO", "FA", "MI", "ZA", "RA", "LE", "NA", "GI", "AN", "IN", "GO", "JC", "HA",
         "BA", "TE", "BI", "SI", "BE", "AS", "JN", "EL"]

base_url = "http://ratingupdate.info/top/"

chars_hotfix = ["AB", "SL"]

base_url_hotfix = "https://puddle.farm/top/"


def get_t100(char):
    url = [base_url, base_url_hotfix][char not in chars]
    resp = requests.get(url + char)
    soup = BeautifulSoup(resp.text, "html.parser")

    player_ids = []

    for i in soup.find("table").children:
        html = str(i)
        if "href" in html and (match := re.findall(r"href=\"/player/(.+?)/..\"", html)):
            player_ids += match

    return player_ids


data = {i: get_t100(i) for i in (chars + chars_hotfix)}
with open("data/t100.json", "w") as f:
    json.dump(data, f)
