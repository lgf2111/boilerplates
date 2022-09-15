from discord.ext import commands
from replit import db


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guilds, id = db["guilds"], str(guild.id)
        guilds[id] = {"prefix": "."}
        db["guilds"] = guilds

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        guilds, id = db["guilds"], str(guild.id)
        del guilds[id]
        db["guilds"] = guilds

    # Commands
    @commands.command()
    async def chpf(self, ctx, new_pfx):
        """Change prefix"""
        id = str(ctx.guild.id)
        guild = db["guilds"][id]
        old_pfx = guild["prefix"]
        guild["prefix"] = new_pfx
        db["guilds"][id] = guild
        await ctx.send(f"Prefix changed from {old_pfx} to {new_pfx}")

    @commands.command()
    async def crpf(self, ctx):
        """Current prefix"""
        id = str(ctx.guild.id)
        guild = db["guilds"][id]
        pfx = guild["prefix"]
        await ctx.send(
            f"Current prefix is {pfx} (You're literally using it right now...LOL)"
        )


async def setup(bot):
    await bot.add_cog(Prefix(bot))
