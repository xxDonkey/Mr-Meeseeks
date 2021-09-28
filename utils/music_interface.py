import youtube_dl

from utils import default

ytdl = youtube_dl.YoutubeDL(
    default.get(file='ytdl_format.json', named_tuple=False)
)

def from_url():
    pass

def from_search():
    pass