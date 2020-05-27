import json
from urllib import request
from random import randint
import threading
import pygame
from pygame import mixer

# YouTube API and sub check information (API key, channel username, initial test sub count)
key = "API KEY HERE"
username = "CHANNEL NAME HERE"
test_subs = 1000

# Pygame sound initializer and song list
pygame.init()
songs = ["INSERT SONG FILES HERE"]

# Ticker and time wait information
time_wait = randint(10, 30)
ticker = threading.Event()

# Subscriber check loop
while not ticker.wait(time_wait):

    # Requests to pull channel subs from YouTube API
    channel_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + username + "&key=" + key
    channel_data = request.urlopen(channel_url).read()
    channel_subs = json.loads(channel_data)["items"][0]["statistics"]["subscriberCount"]

    # Checks if new channel subs is greater than previous check, and plays sound accordingly
    if int(channel_subs) > int(test_subs):
        if int(channel_subs) >= 100:
            song_to_play = mixer.Sound(songs[randint(0, len(songs))])
            song_to_play.play()
        else:
            sub_sound = mixer.Sound("INSERT TIER 1 SUB ALERT")
            sub_sound.play()

    # Sets the test sub amount to the new sub amount
    test_subs = channel_subs
