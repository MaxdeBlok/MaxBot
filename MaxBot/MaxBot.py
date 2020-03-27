import discord
import BeerbotFunction as bb
import asyncio
from discord.ext import commands
import random
import time

TOKEN = 'NjkyMTA4NjU4NjM2NzUwODQ5.XnqKyQ.iPyJXr_wzkVIxmoGOnMM0rHXQR4'
client = discord.Client()
command_prefix = 'beerbot'
Joel_enabled_servers = ('TESTUNIT', 'HJC FiDes', 'Heil Hilter maar is wel maar een grapje natuurlijk')
RPC_games = []

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    #alleen servers met mathon en mij
    if 'pils' in message.content:
        if 'beerbot' not in message.content:
            if any(str(message.guild) in s for s in Joel_enabled_servers):
                with open('pils.gif', 'rb') as f:
                    pils = discord.File(f)
                    await message.channel.send('ha pils')
                    await message.channel.send(file=pils)

    #moet gewoon
    if '49' in message.content:
        await message.channel.send('49 Vo')

    #beschrijving
    if command_prefix == message.content:
        await message.channel.send('Mijn doel is discord zuipjes wat leuker te maken. Ik geef antwoord op je vragen en met mij kan je leuke drankspelletjes spelen (Work in progress)')

    #help voor alle commands
    if message.content.startswith('{0} help'.format(command_prefix)):
        #send message in channel
        await message.author.send('Om een van de onderstaande commands te gebruiken, typ je eerst `beerbot` en daarna het command \n \n'
                                  '**moetikadt:** bierbot zal je vertellen of jij een adt moet trekken \n'
                                  '**Steenpapieradt:** start een game steenpapierschaar \n'
                                  '**pilstijd:** laat zien of het al tijd is voor pilskes')
        print(message.channel)

    #Checken of het tijd is voor pils
    if message.content.startswith('{0} pilstijd'.format(command_prefix)):
        await bb.check_beer_time(message)

    #Steen papier adt
    if str('{0} steenpapieradt'.format(command_prefix)) == message.content:
        game = bb.steen_papier_schaar(message)
        game.choose_opponent()

    #Moet ik een adt
    if message.content.startswith('beerbot moetikadt'):
        bb.moetikadt(message)



#bot.add_command(test)
client.run(TOKEN)





