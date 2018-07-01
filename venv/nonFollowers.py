#!/bin/python3

from InstagramAPI import InstagramAPI
import csv

api = InstagramAPI("inoslaxman", "Nois1199@Insta*")

api.login()

print("Logged in")

api.getSelfUsersFollowing()
following = []

for user in api.LastJson["users"]:
    following.append((user["username"], user["pk"]))

api.getUserFollowers(api.username_id)

followers = []

for user in api.LastJson["users"]:
    followers.append(user["username"])

print(api.LastJson.keys())
print(api.LastJson["next_max_id"])
max_id = api.LastJson["next_max_id"]

for i in range(8):

    api.getUserFollowers(api.username_id, max_id)
    for user in api.LastJson["users"]:
        followers.append(user["username"])

    print(len(followers))
    max_id = api.LastJson["next_max_id"]

api.getUserFollowers(api.username_id, max_id)
for user in api.LastJson["users"]:
    followers.append(user["username"])

print(len(followers))

w = csv.writer(open("following.csv", "w"))
for user in following:
    w.writerow([user])

w = csv.writer(open("followers.csv", "w"))
for user in followers:
    w.writerow([user])

nonFollowers = []

for user in following:
    if user[0] not in followers:
        nonFollowers.append(user)

w = csv.writer(open("nonFollowers.csv", "w"))
for user in nonFollowers:
    w.writerow([user[0], user[1]])
