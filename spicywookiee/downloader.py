import zlib
import requests


class Downloader:
    def __init__(self, url):
        self.url = url
        self.data = ""

    def load(self):
        try:
            self.data = requests.get(self.url).content
        except:
            print "Load fail:", self.url
            self.data = ""
        try:
            d = zlib.decompress(self.data)
            self.data = d
        except:
            pass
        return self.data

    def download(self, path):
        open(path, 'w').write(self.load())
