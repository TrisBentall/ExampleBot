import discord
from discord.ext import commands

PREFIX = "!"

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! - {round(client.latency*1000)}ms')

TOKEN = "Your Bots Token Goes Here"
client.run(TOKEN)