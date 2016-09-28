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
from doubanFMApi import doubanFMApi

class UI():
    def __init__(self):
        print "UI init"

        self.setup_ui()

    def setup_ui(self):
        isLogin = True
        #isLogin = False
        api = doubanFMApi()
        api.set_auth_access_token('Bearer c34a7677932b563a49df6366b98202ae')

        while not isLogin:
            email = raw_input('豆瓣账户 (Email地址): ')
            password = raw_input('豆瓣密码: ')
            isLogin = api.login(email, password)

        api.get_red_heart_songs()

    def run(self):
        print "Run"


if __name__ == '__main__':
    UI().run()
