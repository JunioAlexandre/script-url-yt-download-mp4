import yt_dlp

def baixar_video(url, caminho_destino="/home/junio/Videos/videos-baixados-pelo-script"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio[ext=m4a]/best',  
        'merge_output_format': 'mp4',
        'outtmpl': f"{caminho_destino}/%(title)s.%(ext)s",
    # 'noplaylist': True,  # Ative se caso a URL seja de uma playlist, e vocẽ não queira baixar todos os vídeos!!
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url_video = input("Digite a URL do vídeo do YouTube: ")
baixar_video(url_video)
