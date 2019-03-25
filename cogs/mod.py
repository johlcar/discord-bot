from discord.ext import commands

import discord


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Add mute timer and change permission to mute_members
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """ Mute server member.

        User and bot must have mute member permissions.
        """

        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if reason is None:
            reason = f'Action done by {ctx.author}(ID: {ctx.author.id})'

        await member.add_roles(role, reason=reason)
        await ctx.send(f':ok_hand:{member.name} has been muted.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        """ Unmute server member.

        User and bot must have mute member permissions.
        """

        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if reason is None:
            reason = f'Action done by {ctx.author}(ID: {ctx.author.id})'

        await member.remove_roles(role, reason=reason)
        await ctx.send(f':ok_hand:{member.name} has been unmuted.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a member from the server.

        User and bot must have kick member permissions.
        """

        if reason is None:
            reason = f'Action done by {ctx.author}(ID: {ctx.author.id})'

        await member.kick(reason=reason)
        await ctx.send(f':ok_hand:{member.name} has been kicked from the server... Too bad...')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.member, *, reason=None):
        """Bans a member from the server.

        User and bot must have ban member permissions
        """

        if reason is None:
            reason = f'Action done by {ctx.author}(ID: {ctx.author.id})'

        await member.ban(reason=reason)
        await ctx.send(f':ok_hand:{member.name} has been banned.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def softban(self, ctx, member: discord.member, *, reason=None):
        """Kick and remove messages from server.

        User must have kick member permission, and bot must have ban member permission.
        """

        if reason is None:
            reason = f'Action done by {ctx.author}(ID: {ctx.author.id})'

        await member.ban(reason=reason)
        await member.unban()
        await ctx.send(f':ok_hand:{member.name} has been soft banned.')

    # TODO Unban by member ID (See discord.py example).
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.member, *, reason=None):
        """Unbans a member from the server.

        User and bot must have ban member permissions.
        """

        if reason is None:
            reason = f'Action done by {ctx.author}(ID: {ctx.author.id})'

        await member.unban(reason=reason)
        await ctx.send(f':ok_hand:{member.name} has been unbanned.')

    # TODO Implement temporary ban (will require reminder timer).


def setup(bot):
    bot.add_cog(Mod(bot))
