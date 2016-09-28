# coding: utf-8

class Song(object):
    def __init__(self, song_json):
        self._parse(song_json)

    def _parse(self, song_json):
        self.sid = song_json['sid']
        self.picture = song_json['picture']
        self.artist = song_json['artist']
        self.title = song_json['title']

        self.length = song_json['length']
        self.url = song_json['url']

    @staticmethod
    def parse(song_json):
        return Song(song_json)

    # {u'status': 0,
    # u'picture': u'http://img3.doubanio.com/lpic/s1793998.jpg',
    # u'alert_msg': u'',
    # u'albumtitle': u'\u5927\u70ed',
    # u'url': u'http://mr1.doubanio.com/b1cf80ae31d9015054f2e6cdd69c5f41/0/fm/song/p278561_128k.mp4',
    # u'album': u'/subject/1407383/',
    # u'artist': u'\u5f20\u56fd\u8363',
    # u'ssid': u'715d',
    # u'public_time': u'2000',
    # u'subtype': u'',
    # u'length': 221,
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