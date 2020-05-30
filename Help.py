import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
            embed = discord.Embed(title="Commands Help", description="🔧***General*** \n``ping`` ``credit`` ``avatar`` \n\n✅***Custom Commands*** \n``join`` ``stop`` ``open`` \n\nFor more info on a specific command, \nuse ``niko help {command}``", colour=0x2a0b5a)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))
