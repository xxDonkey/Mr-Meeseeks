import discord

from discord.ext import commands
from discord.ext.commands import errors
from utils import default 

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get()

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