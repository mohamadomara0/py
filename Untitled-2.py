# طارق العربي

from tkinter import *
from yt_dlp import YoutubeDL

def high_quality():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The video has been downloaded in high quality.")
    except Exception as e:
        print(f"Error downloading: {e}")

def low_quality():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'worst',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The video has been downloaded in low quality.")
    except Exception as e:
        print(f"Error downloading: {e}")

def get_audio():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The audio has been downloaded.")
    except Exception as e:
        print(f"Error downloading: {e}")


window = Tk()
window.title("YouTube Downloader")
window.geometry("600x500")
window.configure(bg="pink")

label = Label(window, text="Add your YouTube link here", font="bold", bg="pink")
label.place(x=200, y=30)

entry = Entry(window, width=50)
entry.place(x=200, y=60)

high_btn = Button(window, text="High Quality", command=high_quality)
high_btn.place(x=100, y=200)

low_btn = Button(window, text="Low Quality", command=low_quality)
low_btn.place(x=200, y=200)

audio_btn = Button(window, text="Get Audio", command=get_audio)
audio_btn.place(x=300, y=200)

window.mainloop()
