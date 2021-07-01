"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    playlistname = None
    videos = []

    def __init__(self,_name):
        self.playlistname = _name

    def addvideo(self,video_id):
        self.videos.append(video_id)
