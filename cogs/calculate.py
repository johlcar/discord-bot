from discord.ext import commands
from config import wolfram_token

import aiohttp
import urllib


class Calculate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def calc(self, ctx, query):
        """Query Wolfram short answer API.

        Query must be in quotes. 1 request per 30 seconds.
        """
        encoded_query = urllib.parse.urlencode({f'i': f'{query}'})

        url = f'https://api.wolframalpha.com/v1/result?{encoded_query}' \
            f'&appid={wolfram_token}'
        print(url)
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            content = await response.text()
        await ctx.send(content)

    @calc.error
    async def calc_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if ctx.message.author.guild_permissions.manage_roles:
                await ctx.reinvoke()
                return
            await ctx.send(error)


def setup(bot):
    bot.add_cog(Calculate(bot))
