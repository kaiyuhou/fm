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
import requests

class doubanFMApi():
    API_HOST_URL = "https://api.douban.com"
    TOKEN_HOST_URL = "https://www.douban.com"
    APP_NAME = "radio_android"
    VERSION = "642"
    KEY = "02f7751a55066bcb08e65f4eff134361"
    SECRET = "63cf04ebd7b0ff3b"

    def __init__(self):
        self.auth_access_token = None

        print 'douban FM API init'

    def login(self, email, password):
        rsp = requests.post('%s/service/auth2/token' % doubanFMApi.TOKEN_HOST_URL, data={
            'username': email,
            'password': password,
            'client_id': doubanFMApi.KEY,
            'client_secret': doubanFMApi.SECRET,
            'grant_type': 'password',
            'apikey': doubanFMApi.KEY,
        }).json()

        #{u'access_token': u'a7fc0ab76f94fd53f7f420264ebef7f9',
        # u'expires_in': 7775999,
        # u'douban_user_name': u'\u674e\u6bc5\u7684\u5927\u5200\u8089',
        # u'douban_user_id': u'51758087',
        # u'refresh_token':
        # u'7d484536d784854577d8cfa4868d8fcf'}

        #{u'msg': u'username_password_mismatch',
        # u'code': 120,
        # u'request': u'POST /auth2/token'}

        if not rsp.has_key('access_token'):
            print "登陆失败：",
            if rsp.has_key('msg'):
                print rsp['msg']
            else:
                print rsp
            return False
        else:
            print "登陆成功： ", rsp['douban_user_name']
            self.auth_access_token = "Bearer %s" % rsp['access_token']
            print self.auth_access_token
            return True

    def set_auth_access_token(self, token):
        self.auth_access_token = token


    def get_red_heart_songs(self):
        if self.auth_access_token is None:
            return []

        rsp = requests.get('%s/v2/fm/redheart/basic' % doubanFMApi.API_HOST_URL, params={
            'app_name': doubanFMApi.APP_NAME,
            'version': doubanFMApi.VERSION,
        }, headers={'Authorization': self.auth_access_token}).json()

        for song in rsp['songs']:
            if song

class UI():
    def __init__(self):
        print "UI init"

        self.setup_ui()

    def setup_ui(self):
        isLogin = True #False
        api = doubanFMApi()
        api.set_auth_access_token('Bearer af3d725cdd82e7b70db857169888b725')

        while not isLogin:
            email = raw_input('豆瓣账户 (Email地址): ')
            password = raw_input('豆瓣密码: ')


            isLogin = api.login(email, password)

        api.get_red_heart_songs()

    def run(self):
        print "Run"


if __name__ == '__main__':
    UI().run()
