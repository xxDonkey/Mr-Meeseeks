import youtube_dl

from utils import default

# Silence console warning errors 
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl = youtube_dl.YoutubeDL(
    default.get(file='ytdl_format.json', named_tuple=False)
)

ffmpeg_opts = default.get(file='ytdl_format.json', named_tuple=False)

""" Returns a Discord audio player from a Youtube link. """
def from_url_yt(url):
    pass

""" Returns a Discord audio player from a Spotify link. """
def from_url_spotify(url):
    pass

""" Returns a Discord audio player from a Youtube keyword. """
def from_search():
    pass