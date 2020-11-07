from pytube import YouTube     #pip install pytube

#ask for the link from user
link = input("Enter Youtube video link here: \n")
yout = YouTube(link)

#Showing details
# print("Title: ",yt.title)
# print("Number of views: ",yt.views)
# print("Length of video: ",yt.length)
# print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
video = yout.streams.get_highest_resolution()

#Starting download
print("Downloading...")
video.download()   #video will be downloaded in the wirking directory......if you want to download anywhere else specify the path.
print("Download completed!!")
