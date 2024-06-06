import json
import os

with open("data/t100.json") as f:
    data = json.load(f)

t100 = {f"{j}_{i}" for i in data for j in data[i]}

for i in os.listdir("data/matches"):
    with open(f"data/matches/{i}") as f:
        matches = json.load(f)

    cleaned = [i for i in matches if f"{i[0]}_{i[1]}" in t100]

    with open(f"data/matches_cleaned/{i}", "w") as f:
        json.dump(cleaned, f)

