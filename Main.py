@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
	await ctx.channel.purge(limit=limit+1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)
	await ctx.message.delete()

@client.command(aliases=["help"])
async def commands(ctx):
  embed=discord.Embed(title="TheBogeyTwins Commands", url = "https://discord.gg/QVQm9H66fX", description="Prefix - ; \n \nHello - Says hello back to you \n \nGoodbye - Says bye back to you \n \nOwner - Gives the owners tag \n \nInvite - Gives the invite link to the bot \n \n Commands - Gives you the command list \n \nKick -  Kicks a member **Comming Soon** \n \nClear - deletes messages  \n \nAsk <@528803448175591425> for any help or any commands you would like!",
  color=discord.Color.purple())
  await ctx.message.delete()
  await ctx.author.send(embed=embed)
  await ctx.send(f'{ctx.author.mention}, Check your DMs!', delete_after=10)

client.run('')
