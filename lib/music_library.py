class MusicLibrary:
    def __init__(self):
        self.tracks =  []

    def add(self, track):
        self.tracks.append(track)

    def search_by_title(self, keyword):
        to_return = []
        for item in self.tracks:
            print(item.title)
            if keyword.lower() in str(item.title.lower()):
                to_return.append(item)
        return to_return
