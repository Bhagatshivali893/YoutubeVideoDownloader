#import package
from tkinter import *
from pytube import YouTube

window=Tk()
window.geometry("700x700")
window.config(background="red")
window.title("Youtube Video Downloader By shivali")

youtube_logo=PhotoImage(file="youtubelogo.png")
window.iconphoto(False,youtube_logo)

Label(window,text="YouTube Video Downloader",font=("Comic Sans MS" ,30, "bold"),bg="lightgreen").pack(padx=5,pady=50)

video_link=StringVar()

Label(window,text="Enter The Link Below ",font=("Comic Sans MS",25,"bold")).pack(padx=1,pady=10)
Entry_link=Entry(window,width=50,font=("Comic Sans MS",15,"bold"),textvariable=video_link,bd=4).pack(padx=2,pady=20)

def video_download():
    video_url=YouTube(str(video_link.get()))
    videos=video_url.streams.first()
    videos.download()

    Label(window,text="Download Completed !!",font=("Arial",30,"bold"),bg="lightpink",fg="black").pack(padx=5,pady=20)
    Label(window,text="Check Your Project's Folder To see the downloaded video",font=("Arial",15,"bold"),bg="yellow").pack(padx=1,pady=20)

Button(window,text="DOWNLOAD",font=("Arial",30,"bold"),bg="lightblue",command=video_download).pack(padx=2,pady=20)
window.mainloop()