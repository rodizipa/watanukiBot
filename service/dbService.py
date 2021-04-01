class DatabaseService:
    """Basic database manipulations for abstractions"""
    def __init__(self, bot):
        self.bot = bot

    connection = None

    async def getconnection(self):
        """Get connection with database"""
        self.connection = await self.bot.db.acquire()

    async def releaseconnection(self):
        """Remove connection to database"""
        await self.bot.db.release(self.connection)

    async def execute(self, sql, *args, **kwargs):
        """Execute query and arguments passed"""
        await self.getconnection()
        async with self.connection.transaction():
            await self.bot.db.execute(sql, *args, **kwargs)
        await self.releaseconnection()

    async def fetchrow(self, sql, *args, **kwargs):
        return await self.bot.db.fetchrow(sql, *args, **kwargs)

    async def fetch(self, sql, *args, **kwargs):
        return await self.bot.db.fetch(sql, *args, **kwargs)
