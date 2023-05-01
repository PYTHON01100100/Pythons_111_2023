from pytube import YouTube
print("hello")
link ="https://youtu.be/KHAjn2tjvCw"
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()

print("it has done")

"""


"""