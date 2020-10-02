import discord
from discord.ext import commands
import datetime
import time

from urllib import parse, request
import re
import asyncio
client = discord.Client()

bot = commands.Bot(command_prefix='>', description="Eau Fraiche")


@bot.event
async def on_ready():
    print("Prete a trouvé le One Piece!")

@bot.command()
async def weshaurele(ctx):
    await ctx.send('Salamalekoum frère')

@bot.command()
async def info(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
	await ctx.send(message)

@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def reduc(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne - numTwo)

@bot.command()
async def propa(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne * numTwo)

@bot.command()
async def div(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne / numTwo)

@bot.command()
async def clear(ctx, nombre : int):
  number = nombre
  await ctx.channel.purge(limit = nombre + 1)
  await ctx.send(f"J'ai effacé {nombre} messages!")
  time.sleep(5)
  await ctx.channel.purge(limit = 1)

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} est un enculé.\n https://tenor.com/view/tban-ban-bigflo-oli-bigflo-et-oli-gif-17515232")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} est un énorme connard parce qu'il a : {reason}.\n https://tenor.com/view/tban-ban-bigflo-oli-bigflo-et-oli-gif-17515232")

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été revive.\n https://tenor.com/view/zombie-hand-grave-rise-raiseyourhand-gif-4519606")
			return
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans du con")

@bot.command()
async def sondage(ctx):
	await ctx.send("Quel est ton sondage?")

	def checkMessage(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	try:
		recette = await bot.wait_for("message", timeout = 60, check = checkMessage)
	except:
		await ctx.send("Tu mets trop de temps FDP")
		return
	message = await ctx.send(f"{recette.content}. Réagis avec ✅ ou ❌")
	await message.add_reaction("✅")
	await message.add_reaction("❌")


	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

@bot.command()
async def fch(ctx):
	await ctx.send("https://discord.gg/awYZnJq")

@bot.command()
async def commande(ctx):
	await ctx.send("Bot Crée par <@587949567123914754> \n>weshaurele = inutile \n>info = info du serveur \n>fch = invitation du FC HOMME \n>clear ton nombre = effacer messages \n>kick @... raison = exclure\n>ban @... raison = ban\n>unban ...#...= deban \n>sum 1 1 = addition \n>reduc 1 1 = réduction \n>propa 1 1 = multiplication \n>div 1 1 = division \n>say ... = répete ...")

@bot.command()
async def le_conseil(ctx):
	user = "<@587949567123914754> <@526176908447318026> <@403154354485460993>"
	await ctx.send(f"{user}")


bot.run("NzMyOTM4MTM2NDAwOTUzMzk0.XxHkbQ.kd-n1Itl9P5akdhj1X7NJ-letpU")