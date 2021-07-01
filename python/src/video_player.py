"""A video player class."""
import datetime
import random
from .video_library import VideoLibrary
from .video_playlist import Playlist

class VideoPlayer:
    """A class used to represent a Video Player."""
    playing = None
    paused = False
    videostarttime = 0
    playlists = {}

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for i in self._video_library.get_all_videos():
            print(i.title,'| id :',i.video_id,'| tags :',i.tags)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        #playvideo=VideoLibrary.get_video(video_id) fucking bullshit
        if self.playing != None :
            self.stop_video()
            #pass
        inlist = False
        for i in self._video_library.get_all_videos():
            if i.video_id == video_id :
                playvideo = i.title
                inlist = True
        if inlist :
            print("Playing video:",playvideo)
            self.playing = playvideo
            self.videostarttime = datetime.datetime.now()
        else:
            print('Cannot play video: Video does not exist')

    def stop_video(self):
        """Stops the current video."""
        if self.playing == None :
            print('Cannot stop video: No video is currently playing')
        else:
            print("Stopping video:",self.playing)
        self.playing = None
        self.videostarttime = 0

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self.playing != None:
            self.stop_video()
            #pass
        videolist = self._video_library.get_all_videos()
        index = random.randint(0,len(videolist)-1)
        print("Playing video:",videolist[index].title)
        self.playing = videolist[index].title
        self.videostarttime = datetime.datetime.now()

    def pause_video(self):
        """Pauses the current video."""
        #how long its played for
        #second = str(datetime.datetime.now() - self.videostarttime)[5:]
        #minute = str(datetime.datetime.now() - self.videostarttime)[2:4]
        if self.playing == None:
            print('Cannot pause video: No video is currently playing')
        elif self.paused == True :
            print('Video already paused:',self.playing)
        else:
            print("Pausing video:",self.playing)
            self.paused = True

    def continue_video(self):
        """Resumes playing the current video."""
        if self.playing == None:
            print('Cannot continue video: No video is currently playing')
        elif self.paused == False :
            print('Cannot continue video: Video is not paused')
        else:
            print("Continuing video:",self.playing)
            self.paused = False


    def show_playing(self):
        """Displays video currently playing."""
        output = ''
        for i in self._video_library.get_all_videos():
            if i.title == self.playing :
                videodata = i
        if self.playing == None:
            print('No video is currently playing')
        else:
            output += videodata.title
            output += ' ('
            output += videodata.video_id
            output += ') '
            if len(videodata.tags) != 0:
                output += '['
                for t in videodata.tags:
                    output += t
                    output += ' '
                output = output[:-1]
                output += ']'
            if self.paused == True:
                print('Currently playing:',output,'- PAUSED')
            else:
                print("Currently playing:",output)

    def create_playlist(self, playlist_name):

        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #creates empty playlist
        self.playlists[playlist_name] = []
        print("created playlist :",playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
