#https://github.com/Rapptz/discord.py
import discord
import discord.ext
import asyncio
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
import random
import os
import sys
from tkinter import *
from subprocess import call

BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)

BToken = 'NDg0MzYwODQxODk0ODIxODg4.Dmg4Aw.DFviMVEp3O8XTUerOHI0xCJLUYo'
 
client = discord.Client()
 
@client.command(brief="tells you about the latest update")
async def upgraded():
    await client.say("Yes, I have been upgradededed, ERROR, Ignoring Exception in ERROR... - I now have exceptions, an error no longer has any futher effect, so yes, no more crashing")
 
@client.command()
async def description():
    await client.say("Young One, You Are Incapable Of Comprehending The Purpose Of This Mystique. Those Whom Are Desperate Enough For Wisdom Shall Loose Their Sanity In The Process Of Learning About This Mystique.")
 
@client.command()
async def adt():
    await client.say("A D T, Actual Description Truth | You See, My Purpose Is To Make People Like Servers More, While Messing With Their Sanity As A Side-Effect try to decipher: TOB A YB DELLORT")
 
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
 
 
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with people's sanity"))
    print("Logged in as " + client.user.name)
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
   
    if message.content.upper().startswith('-1ST LOGO'):
        embed = discord.Embed(title="The Deer", description="A deer folowed by are name and slogon!", color=0x8A2BE2)  
        embed.set_image(url="https://media.discordapp.net/attachments/482488997562810372/484291921695473665/Capture.PNG")
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('-2ND LOGO'):
        embed = discord.Embed(title="The Paint Splash", description="A splash of paint on a wall followed by are name and Slogon!", color=0x8A2BE2)
        embed.set_image(url="https://media.discordapp.net/attachments/482488997562810372/484291857078288384/logo-preview-6645700b-398a-4c93-946a-b643ac9d11dc.jpg?width=300&height=300")
        await client.send_message(message.channel, embed=embed)
 
    if message.content.upper().startswith('-3RD LOGO'):
        embed = discord.Embed(title="The Crossed Arrows", description="2 arrows crossed followed by are name and slogon!", color=0x8A2BE2)  
        embed.set_image(url="https://media.discordapp.net/attachments/482488997562810372/484291855186395136/logo-preview-51aa1a3b-a500-496c-bbf9-48bc6ae9a402.jpg?width=300&height=300")
        await client.send_message(message.channel, embed=embed)
 
 
    if message.content.upper().startswith('-STAFFAPP'):
        embed = discord.Embed(title="Staff Application", description="Click the link to be redirected to google were you can apply to be staff!", color=0x2B8AE2)  
        embed.add_field(name="Google Link", value="https://goo.gl/forms/NZuAAgVgQjU6NX743", inline=True)
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
 
 
    if message.content.upper().startswith('-COMMAND (MUST BE IN ALL CAPS)'):
        embed = discord.Embed(title="TITLE", description="SOME OTHER TEXT WITH REPRODUTCIVE ORGANS?", color=0x8A2BE2)
        embed.add_field(name="Google Link", value="https://goo.gl/forms/NZuAAgVgQjU6NX743", inline=True)
        await client.send_message(message.channel, embed=embed)
 
 
 
 
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
        await client.delete_message(message)
#Login
@client.event
async def on_ready():
    print('Connected')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    await client.change_presence(game=Game(name="OOps"))

client.run(BToken)
