#!/bin/python3
import time
import random

from InstagramAPI import InstagramAPI
import csv

# The list of comments
possible_comments = [
    "Ommggg this is so good! <3",
    "I like this so much <3 <3",
    "This is so cute <3 <3"
]

photography_comments = [
    "Just found your profile, this is so good!",
    "Dude this is great! Just cam across your profile and I love it",
    "You're so good at photography! I love this post"
]

# Init the API
api = InstagramAPI("inoslaxman", "Nois1199@Insta")
api.login()


# Function to get posts by tags
# I/P : List of tags
# O/P : Posts from the tags
def get_posts_by_tags(tags):
    media_list = []
    how_many = 4

    print("Retreiving posts...")
    for tag in tags:
        api.tagFeed(tag)
        media_list += api.LastJson['ranked_items'][:int(how_many / len(tags))]
        time.sleep(50)

    print("Posts retreived!\n")
    return media_list


# Function to like a list of posts
# I/P : List of posts
def like_posts(media_list):
    print("Liking posts...")
    for media in media_list:
        api.like(media['id'])
        time.sleep(7)

    print("Posts liked\n")


# Function to comment on posts
# I/P : List of posts
def comment_posts(media_list):
    print("Commenting on posts...")
    for media in media_list:
        api.comment(media['id'], random.choice(possible_comments))
        time.sleep(15)

    print("Commenting done\n")


# Function to get username_id from posts
# I/P : List of posts
# O/P : List of username_ids
def get_media_creators(media_list):
    print("Fetching users...")
    user_list = []
    for media in media_list:
        username_id = media['user']['pk']
        user_list.append(username_id)

    print("Users fetched\n")
    return user_list


# Function to follow a list of users
# I/P : List of username_ids
def follow_people(user_list):
    print("Following people...")
    for user in user_list:
        api.follow(user)
        time.sleep(15)

    print("Following done, people followed: " + str(len(user_list)) + "\n")


# The main function
def main():
    posts = get_posts_by_tags(["photography"])
    like_posts(posts)
    comment_posts(posts)
    users = get_media_creators(posts)
    follow_people(users)


if __name__ == '__main__':
    main()
