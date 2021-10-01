import discord
import math

from discord.ext import commands
from utils import default

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """ Gets the latency of the bot. """
    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency * 1000 # convert to ms
        level = default.clamp(math.floor(latency / 50), 0, 4)

        user = '{0.user}'.format(self.bot)
        response = f'{user} has a response time of {math.round(latency)} ' + (':exclamation: ' * level)
        await ctx.channel.send(response)

def setup(bot):
    bot.add_cog(Utility(bot))