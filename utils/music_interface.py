import asyncio
import discord
import youtube_dl

from utils import default
from youtube_search import YoutubeSearch

# Silence console warning errors 
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl = youtube_dl.YoutubeDL(
    default.get(file='ytdl_format.json', named_tuple=False)
)

ffmpeg_opts = default.get(file='ffmpeg_opts.json', named_tuple=False)

""" Returns a Discord audio player from a Youtube link. """
async def from_url_yt(url, loop=None):
    loop = loop or asyncio.get_event_loop()

    try:
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
    except youtube_dl.utils.DownloadError:
        return None

    # if its a playlist, take first entry
    if 'entries' in data:
        data = data['entries'][0]

    filename = ytdl.prepare_filename(data)
    return discord.FFmpegPCMAudio(filename, **ffmpeg_opts)
    

""" Returns a Discord audio player from a Spotify link. """
async def from_url_spotify(url, loop=None):
    pass

""" Returns a Discord audio player from a Youtube keyword. """
async def from_search(search, loop=None):
    # search youtube for the URL
    data = YoutubeSearch(search, max_results=1).to_dict()[0]
    url = 'https://www.youtube.com' + data['url_suffix']

    # get the link's source
    return await from_url_yt(url)

    
    