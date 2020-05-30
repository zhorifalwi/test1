import discord
from discord.ext import commands

class CustomCommads(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Special perms')
    async def join(self, ctx):
        if ctx.author.voice is None:
            embed = discord.Embed(title="Error", description="You are not connected to a voice channel", colour=0xf12323)
            await ctx.send(embed=embed)
        else:
            await ctx.author.voice.channel.connect()
            embed = discord.Embed(description="✅ | Ni-ko has Joined the Voice", colour=0x2a0b5a)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @join.error
    async def join_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Error", description="You have no permission to run this command", colour=0xf12323)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Special perms')
    async def stop(self, ctx):
        if ctx.author.voice.channel == ctx.guild.voice_client.channel:
            await ctx.guild.voice_client.disconnect()
            embed = discord.Embed(description="✅ | Ni-ko has Disconnected from voice", colour=0x2a0b5a)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error", description="you are not in the same voice channel as Ni-ko bot", colour=0xf12323)
            await ctx.send(embed=embed)

    @stop.error
    async def stop_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Error", description="You have no permission to run this command", colour=0xf12323)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Special perms')
    async def open(self, ctx):
        OwO = ctx.guild.get_member(408785106942164992)
        await ctx.message.channel.set_permissions(OwO, read_messages=True)
        embed = discord.Embed(description="✅ | OwO read perms has enabled", colour=0x2a0b5a)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @open.error
    async def open_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(title="Error", description="You have no permission to run this command", colour=0xf12323)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CustomCommads(bot))
