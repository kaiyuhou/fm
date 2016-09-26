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


class UI():
    def __init__(self):
        print "Hello World!"

        self.setup_ui()

    def setup_ui(self):
        email = raw_input('豆瓣账户 (Email地址): ')
        password = raw_input('豆瓣密码: ')

        print email, password

    def run(self):
        print "Run"


if __name__ == '__main__':
    UI().run()
