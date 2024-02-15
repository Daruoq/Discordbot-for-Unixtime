import os
import time

import discord
from dateutil import parser
from discord.ext import commands

from server import stay_alive

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents, case_insensitive=True)

respawn_times = {}  # Dictionary to store respawn times


def Respawn():
  current_timestamp = int(time.time())
  respawntime = current_timestamp + 12 * 60 * 60
  return respawntime


def parse_time(time_str):
  try:
    parsed_time = parser.parse(time_str)
    return int(parsed_time.timestamp()) + 12 * 60 * 60
  except ValueError:
    return None


@bot.command()
async def Morpheus(ctx, *args):
  if args:
    time_str = ' '.join(args)
    MorpheusRespawntime = parse_time(time_str)

    if MorpheusRespawntime is not None:
      respawn_times['Morpheus'] = MorpheusRespawntime
      discord_timestamp = f'<t:{MorpheusRespawntime}:f>'
      await ctx.send(f'Respawn (Morpheus): {discord_timestamp}')
    else:
      await ctx.send('Invalid time format. Please provide a valid time.')
  else:
    MorpheusRespawntime = Respawn()
    respawn_times['Morpheus'] = MorpheusRespawntime
    discord_timestamp = f'<t:{MorpheusRespawntime}:f>'
    await ctx.send(f'Respawn (Morpheus): {discord_timestamp}')


@bot.command()
async def Morph(ctx, *args):
  if args:
    time_str = ' '.join(args)
    MorpheusRespawntime = parse_time(time_str)

    if MorpheusRespawntime is not None:
      respawn_times['Morpheus'] = MorpheusRespawntime
      discord_timestamp = f'<t:{MorpheusRespawntime}:f>'
      await ctx.send(f'Respawn (Morpheus): {discord_timestamp}')
    else:
      await ctx.send('Invalid time format. Please provide a valid time.')
  else:
    MorpheusRespawntime = Respawn()
    respawn_times['Morpheus'] = MorpheusRespawntime
    discord_timestamp = f'<t:{MorpheusRespawntime}:f>'
    await ctx.send(f'Respawn (Morpheus): {discord_timestamp}')


@bot.command()
async def Rangora(ctx, *args):
  if args:
    time_str = ' '.join(args)
    RangoraRespawntime = parse_time(time_str)

    if RangoraRespawntime is not None:
      respawn_times['Rangora'] = RangoraRespawntime
      discord_timestamp = f'<t:{RangoraRespawntime}:f>'
      await ctx.send(f'Respawn (Rangora): {discord_timestamp}')
    else:
      await ctx.send('Invalid time format. Please provide a valid time.')
  else:
    RangoraRespawntime = Respawn()
    respawn_times['Rangora'] = RangoraRespawntime
    discord_timestamp = f'<t:{RangoraRespawntime}:f>'
    await ctx.send(f'Respawn (Rangora): {discord_timestamp}')


@bot.command()
async def Timers(ctx):
  RangoraRespawntime = respawn_times.get('Rangora', 'Not set')
  MorpheusRespawntime = respawn_times.get('Morpheus', 'Not set')

  await ctx.send('Rangora: ' + f'<t:{RangoraRespawntime}:f>' + '\n' +
                 'Morpheus: ' + f'<t:{MorpheusRespawntime}:f>')


@bot.command()
async def Reset(ctx):
  respawn_times.clear()
  await ctx.send('Respawn times cleared.')


@bot.command()
async def myhelp(ctx):
  await ctx.send(
      '**Commands:**\n' +
      '`Morpheus <time>` - Set the respawn time for Morpheus (e.g., `Morpheus 12:30`).\n'
      +
      '`Morph <time>` - Set the respawn time for Morph (e.g., `Morph 12:30`).\n'
      +
      '`Rangora <time>` - Set the respawn time for Rangora (e.g., `Rangora 16:00`).\n'
      + '`Timers` - Show the respawn times for Morpheus and Rangora.\n' +
      '`Reset` - Clear all respawn times.\n' +
      '`myhelp` - Show this help message.')



my_secret = os.getenv('Token')
stay_alive()
bot.run(my_secret)
