import discord
import random
from discord.ext import commands

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
async def Jos(ctx):
    await ctx.send(f'Stop {round(client.latency * 1000)}ms')


@client.command(opties=['hoe', 'test'])
async def gevoelens(ctx, *, vraag):
    antwoorden = ['Het ging eigenlijk best wel goed totdat jij in deze server kwam.',
                  'Boeie',
                  'Ik verdoe mijn tijd niet aan mensen die microsoft teams gebruiken.',
                  'Wat nou als je een keertje wegloopt van dat toetsenbordje en nooit meer terug komt?,'
                  'Nou eigenlijk, best wel wauw.',
                  'Het gaat helemaal super! Ik wordt totaal niet gedwongen door code om dit te zeggen!']
    await ctx.send(f'Vraag: {vraag}\nAntwoord: {random.choice(antwoorden)}')

client.run('ODQ0OTA4Mzg1MTQ0MTQzOTAz.YKZQQA.qnXmNJocbyVMjHtsish1itNS1PA')