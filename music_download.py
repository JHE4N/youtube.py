from pytubefix import YouTube
from pytubefix.cli import on_progress
 
def music_download(url):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)

    except Exception:
        print(f"Erro: {Exception}")
