from pytube import YouTube
import os
from colorama import Back


# Stole some of this guys code: https://stackoverflow.com/questions/68680322/pytube-urllib-error-httperror-http-error-410-gone
yt = YouTube(input("link to download >>"))

#Show details
print("title: ", yt.title)
print("views: ", yt.views)
print("length: ", yt.length)

video = yt.streams.filter(only_audio=True).first()

destination = '.'

out_file = video.download(output_path = destination)

base = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " " + Back.GREEN + "Downloaded to " + destination)
