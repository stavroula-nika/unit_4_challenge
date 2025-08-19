
class music():

    def __init__(self):
        self.playlist = []

    def add_track(self, track):
        if type(track) != str or track == "":
            raise Exception("Input valid track!")
        self.playlist.append(track)

    def see_playlist(self):
        return self.playlist