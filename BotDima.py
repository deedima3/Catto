import discord
from discord.ext import commands
import random
import pandas as pd
import datetime as dt
import convertapi
import os
import time
import threading

#This is Data
bot = commands.Bot(command_prefix = "!")
TOKEN = 'TOKEN HERE'
convertapi.api_secret = 'SECRET HERE'
respond = [
    'Im not your catto',
    'yes?',
    'nyan?',
    'meoww?'
]
patrespond = [
    '*happy noises*',
    'Arigatou',
    '*purr*',
]
catcall = ("catto", 'cat',"Catto")
ajakanmaen = ("Maen", "main", "Maen", "maen")
# df = pd.read.csv('/CSV/jadwal.csv')

#Event
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(catcall):
        pesan = random.choice(respond) + " " + '{0.author.mention}'.format(message)
        await message.channel.send(pesan)

    if message.content.startswith(ajakanmaen):
        if f'{message.author}' == "50Shades of Gandalf the Grey#9322":
            pesan = "Ayok" + " " + '{0.author.mention}'.format(message)
            await message.channel.send(pesan)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with a Cat || Ryvenna"))
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------')
    # await loop()

    # while True:
    #     nowhour = dt.datetime.now().strftime("%H")
    #     if nowhour == "06":
    #         channel = bot.get_channel(542163375191359498)
    #         await channel.send("Meowning~")
    #         time.sleep(3600)
    #
    # t1 = threading.Thread(target=on_ready)
    # t1.start()

    # while True:
    #     nowaja = dt.datetime.now().strftime("%")
    #     if now is in f'{df["jam"]}':
    #         channel = bot.get_channel(542163375191359498)
    #         row = df.loc[df['jam']] == now]
    #         userid = "<@" + f'{row.iloc[0,1]}' + ">"
    #         await channel.send(f'{row.iloc[0,2]}' + f'{userid}')
    #     time.sleep(900)



#Command
@bot.command()
async def pat(ctx):
    print(f'{ctx.message.author} need some attention')
    await ctx.message.channel.send(file = discord.File(r'D:/C/Python/DiscordBot/Pat/' + f'{random.randint(1, 10)}' + '.gif'))
    await ctx.message.channel.send(random.choice(patrespond))

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.message.channel.send(f"{amount} message cleared")

@bot.command()
async def convertpdf(ctx):
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("Error")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            result = convertapi.convert('pdf', { 'File': f"{url}" })
            dir = r'D:/C/Python/DiscordBot/PDF' + f'/{ctx.message.author}' + f'{random.randint(1, 99999)}' +'.pdf'
            if os.path.exists(f'{dir}'):
                os.remove(f'{dir}')
            result.file.save(f'{dir}')
        await ctx.send(file=discord.File(dir))

@bot.command()
async def introduce(ctx):
    await ctx.message.channel.send("Hello, I'm Dima's Bot Catto~")
    await ctx.message.channel.send("You can help edit me in -paste github link here-")

# @bot.command()
# async def remindme(ctx):
# def loop():

@bot.command()
async def shutdown(ctx):
    await ctx.bot.logout()




bot.run(TOKEN)
