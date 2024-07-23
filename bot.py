import discord
from discord.ext import commands

import config


class RaidedBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        await self.load_cogs()
        await self.tree.sync()

    async def load_cogs(self) -> None:
        for cog_file in config.COGS_DIR.glob("*.py"):
            if cog_file.name != "__init__.py":
                cog: str = f"{config.COGS_DIR.relative_to(config.BASE_DIR)}.{cog_file.name.removesuffix('.py')}"

                await self.load_extension(cog)

                print(f"[+] Loaded {cog}")

    async def on_ready(self):
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/help"))

        print(f"\n[+] Logged in as {self.user}\n")

        print(f"Connected to {len(self.guilds)} server(s):")
        for guild in self.guilds:
            print(f"- {guild.name} ({guild.id}): {guild.member_count} members")


def main():
    bot = RaidedBot(command_prefix=config.PREFIX, intents=config.INTENTS)
    bot.run(config.TOKEN)


if __name__ == "__main__":
    main()
