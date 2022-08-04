#pip install pytube
from pytube import YouTube
video = YouTube('https://www.youtube.com/watch?v=_K9YV4t9dzY')
stream = video.streams.get_by_itag(22)
stream.download()