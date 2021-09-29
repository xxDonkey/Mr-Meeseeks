import discord

from discord.ext import commands
from utils import default 
from utils import music_interface
from utils.data import Queue

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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

    """ Plays the requested song immediately. Skips the current song, and pauses the queue. """
    @commands.command(aliases=['fp'])
    async def forceplay(self, ctx, to_play):
        # queue song next
        self.q.add(to_play, 1) 

        # skip to next song
        self.skip()

    """ Adds a song to the queue. """
    @commands.command(aliases=['p'])
    async def play(self, ctx, to_add):
        # add to end of the queue
        self.q.add(to_add)

        # start playing if we aren't already
        if not ctx.voice_client.isplaying():
            self.q.play_next(ctx)

    """ Skips the current song in the queue. """
    @commands.command(aliases=['s'])
    async def skip(self, ctx):
        # stop the audio that is playing
        if ctx.voice_client.isplaying():
            ctx.voice_client.stop()

        # remove the current song
        self.q.remove()

        # play the next song
        self.q.play_next(ctx)

    """         Checks if the bot is in a voice channel.        """
    """ Called before 'forceplay,' 'play,' or 'skip' is called. """
    @forceplay.before_invoke
    @play.before_invoke
    @skip.before_invoke
    async def ensure_voice_channel(self, ctx):
        # if not connected to voice
        if ctx.voice_client is None:
            # and the commander is in a channel, connect to it
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()

            # otherwise error
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")

def setup(bot):
    bot.add_cog(Voice(bot))