# import random
# import asyncio
import logging
# import logging.handlers

import discord # https://github.com/Rapptz/discord.py, https://discordpy.readthedocs.io/en/latest/
# from discord.ext import commands
from config import token
from config import stact
# from config import prefix

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{stact}'))

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f'Welcome, {member.mention}, to {guild.name}!')

@client.event
async def on_member_remove(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f'Farewell, {member.mention}. We\'re sorry to see you go!')

@client.event
async def on_message(message):
    # Prevents the bot from replying to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author.mention}!', mention_author=True)

    if message.content.startswith('$test'):
        guild = message.author.guild
        if guild.system_channel is not None:
            await guild.system_channel.send(f'Welcome {message.author.mention} to {guild.name}!')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        
# 'token' is acquired from https://www.discord.com/developers/applications/
client.run(token, log_handler=handler, log_level=logging.DEBUG)

# @client.event
# async def on_connect():
#     await