import discord
from discord.ext import commands


class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(
                name=f"while Studying 📚",
            ),
        )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command used!")

    # Commands
    @commands.command()
    async def ping(self, ctx):
        """Check latency"""
        await ctx.send(f"Pong! ({round(self.bot.latency, 1)}ms)")


async def setup(bot):
    await bot.add_cog(Setup(bot))
