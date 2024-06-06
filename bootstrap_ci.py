import os

import numpy as np
import random
import json

random.seed(1234)

BOOTSTRAP_SAMPLES = 2000


def find_bootstrap_ci(char):
    with open(f"data/matches_cleaned/{char}.json") as f:
        data = json.load(f)

    # these are random *enough* but it'd be good to actually control for opponent
    wins = 0
    losses = 0

    for i in data:
        # Excluding the char itself
        if i[1] != char:
            wins += i[2][0]
            losses += i[2][1]

    total = wins + losses

    samples = []
    for _ in range(BOOTSTRAP_SAMPLES):
        bootstrap_sample = random.choices([1, 0], [wins, losses], k=total)
        samples.append(sum(bootstrap_sample) / total)

    return list(np.percentile(samples, [2.5, 50, 97.5]))


bootstrap_ci = {}

for i in os.listdir("data/matches_cleaned"):
    char = i[0:2]
    bootstrap_ci[char] = find_bootstrap_ci(char)

    print(char, bootstrap_ci[char])

with open("data/bootstrap_ci.json", "w") as f:
    json.dump(bootstrap_ci, f)
