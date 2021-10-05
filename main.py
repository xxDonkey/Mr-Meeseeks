import os
import nacl

from dotenv import load_dotenv
from utils.data import Bot
from utils.default import get

load_dotenv()
config = get()

print('Logging in...')

bot = Bot(
    command_prefix  = config.prefix,
    command_attrs   = dict(hidden=True)
)

for file in os.listdir('cogs'):
    if file.endswith('.py'):
        name = file[:-3]
        bot.load_extension(f'cogs.{name}')

bot.run(os.getenv('TOKEN'))

