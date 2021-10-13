import discord

from discord.ext import commands, tasks
from utils import default 
from utils import music_interface

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_song_finished.start()

    """ Joins the voice channel of the user who entered the command. """
    @commands.command(aliases=['j'])
    async def join(self, ctx):
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except discord.errors.ClientException:
            pass

    """ Disconnects the bot from the currently joined channel. """
    @commands.command(aliases=['dis'])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    """ Plays the requested song immediately. Skips the current song, and pauses the queue. """
    @commands.command(aliases=['fp'])
    async def forceplay(self, ctx, to_play):\
        # join the channel
        await self.join(ctx)

        # queue song next and get the url
        url = await self.bot.q.add(to_play, 1) 

        # skip to next song
        self.skip()

        # get next song info
        _, info = self.bot.q.q[-1]
        to_play, url = info

        await ctx.channel.send(f':musical_note:   Playing __**"{to_play}"**__   :musical_note:\n{url}')

    """ Adds a song to the queue. """
    @commands.command(aliases=['p'])
    async def play(self, ctx, *to_play):
        # join the channel
        await self.join(ctx)

        to_play = ' '.join(to_play)

        # add to end of the queue and get the url
        url = await self.bot.q.add(to_play)

        # start playing if we aren't already
        if not ctx.voice_client.is_playing():
            await self.bot.q.play_next()

        # get next song info
        _, info = self.bot.q.q[-1]
        to_play, url = info

        await ctx.channel.send(f':musical_note:   Playing __**"{to_play}"**__   :musical_note:\n{url}')

    """ Skips the current song in the queue. """
    @commands.command(aliases=['s'])
    async def skip(self, ctx):
        # stop the audio that is playing
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        # remove the current song
        self.bot.q.remove()

        # play the next song
        await self.bot.q.play_next()

        await ctx.channel.send(f':track_next:   Skipping!   :track_next:')

        if self.bot.q.q == []:
            return

        # get next song info
        _, info = self.bot.q.q[-1]
        to_play, url = info

        await ctx.channel.send(f':musical_note:   Playing __**"{to_play}"**__   :musical_note:\n{url}')

    """ Shuffles the queue. """
    @commands.command()
    async def shuffle(self):
        self.bot.q.shuffle()

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

    @tasks.loop(seconds=1/20)
    async def check_song_finished(self):
        if self.bot.q.finished:
            print('Called "check_song_finished"')
            self.bot.q.remove()
            await self.bot.q.play_next()
            self.bot.q.finished = False

def setup(bot):
    bot.add_cog(Voice(bot))