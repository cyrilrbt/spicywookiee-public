import re
import os, os.path
from spicywookiee.reader import Reader
from spicywookiee.downloader import Downloader
from spicywookiee.history import History


FEEDS = (
)
BASE_PATH = os.path.join(os.path.dirname(__file__), '..')


def fetch():
    h = History(os.path.join(BASE_PATH, 'History.txt'))
    h.load()

    candidates = []
    for feed in FEEDS:
        r = Reader(feed)
        r.load()
        candidates.extend(r.items)

    for c in sorted(candidates, key=lambda x: x[0]):
        print c[0], c[1]

    for name, (season, episode) in h.data.items():
        pending = set([])
        found = []
        for c in candidates:
            show_match = re.search("^" + name, c[0], re.IGNORECASE)
            if show_match:
                if (c[2] == season and c[3] > episode) or c[2] > season:
                    k = "%02s%02s" % (c[2], c[3])
                    if k not in pending:
                        pending.add(k)
                        found.append(c)
        if found:
            for f in found:
                filename = 'show-%s-%s-%s.torrent' % (name, f[2], f[3])
                print h.title(name), filename, f[1]
                if f[1].startswith('magnet'):
                    os.system("open \"%s\"" % f[1])
                else:
                    d = Downloader(f[1])
                    d.download(os.path.join(BASE_PATH, filename))
                    h.set(name, f[2], f[3])

    h.save()
