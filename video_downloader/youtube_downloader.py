import yt_dlp
""" [ pip install yt-dlp ]"""


# Define the URL
#url = "https://youtu.be/ggnrrnzqwks?si=DDHvRgcWhN8ZROrf"
url = input("Enter the URL for the video :\n")

# Set options
ydl_opts = {
    'format': 'best',
    'verbose': True
}

# Download the video
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
except Exception as e:
    print(e)




# -------------------------------
#import youtube_dl

""" [ pip install youtube_dl ]"""
#url = input("Enter the URL for the video :\n")

#try:
#    with youtube_dl.YoutubeDL() as ydl:
#        ydl.download([url])
#except Exception as e:
#    pass #print(e)

### https://youtu.be/ggnrrnzqwks?si=pQJbKVzdIbt8ojjN

