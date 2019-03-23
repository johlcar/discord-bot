# import discord
# from discord.ext import commands
# from urllib.parse import urlencode
# import random
# import aiohttp

# import secrets

# # Retrieve query results from Wolfram Short Answer API
# @bot.command(aliases=['eval'])
# async def wolfram(*query):
#     url = ('https://api.wolframalpha.com/v1/result?{}%3f'
#            '&appid={}'.format(urlencode({'i': ' '.join(query)}), secrets.wolfram_id))
#     async with aiohttp.ClientSession() as session:
#         response = await session.get(url)
#         content = await response.read()
#     await bot.say(content)

# # Search Python3 Docs
# @bot.command(aliases=['pyh'])
# async def py_help(*query):
#     url = ('https://docs.python.org/3/search.html?{}'
#            '&check_keywords=yes&area=default'.format(urlencode({'q': ' '.join(query)})))
#     await bot.say(url)