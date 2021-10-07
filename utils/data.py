import discord
import random

from utils import permissions
from utils import default
from discord.ext.commands import Bot
from utils import music_interface

class Bot(Bot):
    def __init__(self, *args, **kwargs):
        self.q = Queue(self)
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

class Queue():
    def __init__(self, bot):
        self.bot = bot
        self.q = []
        self.ctx = None

    def __str__(self):
        return self.q.__str__()

    async def play_next(self, ctx):
        if self.q == []:
            # queue is empty
            return

        # ctx.voice_client.play(self.q[0][0])

        self.voice_state.channel.guild.voice_client.play(self.q[0][0])

    # info is a list containing [ name , url ]
    async def add(self, to_add, index=0):
        audio_source, url = None, ''

        # check if its a link -- rudimentary test here, get smth better
        if to_add.startswith('https://'):
            # check if its youtube
            if 'youtube' in to_add:
                audio_source, url = await music_interface.from_url_yt(to_add, loop=self.bot.loop)

            # check if its spotify
            elif 'spotify' in to_add:
                audio_source, url = await music_interface.from_url_spotify(to_add, loop=self.bot.loop)

        # if not a link, search youtube
        else:
            audio_source, url = await music_interface.from_search(to_add, loop=self.bot.loop)

        if not audio_source or not url:
            raise Exception(f'Audio source not found for {to_add}')

        self.q.insert(index, (audio_source, [ to_add, url ]))

        return url

    def remove(self, index=0):
        self.q.pop(index)

    def shuffle(self):
        random.shuffle(self.q)

    def get_q(self):
        q = []
        for song in self.q:
            q.insert(0, song[1])
        return q
