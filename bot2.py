import discord
from discord.ext import commands

client=commands.Bot(command_prefix="~")

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.command()
async def hello(ctx):
	await ctx.channel.send(f"Hello! {ctx.author.name}")

@client.command()
async def poll(ctx,title=None,question=None,*options):
	if len(options) > 10:
		await ctx.send(':no_entry: You can only have atmost **10 options**!')

	if question == None and title != None:
		await ctx.send("Please give a question!")

	if len(options) <= 10 and question is not None:

		reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

		for x, option in enumerate(options):
			question += '\n\n {} {}'.format(reactions[x], option)

		emb=discord.Embed(title=f"{title}",description=f"{question}",colour=discord.Colour.random())          #0xFF0000

		# emb.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)

		# emb.set_thumbnail(url=f'https://cdn.discordapp.com/icons/{ctx.message.guild.id}/{ctx.message.guild.icon}.png')

		# emb.timestamp=ctx.message.created_at

		msg = await ctx.send(embed=emb)

		for reaction in reactions[:len(options)]:
			await msg.add_reaction(reaction)

		

	if len(options) == 0 and title == None and question == None:
		await ctx.send("Please enter the title of the poll followed by the question. Then give your options.\nFor example, ```~poll \"title\" \"question\" \"option1\" \"option2\"```")

	if len(options) == 0 and question != None and title != None:
		await msg.add_reaction('👍')
		await msg.add_reaction('👎')

client.run('ODQ3ODU5NTg1MDU4NjAzMDU4.YLEMxQ.Srf-MAeeCiBh-nKfSXbRN_Q6OEk')
