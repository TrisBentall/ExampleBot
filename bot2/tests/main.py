import discord

client = discord.Bot(debug_guilds=[SERVER_ID])

@client.event
async def on_ready():
    print(f"{client.user} is online | Watching {len(client.guilds)} servers")

@client.slash_command(description="Say Hello")
async def hi(ctx):
    await ctx.respond(f"Hello {ctx.author.name}!", ephemeral=True)

client.run("TOKEN")