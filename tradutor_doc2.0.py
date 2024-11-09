from googletrans import Translator
from pathlib import Path
import pyperclip
import subprocess
import pyautogui
from time import sleep
import tkinter as tk
from tkinter import filedialog
def selecionar_arquivo():
    # Cria uma janela oculta do Tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    # Abre a caixa de diálogo para selecionar um arquivo
    caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Arquivos SRT", "*.srt")])

    return caminho_arquivo

# Usando a função para selecionar o arquivo
CAMINHO_ARQUIVO = selecionar_arquivo()

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

tamanho_parte = 5000


conteudo_novo = [conteudo[i:i + tamanho_parte] for i in range(0, len(conteudo), tamanho_parte)]

translator = Translator()

conteudo_traduzido = []

for item in conteudo_novo:
    traducao = translator.translate(item, src='en', dest='pt')
    conteudo_traduzido.append(traducao.text)

conteudo_completo = ''.join(conteudo_traduzido)


pyperclip.copy(conteudo_completo)

subprocess.Popen(['notepad.exe'])

sleep(1)

pyautogui.hotkey("ctrl", "v")