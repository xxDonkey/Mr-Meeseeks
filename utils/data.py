import discord
import random

from utils import permissions
from utils import default
from discord.ext.commands import Bot
from utils import music_interface

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
        self.ctx = None

    def __str__(self):
        return self.q.__str__()

    async def play_next(self, ctx):
        if self.q == []:
            # queue is empty
            return

        ctx.voice_client.play(self.q[0], after=after_play)

    async def after_play(self, e):
        self.remove()


    async def add(self, to_add, index=0):
        to_play = to_play.lower()
        audio_source = None

        # check if its a link -- rudimentary test here, get smth better
        if to_play.startswith('https://'):
            # check if its youtube
            if to_play.contains('youtube'):
                audio_source = await music_interface.from_url_yt(to_play)

            # check if its spotify
            elif to_play.contains('spotify'):
                audio_source = await music_interface.from_url_spotify()(to_play)

        # if not a link, search youtube
        else:
            audio_source = await music_interface.from_search(to_play)

        self.q.insert(audio_source, index)

    def remove(self, index=0):
        self.q.pop(index)

    def shuffle(self):
        random.shuffle(self.q)



