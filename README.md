<h1 align='center'>
 <strong> <samp>Downloading Instagram Profile Photo using Python</samp> </strong> 👨‍💻
</h1>

## Instagram is an American photo and video sharing social networking service founded by Kevin Systrom and Mike Krieger.
## In this blog we are going to create Instagram Profile Photo downloader using Python. It will be GUI and it will help you to download profile photo of instagram accounts, no matter it is public or private.

# **PRE-REQUISITES:**
 - ### **Basic knowledge of Python**
 - ### **Basic knowledge of Tkinter**
---
## In this project we are going to use instaloader module. You can install it via using pip :
> ## **pip install instaloader**
<br>

## First of all we will create basic GUI using Tkinter.

## ***Below code will help you to create basic GUI :***

``` Python
from tkinter import *
# main body
if __name__=="__main__":
root = Tk()
# window size
root.title("Elite Insta Profile Photo Downloader")
root.geometry("850x520")
root.minsize(800,400)
root.mainloop()
```
> ## **Above code will create a basic GUI .**

<p align ="center">
<img src="https://i.imgur.com/3pUBDsZ.png" alt="Basic GUI" width="650" />
</p>


### Out basic window is ready, now our aim is to decorate it and allow user to enter username in order to download photo.
### We will be using Tkinter variables to store the information like username.
### As Tkinter does not have any ***statusbar*** so will will be creation it using lable. And we will be using os module to get the current working directory and show it in GUI.

> ## **Below code will create GUI and decorate it :**
``` Python
import os
from tkinter import *

# functions
def clear_url_box():
pass
def download():
pass

if __name__=="__main__":
root = Tk()
# window size
root.title("Elite Insta Profile Photo Downloader")
root.geometry("850x520")
root.minsize(800,400)
# Variables
User = StringVar()
downloads_location=StringVar()
download_path=StringVar()
statusvar = StringVar()
download_path.set(os.getcwd())
downloads_location.set(f"Downloads path :- {download_path.get()}")
statusvar.set("Ready to download")
# Designing GUI
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
```
<p align ="center">
<img src="https://i.imgur.com/GTLQHeE.png" alt="Designed GUI" width="650" />
</p>


### Now our Gui is almost ready, now we need to add functionality to our Download button and Clera Url button.
### We also need to update our statusbar like download completed, Some Error.
### It is optional to use **threading** module, but we will be using it. Threading module is used here to download Profile Photo  as it is a time taking task, **so we will use different thread to perform it.** If we will use main thread to download then our GUI will become laggy.
> ## **Now our final code is :**
``` Python
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
root.geometry("850x520")
root.minsize(800,400)
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
```
<p align ="center">
<img src="https://i.imgur.com/mysRw0u.png" alt="Working GUI" width="650"  />
</p>

## ***Hope that you enjoyed it and learned something new from this blog. You can use it as a mini project and add to your resume if you are beginner.***

<p align ="center"><samp><strong>Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
<br>
– Martin Fowler</strong></samp></p>





