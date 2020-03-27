import discord
import datetime
import random
import math

je_moet_adt = [
    'Tuurlijk, pilsrups',
    'vouw die bak',
    'trek hem leeg, kanjer',
    'giet hem je strot in',
    'Waar wacht je op?',
    'Trek hem!',
    'Nee, trek er twee',
    'Alleen als je het aan kan',
    'Ja, want jij bent gaaf'
]

geen_adt = [
    'Tuurlijk niet, kan jij helemaal niet',
    'Gast, doe normaal',
    'Nee je moet je weerstand op peil houden',
    'Nee, want corona',
    'Nee, maar de rest van de server wel!'
    'Nee!',
    'Nee alleen een slokje',
    'Nee, je hebt genoeg gehad voor vandaag',
    'Nee, drink maar water'
]

async def moetikadt(message):
    roll = random.randint(1, 100)
    if roll <= 50:
        zin = random.choice(je_moet_adt)
    else:
        zin = random.choice(geen_adt)

    await message.channel.send(zin)

async def check_beer_time(message):
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    vier = now.replace(hour=16, minute=0, second=0, microsecond=0)
    time_diff = vier - now

    if now.hour < 5:
        await message.channel.send('Nu mag je nog even lekker pilzen, maar niet te lang door gaan hoor')

    elif time_diff.seconds > 0 and now.hour > 16:
        await message.channel.send('Het is na vier, geniet lekker van je pilske')

    else:
        await message.channel.send('Het is nog geen tijd voor pils, nog {0} minutes wachten'.format(math.floor((time_diff.seconds/60))))

async def rock_paper_scissors(message):
    player1 = message.author
    channel = message.channel
    guild = message.guild
    

