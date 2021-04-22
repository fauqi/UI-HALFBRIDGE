from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
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
        self.entry =[[0 for x in range(4)]  for x in range(4)]
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
        self.photo4=Image.open("foto/calculate.png")
        self.photo4 = self.photo4.resize((int(self.sW*0.132), int(self.sH*0.06)), Image.ANTIALIAS)
        self.calculateImage = ImageTk.PhotoImage(self.photo4)
        self.photo5=Image.open("foto/reset.png")
        self.photo5 = self.photo5.resize((int(self.sW*0.132), int(self.sH*0.06)), Image.ANTIALIAS)
        self.resetImage = ImageTk.PhotoImage(self.photo5)
        

        self.labelImage=Label(self.frame,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar)
        self.labelImage2=Label(self.frame2,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar2)
        self.exitButton = Button(self.frame,command=self.exit,bg="#9561EB",text="EXIT",font='Helvetica 30 bold')
        self.startButton = Button(self.frame,command=self.start,bg="#EF5858",text="START",font='Helvetica 30 bold')
        self.backBtn=Button(self.frame2,image=self.backImage,command=self.back)
        self.calculateBtn=Button(self.frame2,activebackground="#67B840",image=self.calculateImage,command=self.calculate,borderwidth=0,bg="#67B840")
        self.resetBtn=Button(self.frame2,activebackground="#67B840",image=self.resetImage,command=self.calculate,borderwidth=0,bg="#67B840")

        #self.entry[0][0]=Entry(self.frame2,font=20)
        for x in range(4):
            for y in range(4):    
                self.entry[x][y] = Entry(self.frame2,font=20)



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
        self.backBtn.place(x=self.sW*0.01,y=self.sH*0.02,width=self.sW*0.032, height=self.sH*0.06)
        self.calculateBtn.place(x=self.sW*0.774,y=self.sH*0.39,width=self.sW*0.132, height=self.sH*0.06)
        self.resetBtn.place(x=self.sW*0.774,y=self.sH*0.47,width=self.sW*0.132, height=self.sH*0.06)
        #elf.entry[0][0].place(x=0.798*self.sW,y=0.299*self.sH,width=self.sW*0.065,height=self.sH*0.044)
        j=0
        k=0
        offsetH=self.sH*0.2128
        offsetW=self.sW*0.181
        jarakW=self.sW*0.141
        jarakH=self.sH*0.0449
        entryWidth=self.sW*0.065
        entryHeight=self.sH*0.044
        
        for j in range(4):
            for k in range(4):    
                self.entry[j][k].place(x=offsetW+((j*(entryWidth+jarakW))),y=offsetH+((k*(entryHeight+jarakH))),width=entryWidth,height=entryHeight)
        self.entry[3][2].place_forget()
        self.entry[3][3].place_forget()
    def back(self):
        self.frame2.place_forget()
        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
    def calculate(self):
        try:
            a=float(self.entry[0][0].get())
            print(a)
        except:
             messagebox.showerror("warning","ganti koma(,) dengan titik(.) untuk pecahan")
        
screen = page(root)
root.mainloop()