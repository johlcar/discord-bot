from discord.ext import commands
from config import wolfram_token

import wolframalpha


class Wolfram(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = wolframalpha.Client(wolfram_token)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def wolf(self, ctx, query):
        """Return only result of a Wolfram query.

        Query must be in quotes. 1 request per 30 seconds.
        """
        res = self.client.query(query)

        await ctx.send(next(res.results).text)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def wolf_full(self, ctx, query):
        """Return full result of a Wolfram query except images.

        Query must be in quotes. 1 request per 30 seconds.
        """
        res = self.client.query(query)

        for pod in res.pods:
            if pod.text:
                await ctx.send("**" + pod.title + ":**\n" + "`" + pod.text + "`")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def wolfg(self, ctx, query):
        """Return only the plot result of a Wolfram query.

        Query must be in quotes. 1 request per 30 seconds.
        """
        res = self.client.query(query)

        for pod in res.pods:
            for sub in pod.subpods:
                if pod.title == 'Plot':
                    printmap = list(map(str,sub.img))
                    print(printmap)
                    await ctx.send("**Result" + ":**\n" + "`" + list(sub.img)[0] + "`")

    @wolf.error
    @wolf_full.error
    @wolfg.error
    async def wolf_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if ctx.message.author.guild_permissions.manage_roles:
                await ctx.reinvoke()
                return
            await ctx.send(error)

def setup(bot):
    bot.add_cog(Wolfram(bot))
