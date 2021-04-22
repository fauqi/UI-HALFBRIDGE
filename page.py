from tkinter import *
from PIL import ImageTk, Image

root=Tk()
SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(SCREENWIDTH, SCREENHEIGHT))
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        self.flag=0
        pad=0
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Double-1>',self.escape)      
    def escape(self,event):
        global SCREENHEIGHT,SCREENWIDTH
        if self.flag==0:
            self.master.overrideredirect(False)
            self.flag=1
        else:
            self.master.overrideredirect(True)
            self.flag=0
        
      
app = FullScreenApp(root)
class page:
    def __init__(self,master):
        self.master=master
        self.sW=SCREENWIDTH
        self.sH=SCREENHEIGHT
        self.frame=Frame(self.master,bg="RED")
        self.frame2=Frame(self.master,bg="RED")
        self.page_init()
        self.showLayar()
    def page_init(self):
        self.photo=Image.open("foto/awal.png")
        self.photo = self.photo.resize((self.sW, self.sH), Image.ANTIALIAS)
        self.gambar = ImageTk.PhotoImage(self.photo)
        self.photo2=Image.open("foto/tab2.png")
        self.photo2 = self.photo2.resize((self.sW, self.sH), Image.ANTIALIAS)
        self.gambar2 = ImageTk.PhotoImage(self.photo2)
        self.photo3=Image.open("foto/back.png")
        self.photo3 = self.photo3.resize((int(self.sW*0.032), int(self.sH*0.06)), Image.ANTIALIAS)
        self.backImage = ImageTk.PhotoImage(self.photo3)
        

        self.labelImage=Label(self.frame,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar)
        self.labelImage2=Label(self.frame2,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar2)
        self.exitButton = Button(self.frame,command=self.exit,bg="#9561EB",text="EXIT",font='Helvetica 30 bold')
        self.startButton = Button(self.frame,command=self.start,bg="#EF5858",text="START",font='Helvetica 30 bold')
        self.backBtn=Button(self.frame2,image=self.backImage,command=self.back)




    def showLayar(self):
        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.labelImage.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.exitButton.place(x=self.sW*0.573 ,y=self.sH*0.77,width=self.sW*0.251,height=self.sH*0.1)
        self.startButton.place(x=self.sW*0.215 ,y=self.sH*0.77,width=self.sW*0.251,height=self.sH*0.1)
    def exit(self):
        root.destroy()
    def start(self):
        self.frame.place_forget()
        self.frame2.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.labelImage2.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.backBtn.place(x=self.sW*0,y=self.sH*0,width=self.sW*0.032, height=self.sH*0.06)
    def back(self):
        self.frame2.place_forget()
        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        
screen = page(root)
root.mainloop()