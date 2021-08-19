from discord.ext import commands
import discord
import os
import random
import time

# bot and client startup
client = discord.Client()
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="~", intents=intents, help_command=None)

@bot.event
async def on_ready():
  print(f"Bot is ready")
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="decision making."))

# function for determining whether to roll a number
def is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    pass

  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass

  return False

# <:PauseChamp:877817523121295420>

delay = 1.5

@bot.command()
async def rng(ctx, *args):
  # number from 1 to X
  if len(args) == 1 and is_number(args[0]):
    embed=discord.Embed(title=f"<:PauseChamp:877817523121295420> Generating a number...", description=f"A number between 1 and {args[0]} is being generated.", color=0x7652fa)
    await ctx.channel.send(embed=embed)
    time.sleep(delay)
    embed.add_field(name="The number generated is", value=f"`{random.randint(1, int(args[0]))}`", inline=False)
    await ctx.channel.send(embed=embed)

  # number from X to X
  elif len(args) == 2 and is_number(args[0]) and is_number(args[1]):    
    embed=discord.Embed(title=f"<:PauseChamp:877817523121295420> Generating a number...", description=f"A number between {args[0] if args[0] > args[1] else args[1]} and {args[0] if args[0] < args[1] else args[1]} is being generated", color=0x7652fa)
    await ctx.channel.send(embed=embed)
    time.sleep(delay)
    embed.add_field(name="The number generated is", value=f"`{random.randint(int(args[0] if args[0] > args[1] else args[1]), int(args[0] if args[0] < args[1] else args[1]))}`", inline=False)
    await ctx.channel.send(embed=embed)    

@bot.command()
async def flip(ctx):
  embed=discord.Embed(title=f"<:PauseChamp:877817523121295420> Flipping a coin...", description=f"The result will either be heads or tails.", color=0x7652fa)
  await ctx.channel.send(embed=embed)
  time.sleep(delay)
  result = random.randint(0, 1)
  embed.add_field(name="The coin flipped:", value=f"", inline=False)
  if result == 1:
    embed.set_image(url="https://i.imgur.com/rAhnfvC.png")
  else:
    embed.set_image(url="https://i.imgur.com/7NJsYAB.png")
  embed.set_field_at(index=0, name="The coin flipped: ", value=f"{'***Heads!***' if result == 1 else '***Tails!***'}", inline=False)
  await ctx.channel.send(embed=embed)

# multisided dice, X amount of times
@bot.command()
async def roll(ctx, sides, num_of_rolls):
  embed=discord.Embed(title=f"<:PauseChamp:877817523121295420> Rolling a {sides}-sided dice", description=f"{num_of_rolls} times.", color=0x7652fa)
  time.sleep(delay)
  dice_value_arr = []
  for i in range(int(num_of_rolls)):
    dice_value_arr.append(f'``{random.randint(1,int(sides))}/{sides}``')
  dice_value_str = " | ".join(dice_value_arr)
  await ctx.channel.send(embed=embed)
  embed.add_field(name="The result/s of the dice is/are: ", value=f"{dice_value_str}", inline=False)
  await ctx.channel.send(embed=embed)

@bot.command()
async def list(ctx, *args):
  # await ctx.channel.send(f'Choosing from your list...')
  # await ctx.channel.send(f'I chose: {random.choice(args)}')
  list_str = ", ".join(args)
  embed=discord.Embed(title=f"<:PauseChamp:877817523121295420> Choosing from your list...", description=f"Choosing from {list_str}", color=0x7652fa)
  await ctx.channel.send(embed=embed)
  time.sleep(delay)
  embed.add_field(name="I have chosen: ", value=f"`{random.choice(args)}`", inline=False)
  await ctx.channel.send(embed=embed)

bot.run(os.getenv('TOKEN'))