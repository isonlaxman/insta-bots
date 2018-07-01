#!/bin/python3

from InstagramAPI import InstagramAPI
import csv

api = InstagramAPI("alexisgiff", "contulmeu00*")

api.login()

print("Logged in")

reader = csv.reader(open('outputAlexis.csv', 'r'))
likerMap = {}
for row in reader:
    if row:
        print(row)
        likerMap[row[0]] = row[1]

print(likerMap)

api.getSelfUserFollowers()
followers = []
strange = []

for follower in api.LastJson["users"]:
    if follower["username"] not in likerMap:
        strange.append(follower["username"])

print(strange)

w = csv.writer(open("strangeAlexis.csv", "w"))
for follower in strange:
    w.writerow([follower])