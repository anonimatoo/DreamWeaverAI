import os
import random
import time
import wave
import struct
import numpy as np
from PIL import Image, ImageDraw

# Criar uma imagem surrealista randomizada
def generate_surreal_image(filename="surreal_art.png"):
    width, height = 512, 512
    image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    for _ in range(100):  # Desenhar formas aleatórias
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        color = tuple(random.randint(0, 255) for _ in range(3))
        draw.ellipse([x1, y1, x2, y2], fill=color, outline=color)
    
    image.save(filename)
    print(f"Imagem gerada: {filename}")

# Criar uma música aleatória
def generate_surreal_music(filename="surreal_music.wav", duration=5):
    sample_rate = 44100  # Taxa de amostragem
    num_samples = duration * sample_rate
    waveform = np.sin(2 * np.pi * np.cumsum(np.random.rand(num_samples) * 10))
    waveform = (waveform * 32767).astype(np.int16)
    
    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16 bits
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(waveform.tobytes())
    
    print(f"Música gerada: {filename}")

# Criar e vender NFT automaticamente (simulação)
def sell_nft(image_filename, music_filename):
    price = round(random.uniform(0.01, 10), 2)  # Preço aleatório em criptomoeda
    print(f"NFT gerado com arte {image_filename} e música {music_filename} listado por {price} ETH!")
    return price

# Loop principal
def main():
    while True:
        print("\n--- Gerando um novo NFT surrealista ---")
        img_file = "surreal_art.png"
        music_file = "surreal_music.wav"
        generate_surreal_image(img_file)
        generate_surreal_music(music_file)
        earnings = sell_nft(img_file, music_file)
        print(f"💰 Lucro estimado: {earnings} ETH")
        time.sleep(10)  # Espera 10 segundos antes de gerar o próximo

if __name__ == "__main__":
    main()
