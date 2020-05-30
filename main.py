
import discord
import ffmpy

from discord.ext import commands

bot = commands.Bot(command_prefix = 'niko ')

bot.load_extension('modules.General')
bot.load_extension('modules.CustomCommands')
bot.load_extension('modules.Help')

@bot.event
async def on_ready():
    print('Ni-ko BOT is online')


@bot.event
async def on_message(message):
    if 'human' in message.content:
        role = discord.utils.find(lambda r: r.name == "captha", message.guild.roles)
        if role in message.author.roles:
            await message.channel.set_permissions(message.author, read_messages=False)
            vc = message.guild.voice_client
            vc.play(discord.FFmpegPCMAudio('mantap.mp3'), after=lambda e: print('done'))
            embed = discord.Embed(title="📛WARNING", description="Captcha Protocol Activated", colour=0xf12323)
            bla = discord.File('D:\My Niko Project\warning.gif', filename='warning.gif')
            embed.set_image(url='attachment://warning.gif')
            await message.channel.send(file=bla, embed=embed)
    await bot.process_commands(message)

bot.run('NTA1NzI5NjA0OTU5MzM4NTE4.XsY36w.eS56mbrc2VojXY9fcQCkGguIE_0')
