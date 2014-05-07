import re
import StringIO
from xml.dom import minidom

from spicywookiee.downloader import Downloader


class Reader:
    def __init__(self, url):
        self.url = url
        self.items = []

    def _read_field(self, item, name):
        field = None
        try:
            field = item.getElementsByTagName(name)[0].childNodes[0].nodeValue
        except:
            pass
        return field

    def _read_attr(self, item, name, attname):
        field = None
        try:
            field = item.getElementsByTagName(name)[0]._attrs[attname].nodeValue
        except:
            pass
        return field

    def _parse_season(self, title):
        season = episode = 0
        try:
            matches = re.search(r'S?(\d{1,2})[ExeX]{1,1}(\d{1,2})', title)
        except:
            pass
        if matches is not None:
            season = int(matches.group(1))
            episode = int(matches.group(2))

        return (season, episode)

    def load(self):
        d = Downloader(self.url)
        try:
            dom = minidom.parse(StringIO.StringIO(d.load()))
        except:
            dom = None

        if dom:
            for item in dom.getElementsByTagName('item'):
                title = self._read_field(item, 'title')
                link = self._read_field(item, 'link')
                enc = self._read_attr(item, 'enclosure', 'url')
                if enc:
                    link = enc
                season, episode = self._parse_season(title)
                if season and episode:
                    self.items.append((title, link, season, episode))
