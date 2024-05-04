from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

path = r"/Users/anshumansingh/Downloads"
url  = r"https://youtu.be/zT7niRUOs9o?si=0ZvP6o7r2rGnhEwy"

def download_video(url, path):
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution = yt.streams.get_highest_resolution().download(path)
        print("Downloaded Successfully")
    except Exception as e:
        print("Error: ", e) 

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Folder selected: {folder}')
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url =  input("Enter the video URL: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Please select a folder to save the video")
    else:
        print(f"Downloading video to {save_dir}")
        download_video(video_url, save_dir)


