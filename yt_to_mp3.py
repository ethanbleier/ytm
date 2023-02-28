from pytube import YouTube
import os
from colorama import Back

yt = YouTube(
    str(input("Enter url \n>>")))

video = yt.streams.filter(only_audio=True).first()

print("enter destination, leave blank for current directory")
destination = str(input(">> ")) or '.'

out_file = video.download(output_path = destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " " + Back.GREEN + "Downloaded to " + destination)
