from pytube import YouTube
from sys import argv 
import tkinter as tk



def baixar_video():
 link = entrada_link.get()
 yt = YouTube(link)


 print('Título: ', yt.title)
 print('Visualizações:', yt.views)

 yd = yt.streams.get_highest_resolution()
 yd.download('Pasta download') #inserir pasta para download aqui

 print('O download foi realizado.')

janela = tk.Tk()
janela.title("Baixar Vídeo do YouTube")
rotulo = tk.Label(janela, text="Insira o link do vídeo:")
rotulo.pack(pady=10)
entrada_link = tk.Entry(janela, width=40)
entrada_link.pack(pady=10)
botao_baixar = tk.Button(janela, text="Baixar Vídeo", command =baixar_video)
botao_baixar.pack(pady=10)
janela.mainloop()
