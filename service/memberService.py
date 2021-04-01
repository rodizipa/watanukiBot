from service.dbService import DatabaseService
import discord


class MemberService(DatabaseService):
    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot

    async def add_member(self, member: discord.Member, guild_id):
        await self.execute("insert into member(member_id, display_name, guild_id) VALUES ($1, $2, $3)",
                           member.id, member.display_name, guild_id)

    async def get_member(self, member_id):
        return await self.fetchrow("select * from member where member_id = $1", member_id)

    async def get_all_members(self, guild_id):
        return await self.fetch("SELECT * from member where guild_id = $1", guild_id)
