from discord.ext import commands

import config

description = '''Hello! I am a bot written by soup to provide discord server management and various utilities.'''

bot = commands.Bot(command_prefix='!', description=description)

bot.load_extension("cogs.mod")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(config.discord_token)