from moviepy.editor import *
videoclip = VideoFileClip('Enter mp4 file name here')
audio = videoclip.audio
audio.write_audiofile('Enter mp3 file name to be created here')
