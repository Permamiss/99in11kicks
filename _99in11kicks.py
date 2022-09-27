# don't tell Adan I reused the Cube bot code for this
# Adan if you're reading this no you aren't

import os
import discord
from discord.ext import commands
#import random
#import asyncio # used for sleeping

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN_TWO")
print(f"Token is {TOKEN}")

intents = discord.Intents.default()
intents.message_content = True
#intents.members = True # enable if you are printing IDs of members of a server

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
	print(f"Bot {bot.user} is ready to work!")
	

	# debug to get channel names & IDs
	'''
	for guild in bot.guilds:
		print(f"ServerName {guild.name} | ServerID {guild.id}")
		print(" - ChannelName | ChannelID")
		for channel in guild.text_channels:
			print(f" - {channel.name} | {channel.id}")
	'''
	# debug to get user names & IDs
	'''
	for guild in bot.guilds:
		print(f"ServerName {guild.name} | ServerID {guild.id}")
		print(" - PlayerName | PlayerID")
		for member in guild.members:
			print(f" - {member.nick or member.name} | {member.id}")
	'''

'''
@bot.command(name = "join", help = "Joins the voice channel")
async def join(context : commands.Context):
	channel = context.author.voice.channel
	await channel.connect()

@bot.command(name = "leave", help = "Leaves the voice channel")
async def leave(context : commands.Context):
	if context.voice_client:
		await context.voice_client.disconnect()
'''

@bot.event
async def on_message(message : discord.Message):
	sender = message.author

	if sender.bot: # ignore message if it comes from a bot
		return

	#content = message.content.lower()
	content = message.content

	print(f"Message received from {sender}")

	if "k238XpMMn38" in content:
		print("Kicking user for posting illegal dead bit.")
		await message.reply(f"Kicked user {sender.nick or sender.name} for posting a dead bit.")
		await sender.kick(reason="You posted a dead bit. Kill yourself.")

	await bot.process_commands(message) # always keep this line of code at the bottom of this method so that commands can be processed properly

@bot.event
async def on_message_edit(message : discord.Message):
	on_message(message)


bot.run(TOKEN)