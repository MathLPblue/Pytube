from pytube import YouTube
from sys import argv 
link = input("Digite o link do vídeo do YouTube: ") if len(argv) < 2 else argv[1]
yt = YouTube(link)


print('Título: ', yt.title)
print('Visualizações:', yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('Pasta download') #inserir pasta para download aqui

print('O download foi realizado.')