import discord
import asyncio
import pendulum
from CONFIG import TIME_INCREMENT_IN_MINUTES
from helpers.datetimeutil import pendulum_to_datetime
from asyncpg.exceptions import UniqueViolationError
from discord.ext import commands
import random

nicks = [
    "Aeronauta Barata",
    "Agrícola Beterraba Areia",
    "Agrícola da Terra Fonseca",
    "Alce Barbuda",
    "Amado Amoroso",
    "Amável Pinto",
    "Amazonas Rio do Brasil Pimpão",
    "América do Sul Brasil de Santana",
    "Amin Amou Amado",
    "Antonio Manso Pacífico de Oliveira Sossegado",
    "Antônio Morrendo das Dores",
    "Asteróide Silverio",
    "Bandeirante do Brasil Paulistano",
    "Barrigudinha Seleida",
    "Bispo de Paris",
    "Céu Azul do Sol Poente",
    "Chevrolet da Silva Ford",
    "Dezêncio Feverêncio de Oitenta e Cinco",
    "Dolores Fuertes de Barriga",
    "Esparadrapo Clemente de Sá",
    "Homem Bom da Cunha Souto Maior",
    "Ilegível Inilegível",
    "Inocêncio Coitadinho",
    "Janeiro Fevereiro de Março Abril",
    "Lança Perfume Rodometálico de Andrade",
    "Marciano Verdinho das Antenas Longas",
    "Maria Privada de Jesus",
    "Maria Tributina Prostituta Cataerva",
    "Maria-você-me-mata",
    "Mimaré Índio Brazileiro de Campos",
    "Dra Pirilau",
    "XanaCarnivora",
    "Dapra20comer",
    "Tatycomendo",
    "Uhpapaichegou",
    "Rasgacu",
    "Cruizcredo",
    "Flamengolol",
    "Lord fralda",
    "SeuVagem",
    "Avestruz que te seduz",
    "Melado de óleo",
    "Comi quem leu",
    "Beijosmeliga",
    "Headshot grátis",
    "Estou sem munição",
    "Olha o passarinho",
    "Cavalo amigável",
    "Morreu antes de ler",
    "SemNome",
    "RecebiSpam",
    "Kharne Greylhada",
    "Boleto Vazio",
    "Capa Nera",
    "BatataSozinha",
    "FeraSokeRuim",
    "Amortyzador",
    "Parcyal Mente",
    "VlogImundo",
    "After Eita",
    "Erro 504",
    "PuleiMorri",
    "iRuim 2.0",
    "LaggandoD+",
    "MeusProbrema",
    "NickO Riginal",
    "ArsenalFunkeiro",
    "Rato Atomico",
    "Bispo Pelado",
    "Pablo Escovando",
    "Byata R3zando",
    "Cabo Nero",
    "Bruxopolis",
    "Ze Morteiro",
    "Juan Casavelha",
    "Sayan Casual",
    "Cherno Borg",
    "Rick Jaimes",
    "Tirona Lapela",
    "JovemMistico",
    "Urso Vago",
    "MonkeeFeice",
    "Major Morte",
    "Tone Yorke",
    "Fredo Mercurio",
    "Davyd Boyeae",
    "Ivete Comgalo",
    "Eilish Rijinha",
    "Atom Jobine",
    "Ze Aberration",
    "Sou1abismo",
    "Adaptoide",
    "DiegoDanger",
    "Dildo Baggins",
    "Riddickulo",
    "Vinho Diezel",
    "Johnson Alcibíades",
    "xXRodolf HitterXx",
    "Mário do Armário",
    "8============D",
    "Vem Virar Pó",
    "Aaaaaaaaatirei",
    "Morreu ————>",
    "Headshot gratis",
    "Highlander",
    "Tomi_li_jones",
    "Seu Vagem",
    "Tiriva Assissina",
    "Sou do seu time",
    "Atire aqui",
    "Lhama que te ama",
    "mewtwo matou um cara",
    "Rolando Escada Abaixo",
    "mataloene",
    "Matador de frangos",
    "Estado avançado de decomposição",
    "MATADOR DE VÉIOS",
    "Padre Marcelo r0x",
    "Mario dos Santos",
    "matacachorrone",
    "Lord Bumbumole",
    "super saia jeans",
    "Mata_eu",
    "Não chuta a criança",
    "Boi do saco roxo",
    "ainda temos doritos",
    "Mew são Impossível",
    "Dark William Bonner",
    "Velha Cega",
    "Oddishéia no Espaço",
    "Leite de Macaca",
    "eu odeio minha locadora",
    "Varinha de cutucar estrela",
    "Bastardo_de_nove_dedos",
    "beque de fazenda",
    "Marta Leone",
    "Chuck Morris ou não morris?",
    "Atras de você",
    "bauser o feros",
    "sonic the hotdog",
    "Lambari de Botas",
    "Beijosmeliga",
    "NO_NICK",
    "The_Phunto",
    "Me mira mas me erra",
    "Doutor Ted Explica",
    "Júpiter é legal pow",
    "Peida na lancheira",
    "Amigo Tampinha",
    "tonho laranjão",
    "Pamonha de Piracicaba",
    "Iron Madein China",
    "Monoteta",
    "ME-largepenis",
    "Paul Steel de paul me too",
    "Móveis Coloniais de Acajú",
    "Alvo preferencial",
    "xerudilimao",
    "Sete rolas de arame farpado",
    "Avestruz que te seduz",
    "Maryon",
    "Jesus faz backup",
    "CaRa CoM nAmOrAda",
    "MATALEOPARDONE",
    "uruBlue",
    "H ROMEU PINTO",
    "Samantha RaioLaser",
    "matatigrone",
    "Alt of Ctrl",
    "JOHN LOCKE DAS DORGAS",
    "Osmose Osbourne",
    "rato velho vira morcego",
    "Unicórnio com Audácia",
    "Morreu antes de ler isso tudo",
    "Elefantinhu Rosinha~*",
    "melado de oleo",
    "denunciado por preconceito",
    "Passarinho da floresta",
    "Hipopotamo Roxo do Mal",
    "Estou sem munição",
    "eretus hasvezs",
    "O Cabrito Faz Mééé",
    "Silvio Saint",
    "paula tejano",
    "MACAXEIRA ASSASSINA",
    "Banido da luz vermelha",
    "Olha o passarinho",
    "Pardal da Jamaica",
    "papai quero um minhoco",
    "baleia doida que explode",
    "YETESABIO",
    "Cavalo amigável 25cm",
    "Igby e os Triceratops",
    "Tetas de Mel",
    "Sylvester estalonge",
    "Viking Vaporub",
    "Tainha frita",
    "Catetas",
    "COMI QUEM LÊU",
    "Boi Banido",
    "robocop de aluminio",
    "Padaria Nayara",
    "I can’t dace forró",
    "Dark Receber",
    "Jacaré do zoologico",
    "Aguinaldo mão de esterco",
    "Macarrão Instantâneo",
    "Não atire, sou da paz",
    "Marta Leone"
]


