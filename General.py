import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def credit(self, ctx):
        embed = discord.Embed(title="Credit", description="This bot was made by AQUA and [HNS] Athaerinium", colour=0x2a0b5a)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(title=f"{member.name}", colour=0x2a0b5a)
        embed.set_image(url='{}'.format(member.avatar_url))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))
