from moviepy.editor import *                                         #pip install moviepy
videoclip = VideoFileClip('Enter mp4 file name here')                #enter file name and path of the file which will be converted
audio = videoclip.audio
audio.write_audiofile('Enter mp3 file name to be created here')      #enter the file name and path where the file should be saved.

