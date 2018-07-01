#!/bin/python3

from InstagramAPI import InstagramAPI
import csv

print("Started")

api = InstagramAPI("alexisgiff", "contulmeu00*")

api.login()

print("Logged in")

likerMap = {}

posts = api.getTotalSelfUserFeed()

print("Posts received")

for post in posts[:50]:
    id = post["id"]
    print(id)

    likers = []

    api.getMediaLikers(id)
    for liker in api.LastJson["users"]:
        likers.append(liker["username"])

    print(likers)

    for liker in likers:
        if liker in likerMap:
            likerMap[liker] += 1
        else:
            likerMap[liker] = 1

print("Reading done, writing now")

print(likerMap)

w = csv.writer(open("outputAlexis.csv", "w"))
for key, val in likerMap.items():
    w.writerow([key, val])

print("Written")
