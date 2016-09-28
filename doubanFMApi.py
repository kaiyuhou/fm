# coding: utf-8
import requests
from Song import *

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

        #{u'description': u'',
        # u'collected_count': 0,
        # u'title': u'\u6211\u7684\u7ea2\u5fc3\u6b4c\u66f2',
        # u'offshelf_alert': u'\u90e8\u5206 ... \u5427',
        # u'creator': {u'url': u'https://www.douban.com/people/51758087/',
            # u'picture': u'http://img3.doubanio.com/icon/user_normal.jpg',
            #u'id': u'51758087',
            #u'name': u'\u674e\u6bc5\u7684\u5927\u5200\u8089'},
        # u'cover': u'',
        # u'updated_time': u'2015-01-01 00:00:00',
        # u'is_collected': True,
        # u'rec_reason': u'',
        # u'created_time': u'',
        # u'can_play': True,
        # u'type': -1,
        # u'id': -1,
        # u'songs': [{u'update_time': 1470125786, u'sid': u'278561', u'playable': True, u'like': 1},
        #            {u'update_time': 1470126018, u'sid': u'680412', u'playable': True, u'like': 1},
        #            {u'update_time': 1470126161, u'sid': u'1477098', u'playable': True, u'like': 1},

        song_sids = ""

        for song in rsp['songs']:
            if song['playable'] is True and len(song_sids) < 100:
                song_sids += song['sid'] + '|'

        song_sids = song_sids[:-1]

        rsp = requests.post('%s/v2/fm/songs' % doubanFMApi.API_HOST_URL, data={
            'sids': song_sids,
            'kbps': '128',
            'app_name': doubanFMApi.APP_NAME,
            'version': doubanFMApi.VERSION,
            'apikey': doubanFMApi.KEY,
        }, headers={'Authorization': self.auth_access_token}).json()

        # {u'status': 0,
        # u'picture': u'http://img3.doubanio.com/lpic/s1793998.jpg',
        # u'alert_msg': u'',
        # u'albumtitle': u'\u5927\u70ed',
        # u'url': u'http://mr1.doubanio.com/b1cf80ae31d9015054f2e6cdd69c5f41/0/fm/song/p278561_128k.mp4',
        # u'album': u'/subject/1407383/',
        # u'artist': u'\u5f20\u56fd\u8363',
        # u'ssid': u'715d',
        # u'public_time': u'2000',
        # u'subtype': u'', u'length': 221,
        # u'kbps': u'128',
        # u'aid': u'1407383',
        # u'sid': u'278561',
        # u'title': u'\u6211',
        # u'file_ext': u'mp4',
        # u'sha256': u'513ad614c45d3a5bc8c5b6aa1e5215d034a015aef3dceba8be3ab74d68294126',
        # u'singers': [{u'name': u'\u5f20\u56fd\u8363',
            # u'name_usual': u'\u5f20\u56fd\u8363',
            # u'avatar': u'http://img7.doubanio.com/img/fmadmin/small/31245.jpg',
            # u'related_site_id': 0,
            # u'is_site_artist': False,
            # u'id': u'1445'}],
        # u'release': {u'link': u'https://douban.fm/album/1407383ge200',
            # u'id': u'1407383',
            # u'ssid': u'e200'}}

        return map(Song.parse, rsp)

