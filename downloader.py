import requests
import threading
import os
import instaloader
from tkinter import *
from time import sleep

# functions
def clear_url_box():
    User.set("")
def update_status(temp):
    statusvar.set(temp)
    sbar.update()
def download():
    t1 = threading.Thread(target=get_image_url, name='t1')
    t1.start()
def get_image_url():
    download_btn.config(text="Wait",command=None)
    username = User.get()
    update_status("Downloading")
    # username = "elite2002akshay"
    ig = instaloader.Instaloader()
    try:
        t = ig.download_profile(username , profile_pic_only=True)
    except:
        update_status("Some Error")
        sleep(3)
    download_btn.config(text="Download",command=download)
    update_status("Ready to Download")
# main body
if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite Insta Profile Photo Downloader")
    root.geometry("1000x600")
    root.minsize(1000,600)
    

    # Variables
    User = StringVar()
    downloads_location=StringVar()
    download_path=StringVar()
    download_path.set(os.getcwd())
    downloads_location.set(f"Downloads path :- {download_path.get()}")
    statusvar = StringVar()
    statusvar.set("Ready to download")
    # code to download a video
    heading1=Label(root,text="ELITE AKSHAY",font="calibre 40 bold",relief=RAISED,background="red",padx=10,pady=9)
    heading1.pack()
    space=Label(root,text="",font="calibre 2 bold")
    space.pack()
    heading2=Label(root,text="INSTA PROFILE PHOTO DOWNLOADER",font="Times 25 bold",relief=RAISED,background="cyan",padx=10,pady=9,)
    heading2.pack()
    f1=Frame(root)
    f1.pack(side=TOP,fill=BOTH,expand=True,pady=10)
    name=Label(f1,text="ENTER USERNAME",font="calibre 20 bold italic",relief=FLAT,padx=8,pady=5,)
    name.pack()
    space=Label(f1,text="",font="calibre 1 bold")
    space.pack()
    user_name=Entry(f1,textvariable=User,font="calibre 25 normal",fg="blue",relief=SUNKEN)
    user_name.pack()
    download_loacation_display=Label(f1,textvariable=downloads_location,font="calibre 10 bold italic",relief=FLAT,padx=18,pady=3)
    download_loacation_display.pack()
    download_btn=Button(f1,text="Download",command=download,bd=5,fg="blue",font="calibre 18 bold")
    download_btn.pack(side = LEFT, expand = True, fill = X)
    clear_url_btn=Button(f1,text="CLEAR URL",command=clear_url_box,bd=5,font="calibre 18 bold")
    clear_url_btn.pack(side = LEFT, expand = True, fill = X)
    # statusbar
    sbar = Label(root,textvariable=statusvar, relief=SUNKEN, anchor="w",padx=10,pady=7,background="cyan",fg="red",font="calibre 12 bold")
    sbar.pack(side=BOTTOM, fill=X)



    root.mainloop()