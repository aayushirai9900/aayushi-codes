import moviepy.editor                                                         #pip install moviepy
video1 = moviepy.editor.VideoFileClip("Vedio Merger/1.mp4")                   # Tking clip to merge     #add .subclip(a,b) to jus merge subclip from the full clip
video2 = moviepy.editor.VideoFileClip("Vedio Merger/2.mp4")                   # Tking clip to merge     #add .subclip(a,b) to jus merge subclip from the full clip
finalvideo = moviepy.editor.concatenate_videoclips([video1,video2])           # merging video
finalvideo.write_videofile("Final.mp4",codec='libx264')                       # encoding and writing video in desired name.
 
