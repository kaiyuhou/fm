# coding: utf-8
"""
create: Mike at 2016-9-25
version: 0.1
ref:    https://www.zhihu.com/question/25697796
        https://github.com/flavedogame/doubanfm-py

Abstract: I want to create a Python project to Play Douban FM
Challenge: UI
            Connected to Douban
            How to play a music in Python
"""
import mp3play
import urllib
import time
from doubanFMApi import doubanFMApi


class UI():
    def __init__(self):
        print "UI init"

        self.setup_ui()

    def setup_ui(self):
        isLogin = True
        #isLogin = False
        api = doubanFMApi()
        api.set_auth_access_token('Bearer e3fd1f060a602cacabf75d121f208604')

        while not isLogin:
            email = raw_input('豆瓣账户 (Email地址): ')
            password = raw_input('豆瓣密码: ')
            isLogin = api.login(email, password)

        songs = api.get_red_heart_songs()
        print songs[1].title
        print songs[1].url

        urllib.urlretrieve(songs[1].url, 'a.mp3')

        music = mp3play.load('a.mp3')
        music.play()

    def run(self):
        print "Run"


if __name__ == '__main__':
    #UI().run()
    music = mp3play.load('a.mp3')
    music.play()
    time.sleep(min(5, music.seconds()))
