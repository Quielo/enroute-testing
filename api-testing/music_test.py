"""
Run command:
    $ pytest ./api-testing/music_test.py -v
"""

import values as v
import requests
import json
import os


def test_top10():

    response10 = requests.get(f"{v.url}{v.top10Art}&apikey={v.Key}")

    assert (response10.status_code == 200)


def test_infoTop3():

    response3 = requests.get(f"{v.url}{v.top3Art}&apikey={v.Key}")

    assert (response3.status_code == 200)


def test_albumLast5():

    responseAlbums5 = None

    response10 = requests.get(f"{v.url}{v.top10Art}&apikey={v.Key}")

    dataArtists = json.loads(response10.content.decode('utf8'))
    artists = dataArtists['message']['body']['artist_list']
    lastones = artists[5::]

    for last in lastones:
        responseAlbums5 = requests.get(f"{v.url}{v.albums}&apikey={v.Key}")
        print(last)

    assert (response10.status_code == 200 and responseAlbums5.status_code == 200)
