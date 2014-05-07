class History:
    def __init__(self, path):
        self.path = path
        self.data = {}
        self.comments = ''

    def set(self, name, season, episode):
        if self.data[name][0] == season and self.data[name][1] >= episode:
            return
        self.data[name] = (season, episode)

    def title(self, name):
        pretty = name.replace('.', ' ')
        return pretty.title()

    def load(self):
        fd = open(self.path, 'r')
        buffer = fd.readlines()
        for line in map(str.strip, buffer):
            if line.startswith('#'):
                self.comments += '%s\n' % line
            else:
                title, episode = line.split('=')
                s, e = map(lambda x: int(x.strip()), episode.split(','))
                self.data[title.strip()] = (s, e)
        fd.close()

    def save(self):
        fd = open(self.path, 'w')
        for name in sorted(self.data.keys()):
            fd.write('%s=%s,%s\n' % (name, self.data[name][0],
                                     self.data[name][1]))
        fd.close()
