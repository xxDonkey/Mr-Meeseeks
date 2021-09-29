import youtube_dl

from utils import default

ytdl = youtube_dl.YoutubeDL(
    default.get(file='ytdl_format.json', named_tuple=False)
)

ffmpeg_opts = default.get(file='ytdl_format.json', named_tuple=False)

""" Returns a Discord audio player from a Youtube link. """
def from_url(url):
    pass

""" Returns a Discord audio player from a Youtube keyword. """
def from_search():
    pass