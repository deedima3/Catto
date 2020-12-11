import discord
from discord.ext import commands
import random
import pandas as pd
import datetime as dt

bot = commands.Bot(command_prefix = "!")
TOKEN = 'NzgzMTk2MjQ0MDEyNTY0NDgw.X8XOVw.Q9tR0q_tFRMCVNV6-JPzl2gTrXo'

#Event
@bot.event
async def on_message(message):
    input = ("catto", 'cat',"Catto")
    if message.author == bot.user:
        return

    if message.content.startswith(input):
        respond = [
            'Im not your catto',
            'yes?',
            'nyan?',
            'meoww?'
        ]
        pesan = random.choice(respond) + " " + '{0.author.mention}'.format(message)
        await message.channel.send(pesan)
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    input = ("")

#Command
@bot.command()
async def pat(ctx):
    print('{0.author} need some attention')
    await ctx.message.channel.send("Nyan~")

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.message.channel.send(f"{amount} message cleared")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with a Cat || Ryvenna"))
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------')


bot.run(TOKEN)
