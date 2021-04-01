from service.dbService import DatabaseService
import discord


class GuildService(DatabaseService):
    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot

    async def add_guild(self, guild: discord.Guild):
        await self.execute("insert into guild(guild_id, guild_name) VALUES ($1, $2)",
                           guild.id, guild.name)

    async def check_guild(self, guild_id):
        guild = await self.fetchrow("select * from guild where guild_id = $1", guild_id)
        return guild is not None

    async def get_active_guilds(self):
        return await self.fetch("select * from guild where event_online = true")

    async def update_time(self, guild_id, time):
        return await self.execute("update guild set next_update = $1 where guild_id = $2", time, guild_id)

    async def update_guild_online(self, guild_id, value: bool):
        await self.execute("update guild set event_online = $1 where guild_id = $2", value, guild_id)
