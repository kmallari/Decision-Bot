from discord.ext import commands
import discord
import os
import random

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

@bot.command()
async def roll(ctx, *args):
  if len(args) == 1 and is_number(args[0]):
    await ctx.channel.send(f'Choosing a number from 1 to {args[0]}')
    await ctx.channel.send(f'The number is: {random.randint(1, int(args[0]))}')
  elif len(args) == 2 and is_number(args[0]) and is_number(args[1]):
    await ctx.channel.send(f'Choosing a number from {args[0] if args[0] > args[1] else args[1]} and {args[0] if args[0] < args[1] else args[1]} ')
    await ctx.channel.send(f'The number is: {random.randint(int(args[0]), int(args[1]))}')
  elif args[0] == "coinflip":
    await ctx.channel.send(f'Flipping a coin...')
    await ctx.channel.send(f'The coin shows... {"heads" if random.randint(0,1) == 1 else "tails"}')
  elif len(args) == 2 and args[0] == "dice" and is_number(args[1]):
    await ctx.channel.send(f'Rolling a {args[1]} sided dice...')
    await ctx.channel.send(f'The dice rolled: {random.randint(1, int(args[1]))}')
  elif len(args) > 2 and args[0] == "dice" and is_number(args[1]) and is_number(args[2]): 
    await ctx.channel.send(f'Rolling a {args[1]}-sided dice {args[2]} times')
    dice_value_arr = []
    for i in range(int(args[2])):
      dice_value_arr.append(f'``{random.randint(1,int(args[1]))}/{args[1]}``')
    dice_value_str = " | ".join(dice_value_arr)
    await ctx.channel.send(f'The dice rolled: {dice_value_str}')
  elif args[0] == "dice":
    await ctx.channel.send(f'Rolling a 6 sided dice...')
    await ctx.channel.send(f'The dice rolled: {random.randint(1, 6)}')
  else:
    await ctx.channel.send(f'Choosing from your list...')
    await ctx.channel.send(f'I chose: {random.choice(args)}')

bot.run(os.getenv('TOKEN'))