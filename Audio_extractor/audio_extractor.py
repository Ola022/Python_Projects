import moviepy.editor as mp
import os

""" [ pip install moviepy ]"""

# C:\Users\Ola\Documents\programming\Real-Projects\Audio_extractor\BENIN_BOYS.mp4
#path = "C:/Users/Ola/Documents/programming/Real-Projects/Audio_Video/{}".format("BENIN_BOYS")
path = input("Enter the path for the video file :\n")

video_clip = mp.VideoFileClip(path)
audio_clip = video_clip.audio
audio_clip.write_audiofile("audio.mp3")