from discord.ext import commands

import config

description = '''Hello! I am a bot written by soup to provide various utilities.'''

initial_extensions = (
    'cogs.mod',
    'cogs.wolfram',
)

bot = commands.Bot(command_prefix='!', description=description)

for extension in initial_extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


bot.run(config.discord_token)