import asyncio
import logging
import discord
import asyncpg
import pendulum
from helpers.datetimeutil import pendulum_to_datetime
from discord.ext import commands

import CONFIG

from service import memberService, guildService

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.presences = False

cogs = ['cogs.primeiroAbril']


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=CONFIG.PREFIX, description="Primeiro de Abril", intents=intents)
        self.__db = kwargs.pop("db")
        self.__memberService = memberService.MemberService(self)
        self.__guildService = guildService.GuildService(self)
        self.__rt = self.loop.create_task(self.reset_task())

    async def get_april_cog(self):
        return self.get_cog("PrimeiroAbrilCog")

    async def reset_task(self):
        await self.wait_until_ready()
        while not self.is_closed():
            now = pendulum.now()
            for guild in await self.guildservice.get_active_guilds():
                if guild['next_update'] and now > pendulum.instance(guild['next_update']):
                    april_cog = await self.get_april_cog()
                    await april_cog.watanuki_primeiro_de_abril(guild=self.get_guild(guild['guild_id']))
                    await self.guildservice.update_time(guild['guild_id'], pendulum_to_datetime(
                        pendulum.now().add(CONFIG.TIME_INCREMENT_IN_MINUTES)))
            await asyncio.sleep(60)

    @property
    def db(self):
        return self.__db

    @property
    def memberservice(self):
        return self.__memberService

    @property
    def guildservice(self):
        return self.__guildService

    async def on_ready(self):
        print("Watanuki pronto para trolar!\n")

    async def load_modules(self):
        for cog in cogs:
            self.load_extension(cog)

    async def on_message(self, message):
        try:
            await self.process_commands(message)
        except discord.DiscordException as discord_ex:
            print("Erro de comando. Verifique o log.\n")
            logging.error(discord_ex.__name__, discord_ex)

    async def on_member_join(self, member):
        cog_april = await self.get_april_cog()
        if cog_april:
            await cog_april.on_join_or_nick_update(cog_april, member)

    # Todo: Também verificar evento de entrada no servidor e talvez executar a cada X min


async def run():
    pg_credentials = {"user": CONFIG.USERNAME, "password": CONFIG.PASSWORD, "database": CONFIG.DATABASE,
                      "host": CONFIG.HOST}
    async with asyncpg.create_pool(**pg_credentials) as db:
        bot = Bot(db=db)
        try:
            bot.remove_command("help")
            await bot.load_modules()
            await bot.start(CONFIG.TOKEN)
        except KeyboardInterrupt:
            await bot.logout()


if __name__ == '__main__':
    print('Iniciando o bot\n')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    except Exception as ex:
        logging.error(ex.__name__)
