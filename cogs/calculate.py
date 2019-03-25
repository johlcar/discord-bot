from discord.ext import commands
from config import wolfram_token

import aiohttp
import urllib


class Calculate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def math(self, ctx, expression):
        """Query Wolfram API.

        Query must be in quotes.
        """
        url = ('https://api.wolframalpha.com/v1/result?{}%3f'
               '&appid={}'.format(urllib.parse.urlencode({'i': ' '.join(expression)}), wolfram_token))
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            content = await response.read()
        await ctx.send(content)


def setup(bot):
    bot.add_cog(Calculate(bot))
