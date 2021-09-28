import discord

from discord.ext import commands
from discord.ext.commands import errors
from utils import default 

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get()

    """ Joins the voice channel of the user who entered the command. """
    @commands.command(aliases=['join', 'j'])
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await channel.connect()

    @commands.command(aliases=['disconnect', 'dis'])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(aliases=['play', 'p'])
    def play(self, ctx, to_play):

        # check if its a link

        # check if its youtube
        # check if its spotify
        # abort if neither

        # if not a link, search youtube

        pass


def setup(bot):
    bot.add_cog(Events(bot))