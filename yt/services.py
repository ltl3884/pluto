from pytube import YouTube
import time


class YtInfo:

    def __init__(self, url):
        self.url = url

    def yt_info(self):
        info = {}
        yt = YouTube(self.url)
        info['videos'] = yt.streams.filter(only_video=True, file_extension='mp4', is_dash=True).all()
        info['audios'] = yt.streams.filter(only_audio=True).all()
        info['captions'] = yt.caption_tracks
        info['title'] = yt.title
        info['length'] = time.strftime('%H:%M:%S', time.gmtime(yt.length))
        info['thumbnail_url'] = yt.thumbnail_url
        # v = {"resolution": '1080p', "mime_type": 'mp4', "filesize": 677889, "default_filename": '1234',
        #      "url": 'http://www.xxx.com', 'abr': '128kps'}
        # c = {"url": 'https://www.youtube.com/api/timedtext?v=kZ6Nf2vsSNc&asr_langs=de,en,es,fr,it,ja,ko,nl,pt,ru&caps=asr&xorp=true&hl=en&ip=0.0.0.0&ipbits=0&expire=1595089625&sparams=ip,ipbits,expire,v,asr_langs,caps,xorp&signature=4415246BC23439ED3C78D0883CED6720990FFAB3.BB9825FDDDA14D63F48AE0326A71DB480AFBF775&key=yt8&lang=zh', 'code': 'zh-cn', 'name': 'chinese'}
        # info['videos'] = [v]
        # info['audios'] = [v]
        # info['captions'] = [c]
        # info['title'] = '1234'
        # info['length'] = time.strftime('%H:%M:%S', time.gmtime(11122))
        # info['thumbnail_url'] = 'https://i.ytimg.com/vi/g2oBfc_FxGs/maxresdefault.jpg?v=5e05b6e5'
        return info
