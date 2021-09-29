import discord

from discord.ext import commands
from discord.ext.commands import errors
from utils import default 
from utils import music_interface
from utils.data import Queue

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get()
        self.q = Queue()

    """ Joins the voice channel of the user who entered the command. """
    @commands.command(aliases=['j'])
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await channel.connect()

    """ Disconnects the bot from the currently joined channel. """
    @commands.command(aliases=['dis'])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    """ Plays the requested song immediately. Pauses the queue. """
    @commands.command(aliases=['fp'])
    async def forceplay(self, ctx, to_play):
        to_play = to_play.lower()
        player = None

        # check if its a link -- rudimentary test here, get smth better
        if to_play.startswith('https://'):
            # check if its youtube
            if to_play.contains('youtube'):
                player = music_interface.from_url_yt(to_play)

            # check if its spotify
            elif to_play.contains('spotify'):
                player = music_interface.from_url_spotify()(to_play)

        # if not a link, search youtube
        else:
            player = music_interface.from_search(to_play)

      # player should not contain the audio player

    """ Adds a song to the queue. """
    @commands.command(aliases=['p'])
    async def play(self, ctx, to_add):
        
        pass

def setup(bot):
    bot.add_cog(Commands(bot))