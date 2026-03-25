import discord
from discord.ext import commands
import yaml
import random
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import requests

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

TOKEN = config['token']

# Cargar el modelo al inicio
try:
    model = tf.keras.models.load_model('keras_model.h5')
    print("Modelo cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    model = None

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 9999):
    await ctx.send("he" * count_heh)

@bot.command()
async def loteria(ctx):
    number = random.randint(1, 9999)
    winning_number = random.randint(1, 9999)
    await ctx.send(f'Your number: {number}\nWinning number: {winning_number}')
    if number == winning_number:
        await ctx.send('Congratulations! You won the lottery!')
    else:
        await ctx.send('Sorry, better luck next time!')

@bot.command()
async def imagen(ctx):
    if model is None:
        await ctx.send("El modelo de IA no está disponible.")
        return
    
    if not ctx.message.attachments:
        await ctx.send("Por favor, adjunta una imagen con el comando.")
        return
    
    attachment = ctx.message.attachments[0]
    if not attachment.content_type.startswith('image/'):
        await ctx.send("El archivo adjunto debe ser una imagen.")
        return
    
    try:
        # Descargar la imagen
        response = requests.get(attachment.url)
        response.raise_for_status()
        img = Image.open(io.BytesIO(response.content))
        
        # Preprocesar la imagen (asumiendo 224x224, ajustar si es necesario)
        img = img.resize((224, 224))
        img = img.convert('RGB')  # Asegurar 3 canales
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Hacer predicción
        prediction = model.predict(img_array)
        
        # Asumir clasificación binaria: 0 real, 1 IA
        if prediction[0][0] > 0.5:
            result = "una imagen generada por IA"
        else:
            result = "una imagen real"
        
        await ctx.send(f"La imagen parece ser {result}.")
    
    except Exception as e:
        await ctx.send(f"Error al procesar la imagen: {str(e)}")

bot.run("hola bro, aqui va tu token")

# hola

""" hola """
