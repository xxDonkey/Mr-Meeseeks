import discord
import random

from utils import permissions
from utils import default
from discord.ext.commands import Bot

class Bot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message(self, msg):
        if not self.is_ready() or msg.author.bot:
            return

        await self.process_commands(msg)

class Embed(discord.Embed):
    def __init__(self, bot, footer=None, **kwargs):
        super().__init__(**kwargs)
        self.config = default.get()

        self.set_footer(text=f'Support: {self.config.bot_author}', icon_url=bot.user.avatar_url_as(size=1024))
        self.timestamp = default.get_timestamp()

class Queue():
    def __init__(self):
        self.q = []

    def __str__(self):
        return self.q.__str__()

    def add(self, audio_player):
        self.q.append(audio_player)

    def remove(self):
        pass

    def shuffle(self):
        random.shuffle(self.q)



