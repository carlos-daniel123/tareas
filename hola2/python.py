import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def python(self, ctx):
        await ctx.send("Python is a great programming language!")

@bot.command()
async def linux(ctx):
        await ctx.send("Linux is a popular open-source operating system kernel that serves as the foundation for many distributions, such as Ubuntu, Fedora, and Debian.")

@bot.command()
async def windows(ctx):
        await ctx.send("Windows is a widely used operating system developed by Microsoft.")

@bot.command()
async def macos(ctx):
        await ctx.send("macOS is the operating system developed by Apple for their Mac computers.")

@bot.command()
async def chromeos(ctx):
        await ctx.send("Chrome OS is a lightweight operating system developed by Google, primarily for Chromebooks.")

@bot.command()
async def android(ctx):
        await ctx.send("Android is a mobile operating system developed by Google, used on a wide range of smartphones and tablets.")

@bot.command()
async def freebsd(ctx):
        await ctx.send("FreeBSD is a free and open-source Unix-like operating system based on the Berkeley Software Distribution (BSD).")

@bot.command()
async def unix(ctx):
        await ctx.send("Unix is a powerful and versatile operating system that has influenced many other operating systems, including Linux and macOS.")

@bot.command()
async def imagen(ctx):
        if ctx.message.attachments:

            for attachment in ctx.message.attachments:

                    file_name= attachment.filename

                    file_url = attachment.url        

                    await attachment.save(f"{file_name}")

                    await ctx.send(f"¡Gracias por subir la imagen! La URL de tu imagen es: {file_url}")

                    await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"{file_name}"))

        else:

            await ctx.send("No recibí ninguna imagen o el archivo no es una imagen. Por favor, intenta de nuevo.")

bot.run('el token va aqui bro')
