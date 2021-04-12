from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [775227458596372502]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
    def run(self, version):
        self.VERSION = version
        
        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        
            print("running bot...")
            super().run(self.TOKEN, reconnect=True)
            
    async def on_connect(self):
        print("Bot Connected")

    async def on_disconnect(self):
        print("Bot Disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(793373417142616125)
            print("Bot Ready")

            channel = self.get_channel(828831972415504414)
            await channel.send("Now Online")

            embed = Embed(title="Now Online!", description="Bot is now online")
            fields = [("Name", "Value", True),
                      ("Another field", "This field is next to the other one.", True),
                      ("A non-inline field", "This field will appear on it's own row", False)]
            for name, value, inline in fields:
                embed.add_field(name="Name", value="Value", inline=inline)
            await channel.send(embed=embed)

        else:
            print("Bot Reconnected")

    async def on_message(self, message):
        pass

bot = Bot()