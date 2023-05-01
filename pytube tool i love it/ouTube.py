from pytube import YouTube
YouTube('https://youtu.be/KHAjn2tjvCw').streams.first().download()
yt = YouTube('https://youtu.be/KHAjn2tjvCw')
yt.streams
