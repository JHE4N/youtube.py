#pip install pytube
from pytube import YouTube


def download_music(url):
    videoLink = YouTube(url)
    audio = videoLink.streams.filter(only_audio=True)
    audio.download(filename="audio.mp4")



download_music('https://www.youtube.com/watch?v=_K9YV4t9dzY')