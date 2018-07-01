#!/bin/python3
import time

from InstagramAPI import InstagramAPI
import csv

api = InstagramAPI("inoslaxman", "Nois1199@Insta*")

api.login()

print("Logged in")

reader = csv.reader(open('nonFollowers.csv', 'r'))
nonFollower = []
for row in reader:
    if row:
        nonFollower.append((row[0], row[1]))

print("Read data")
print(nonFollower)

unfollow = []

for user in nonFollower:
    api.getUsernameInfo(user[1])
    print(api.LastJson)

    if api.LastJson.get("user") is None:
        time.sleep(120)
    else:
        if api.LastJson["user"]["follower_count"] < 5000:
            unfollow.append(user[0])

print(unfollow)

w = csv.writer(open("unfollow.csv", "w"))
for user in unfollow:
    w.writerow([user])

