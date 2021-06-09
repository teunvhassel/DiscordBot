import discord
import random
from discord.ext import commands
import urllib.parse, urllib.request, re
import aiohttp
import asyncio
import os

# API key wordt opgehaald vanuit een environment variable
bot_jos = os.environ.get('bot_jos')

# Met de variabele "client" maak ik het voor mezelf gemakkelijker om de bot op te roepen
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Jos komt binnen via de achterdeur...')

@client.event
async def on_member_join(member):
    print(f'{member} is binnen gekomen via de voordeur...')

@client.event
async def on_member_remove(member):
    print(f'{member} is weggejaagd van de server... mag ik een F in de chat?')



# Maak een commando aan
@client.command()
async def jos(ctx):
    await ctx.send(f'Stop {round(client.latency * 1000)}ms')

# Vraag aan Jos hoe het gaat
@client.command(opties=['hoe gaat het', 'test'])
async def gevoelens(ctx, *, vraag):
    antwoorden = ['Het ging eigenlijk best wel goed totdat jij in deze server kwam.',
                  'Boeie',
                  'Ik verdoe mijn tijd niet aan mensen die microsoft teams gebruiken.',
                  'Wat nou als je een keertje wegloopt van dat toetsenbordje en nooit meer terug komt?',
                  'Nou eigenlijk, best wel wauw.',
                  'Het gaat helemaal super! Ik wordt totaal niet gedwongen door code om dit te zeggen!']
    await ctx.send(f'Vraag: {vraag}\nAntwoord: {random.choice(antwoorden)}')


# Haal een video van YouTube op
@client.command()
async def youtube(ctx, *, search):
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    html_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0]) # als je het getal van de list verhoogt krijg je meer zoekresultaten, 0 = 1 resultaat


client.run(bot_jos)
