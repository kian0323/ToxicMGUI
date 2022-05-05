import discord
import requests
from discord.ext import commands
from discord import file
from discord.utils import get
import os

client = commands.Bot(command_prefix=';')

@client.command()
@commands.has_role("Owner")
async def generate(ctx, user: discord.User):
    
    disc = user.id
    
    url = requests.get(f"Website_Link/generate.php?disc={disc}")
    
    generate = url.text
    
    if generate == 'User Already Has A Key!':
        message = (f"**{user}** Already Has A Key!")
        embedVar = discord.Embed(title=message, color=0xFF0000)
        await ctx.reply(f"**<@{disc}> Already Has A Key!**")
    else:
        await ctx.reply("**Success!**")
        await ctx.reply(f"**<@{disc}>, A Generated Token Has Been Sent To Your DM's!***")
        await ctx.author.send(f"**{user}'s Token: {generate}**")
        await user.send(f"**Here's Your Token!** ```\n{generate}```")
        
        
@client.command()
@commands.has_role("Owner")
async def delete(ctx, user: discord.User):
    
    disc = user.id
    
    url = requests.get(f"Website_Link/delete.php?disc={disc}")
    
    generate = url.text
    
    if generate == 'User Not Found':
        await ctx.reply(f"**<@{disc}> Is Not Listed In DB!")
    else:
        await user.send(f"**An Admin Deleted Your Token!**")
        await ctx.reply(f"**<@{disc}>'s Token Has Ben Successfully Deleted!**")
        

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('@ YuvalServices'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message = (f"Please Mention A User!")
        embedVar = discord.Embed(title=message, color=0xFF0000)
        await ctx.channel.send(embed=embedVar)
    elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        message = (f"You Don't Have The Permission To Use This!")
        embedVar = discord.Embed(title=message, color=0xFF0000)
        await ctx.channel.send(embed=embedVar)
    elif isinstance(error, commands.CommandNotFound):
        message = (f"Command Not Found!")
        embedVar = discord.Embed(title=message, color=0xFF0000)
        await ctx.channel.send(embed=embedVar)
       
client.run(os.environ['token'])
