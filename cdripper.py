import tkinter as tk
from tkinter import messagebox
import subprocess
import eyed3

def rip_cd_to_mp3():
    try:
        subprocess.check_call(["cdparanoia", "-B"])
        messagebox.showinfo("Success", "CD tracks extracted successfully!")

        subprocess.check_call(["lame", "--preset", "insane", "*.wav"])
        messagebox.showinfo("Success", "CD tracks converted to MP3 successfully!")


        audiofile = eyed3.load("track01.mp3")


        audiofile.tag.artist = "Artist Name"
        audiofile.tag.album = "Album Name"
        audiofile.tag.album_artist = "Album Artist"
        audiofile.tag.title = "Title"
        audiofile.tag.track_num = 1


        with open("cover.jpg", "rb") as image_data:
            audiofile.tag.images.set(3, image_data.read(), "image/jpeg")


        audiofile.tag.save()

        messagebox.showinfo("Success", "Metadata and Album Art added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("CD Ripper")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Rip CD to MP3")
label.pack(pady=20)

rip_button = tk.Button(frame, text="Start Ripping", command=rip_cd_to_mp3)
rip_button.pack()

root.mainloop()
