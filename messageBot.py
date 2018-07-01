#!/bin/python3
import time
import random

from InstagramAPI import InstagramAPI
import csv

# Init the API
api = InstagramAPI("inoslaxman", "Nois1199@Insta")
api.login()

# Function to message a list of people
# I/P: The list of people to message

def message (people):
    