from tkinter import *
from PIL import ImageTk, Image

root=Tk()
SCREENWIDTH = int(root.winfo_screenwidth())
SCREENHEIGHT = int(root.winfo_screenheight())
class page:
    def __init__(self,master):
        self.master=master
        self.master.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.sW=SCREENWIDTH
        self.sH=SCREENHEIGHT
        self.frame=Frame(self.master,bg="RED")
        self.page_init()
        self.showLayar()
    def page_init(self):
        self.photo=Image.open("awal.png")
        self.photo = self.photo.resize((self.sW, self.sH), Image.ANTIALIAS)
        self.gambar = ImageTk.PhotoImage(self.photo)
        self.labelImage=Label(self.frame,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar)
        self.exitButton = Button(command=exit,bg="#9561EB",text="EXIT",font='Helvetica 30 bold')
    def showLayar(self):
        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.labelImage.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.exitButton.place(x=self.sW*0.573 ,y=self.sH*0.77,width=self.sW*0.251,height=self.sH*0.1)
    def exit(self):
        root.destroy()
screen = page(root)
root.mainloop()