import discord

from utils import default

config = default.get("config.json")

def is_admin(ctx):
    return ctx.message.author.guild_permissions.administrator

def link_channel(ctx):
    return ctx.channel.name == config.link_channel

def update_channel(ctx):
    return ctx.channel.name == config.role_update_channel
