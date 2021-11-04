# Remember this is just simple setup!
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"{bot.user.name} Is ready.")


@bot.command()
async def hi(ctx):
    await ctx.send("Hi there!")


bot.run(
    "TOKEN"
)  # To get Bot Token, you need go to https://discord.com/developers/applications
