#!/bin/python3

from InstagramAPI import InstagramAPI
import csv

api = InstagramAPI("inoslaxman", "Nois1199@Insta*")

api.login()

print("Logged in")

api.tagFeed("photography")
print(api.LastJson)

post = api.LastJson['ranked_items'][0]
api.like(post['id'])

print(len(api.LastJson))