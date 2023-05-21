from ctypes import memset
import discord
import asyncio
from discord.ext import commands

#     token

token = 'YOUR TOKEN'

#     intents

intents = discord.Intents.default()
intents.message_content = True

#     bot

bot = commands.Bot(command_prefix='!', intents=intents)


#     @bot.event

@bot.event
async def on_ready():
    print("bot run shod")
    print("zibast")

@bot.event
async def on_disconnect():
    print("bot dc shod")

#     @bot.command

bot.command()
async def MY_USERNAME(ctx):
    await ctx.send(ctx.author)

#

@bot.command()
async def tekrar(ctx,*,args):
    await ctx.send(args)

#

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,Dalil = None):
    await member.kick(reason=Dalil)
    await ctx.send("fard mored nazar kick shod")    

#     bot command 1


#     bot runer

bot.run(token)