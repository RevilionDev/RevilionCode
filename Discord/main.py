# Remember this is just simple setup!
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())


@bot.command()
async def hi(ctx):
    await ctx.send("Hi there!")


bot.run(
    "TOKEN"
)  # To get Bot Token, you need go to https://discord.com/developers/applications
