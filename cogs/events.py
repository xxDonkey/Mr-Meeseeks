import discord

from discord.ext import commands
from discord.ext.commands import errors
from utils import default 

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Sucessfully logged in.")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member != self.bot.user:
            return

        self.bot.q.voice_state = after

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument) or isinstance(err, errors.TooManyArguments):
            cmd = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
            await ctx.send_help(cmd)

        elif isinstance(err, errors.CommandInvokeError):
            error = default.get_traceback(err.original)

            if '2000 or fewer' in str(err) and len(ctx.message.clean_content) > 1900:
                return await ctx.send('You attempted to make the command display more than 2,000 characters.\nBoth the error and the command will be ignored.')

            print(err)
            await ctx.send(f'There was an error processing the command. {error}')
        
        elif isinstance(err, errors.MaxConcurrencyReached):
            await ctx.send(f'You\'ve reached max capacity of command usage at once, please finish the previous one.')

        elif isinstance(err, errors.CommandOnCooldown):
            await ctx.send(f'This command is on cooldown. Try again in {err.retry_after:.2f} seconds.')

        elif isinstance(err, errors.CheckFailure):
            pass

        elif isinstance(err, errors.CommandNotFound):
            pass

def setup(bot):
    bot.add_cog(Events(bot))