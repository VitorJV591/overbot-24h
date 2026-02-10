import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} ONLINE E PRONTO PARA A FAXINA!')

@bot.command()
async def reformar(ctx):
    await ctx.send("🧹 *INICIANDO FAXINA TOTAL...* Apagando canais antigos!")

    # 1. ESTA PARTE APAGA TUDO QUE EXISTE
    for canal in ctx.guild.channels:
        try:
            await canal.delete()
        except:
            continue 

    # 2. CRIA CANAIS DA STAFF (Privados)
    staff_cat = await ctx.guild.create_category("🛡️ STAFF")
    await ctx.guild.create_text_channel("🔒-conversa-staff", category=staff_cat)
    await ctx.guild.create_voice_channel("🔊 Reunião Staff", category=staff_cat)

    # 3. CRIA CANAIS PÚBLICOS (Chat e Voz)
    pub_cat = await ctx.guild.create_category("🌎 COMUNIDADE")
    await ctx.guild.create_text_channel("💬-geral", category=pub_cat)
    await ctx.guild.create_text_channel("📢-avisos", category=pub_cat)
    await ctx.guild.create_voice_channel("🔊 Chat de Voz", category=pub_cat)

    # 4. CRIA CANAIS DE OVERWATCH
    ow_cat = await ctx.guild.create_category("🏆 OVERWATCH")
    await ctx.guild.create_text_channel("🎮-buscar-grupo", category=ow_cat)
    await ctx.guild.create_voice_channel("🔊 RANKED 5v5", category=ow_cat, user_limit=5)

    # Canal final para confirmar a reforma
    final = await ctx.guild.create_text_channel("✅-reforma-concluida")
    await final.send("🔥 *TUDO PRONTO!* Servidor limpo e organizado.")

# COLE O TOKEN INTEIRO DENTRO DAS ASPAS ABAIXO
bot.run(os.getenv('DISCORD_TOKEN'))
