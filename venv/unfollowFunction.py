#!/bin/python3
import time

from InstagramAPI import InstagramAPI
import csv


def get_to_unfollow():
    reader = csv.reader(open('unfollow.csv', 'r'))
    to_unfollow = []
    for row in reader:
        if row:
            to_unfollow.append(row[0])
    return to_unfollow


def get_non_followers():
    reader = csv.reader(open('nonFollowers.csv', 'r'))
    non_followers = {}
    for row in reader:
        if row:
            non_followers[row[0]] = row[1]
    return non_followers


def main():
    api = InstagramAPI("inoslaxman", "Nois1199@Insta")
    api.login()

    print("Logged in")

    to_unfollow = get_to_unfollow()
    non_followers = get_non_followers()

    print("Received the lists")
    print("To unfollow: " + str(len(to_unfollow)))
    print("Non: " + str(len(non_followers)))
    print("Starting to unfollow")

    for user in to_unfollow:
        api.unfollow(non_followers[user])
        if api.LastJson.get("friendship_status") is None:
            time.sleep(120)
            api.unfollow(non_followers[user])
            
        print("Unfollowed " + user)

    print("Done")

if __name__ == '__main__':
    main()
