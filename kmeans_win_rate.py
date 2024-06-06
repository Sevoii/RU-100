import json
import csv
from collections import defaultdict

# blacklist = ["SL", "AB"]
#
# with open("data/bootstrap_ci.json") as f:
#     data = json.load(f)
#
# with open("data/bootstrap_ci.csv", "w", newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(["Character", "Median_Win_Rate"])
#
#     for i in data:
#         if i not in blacklist:
#             writer.writerow([i, data[i][1]])

# input("Press Enter After Running `kmeans_win_rate.r`")

groups = defaultdict(lambda: list((list(), 0)))

with open("data/kmeans_win_rate.csv") as f:
    reader = csv.reader(f)
    next(reader)  # Ignore first row
    for row in reader:
        groups[row[2]][0].append(row[0])
        groups[row[2]][1] = row[1]

print(sorted(list(groups.values()), key=lambda x: x[1], reverse=True))
