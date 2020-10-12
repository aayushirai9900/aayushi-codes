import moviepy.editor
video1 = moviepy.editor.VideoFileClip("C:/Users/user/Desktop/Movie/1.mp4")
video2 = moviepy.editor.VideoFileClip("C:/Users/user/Desktop/Movie/2.mp4")
finalvideo = moviepy.editor.concatenate_videoclips([video1,video2])
finalvideo.write_videofile("Final.mp4",codec='libx264')
