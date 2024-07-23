import discord
from discord import app_commands
from discord.ext import commands


# For further documentation, refer to https://discordpy.readthedocs.io/en/latest


class ExampleCog(commands.Cog, name="example"):
    """
    Example commands.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    #
    #  - [ Individual Commands ] -
    #

    @app_commands.command(name="hello", description="Replies with `Hello World!`")
    async def hello(self, interaction: discord.Interaction):
        """
        Replies with `Hello World!` in a hidden message.
        """

        await interaction.response.send_message("Hello Wold!", ephemeral=True)

    #
    # - [ Group Commands ] -
    #

    group = app_commands.Group(name="msg", description="/msg commands")

    @group.command(name="ping", description="/msg ping [msg_text]")
    @app_commands.describe(msg_text="The text to use in the response")
    async def msg_ping(self, interaction: discord.Interaction, msg_text: str):
        """
        Replies to `user` with `msg_text`.
        """

        user: discord.Member = interaction.user

        await interaction.response.send_message(
            f"Pong {user.mention}. Your message was: {msg_text}", ephemeral=True
        )

    @group.command(name="example", description="/msg example")
    async def msg_example(self, interaction: discord.Interaction):
        """
        Sends a public message to the channel where the command was run.
        """

        await interaction.channel.send(f"Example message")


async def setup(bot: commands.Bot):
    await bot.add_cog(ExampleCog(bot))