async def change_member_nick(member, nick, ctx=None):
    if not isinstance(member, discord.Member):
        member = ctx.guild.get_member(member)

    if member:
        try:
            await member.edit(nick=nick)
        except discord.DiscordException:
            pass


async def on_join_or_nick_update(cog, member: discord.Member):
    await cog.register_member(member, member.guild.id)
    await change_member_nick(member, random.choice(nicks))


class PrimeiroAbrilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def register_member(self, member, guild_id):
        try:
            await self.bot.memberservice.add_member(member, guild_id)
        except UniqueViolationError:
            pass

    @commands.command(name="scanmembers", aliases=['sm'])
    async def scan_members(self, ctx):
        """Scaneia e adiciona membros no banco"""
        if not ctx.guild.id:
            return

        if not await self.bot.guildservice.check_guild(ctx.guild.id):
            await self.bot.guildservice.add_guild(ctx.guild)

        async for member in ctx.guild.fetch_members():
            await self.register_member(member, ctx.guild.id)
        print("Usuários salvos com sucesso.")
        await asyncio.sleep(1)
        await ctx.message.delete()

    # Todo: Função de Alterar nomes dos usuários
    @commands.command(name="watanuki", aliases=['wata'])
    async def watanuki_primeiro_de_abril(self, ctx=None, guild=None):
        """Altera o nome dos usuários"""
        guild = ctx.guild if ctx else guild
        pool_nicks = list(nicks)
        async for member in guild.fetch_members():
            nome = random.choice(pool_nicks)
            pool_nicks.remove(nome)
            await change_member_nick(member, nome, ctx=ctx)
        print("Watanuki watanuki primeiro de abril!")
        await self.bot.guildservice.update_guild_online(guild.id, True)
        await asyncio.sleep(1)
        if ctx:
            time = pendulum_to_datetime(pendulum.now().add(minutes=TIME_INCREMENT_IN_MINUTES))
            await self.bot.guildservice.update_time(guild.id, time)
            await ctx.message.delete()

    @commands.command(name="restoremembers", aliases=['rm'])
    async def restore_members(self, ctx):
        """Restaura nome dos usuários salvos no banco anteriormente"""
        membros = await self.bot.memberservice.get_all_members(ctx.guild.id)
        await self.bot.guildservice.update_guild_online(ctx.guild.id, False)

        for member in membros:
            await change_member_nick(member['member_id'], member['display_name'], ctx)
        print("Usuários restaurados com sucesso")
        await self.bot.guildservice.update_guild_online(ctx.guild.id, False)
        await asyncio.sleep(1)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(PrimeiroAbrilCog(bot))
