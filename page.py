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
        master.bind('<Escape>',self.escape)
        master.bind('<F>',self.full)
        master.bind('<f>',self.full)      
    def escape(self,event):
        global SCREENHEIGHT,SCREENWIDTH
        if self.flag==0:
            self.master.overrideredirect(False)
            self.flag=1
        else:
            self.master.overrideredirect(True)
            self.flag=0
    def full(self,event):
        self.master.overrideredirect(True)
        self.flag=0
      
app = FullScreenApp(root)
class Page:
    def __init__(self,master):
        self.master=master
        self.sW=SCREENWIDTH
        self.sH=SCREENHEIGHT
        self.frame=Frame(self.master,bg="RED")
        self.frame2=Frame(self.master,bg="RED")
        self.entry =[[0 for x in range(5)]  for x in range(5)]
        self.outLabel =[[0 for x in range(5)]  for x in range(5)]
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
        self.resetBtn=Button(self.frame2,activebackground="#67B840",image=self.resetImage,command=self.reset,borderwidth=0,bg="#67B840")
        self.defaultBtn=Button(self.frame2,command=self.default)
        #self.entry[0][0]=Entry(self.frame2,font=20)
        for x in range(5):
            for y in range(5):    
                self.entry[x][y] = Entry(self.frame2,font=20)
        for j in range(5):
            for k in range(5):    
                self.outLabel[j][k] = Label(self.frame2,font=20,bg="#7BD152")



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
        x=0
        y=0
        offsetH=self.sH*0.165
        offsetW=self.sW*0.181
        jarakW=self.sW*0.141
        jarakH=self.sH*0.0292
        entryWidth=self.sW*0.065
        entryHeight=self.sH*0.044
        
        for j in range(5):
            for k in range(5):    
                self.entry[j][k].place(x=offsetW+((k*(entryWidth+jarakW))),y=offsetH+((j*(entryHeight+jarakH))),width=entryWidth,height=entryHeight)
        
        offsetH2=self.sH*0.6367
        offsetW2=self.sW*0.181
        jarakW2=self.sW*0.141
        jarakH2=self.sH*0.0195
        labelWidth=self.sW*0.065
        labelHeight=self.sH*0.044
       
        for x in range(5):
            for y in range(5):    
                self.outLabel[x][y].place(x=offsetW2+((y*(labelWidth+jarakW2))),y=offsetH2+((x*(labelHeight+jarakH2))),width=labelWidth,height=labelHeight)
        
        self.entry[2][3].place_forget()
        self.entry[3][3].place_forget()
        self.entry[4][3].place_forget()
        self.defaultBtn.place(x=100,y=100,width=50,height=50)
        self.master.bind('<Return>',self.enter)
    def enter(self,event):
        self.calculate()
        

    def back(self):
        self.frame2.place_forget()
        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH,anchor=NW)
        self.master.unbind('<Return>')
    def calculate(self):
        # try:
        #     self.hitung()
            
        # except:
        #      messagebox.showerror("warning","ganti koma(,) dengan titik(.) untuk pecahan")
        self.hitung()
    def reset(self):
        for x in range(5):
            for y in range(5):
                self.entry[x][y].delete(0,END)
    def hitung(self):
        # vinMax=float(self.entry[0][0].get())
        # voutMax=float(self.entry[0][1].get())
        # # print(str(vinMax)+str(voutMax))
        # a="{:.2f}".format(vinMax)
        # print (a)
        self.vinMax=float(self.entry[0][0].get())
        self.vinMin=float(self.entry[1][0].get())
        self.vOut=float(self.entry[2][0].get())
        self.iOut=float(self.entry[3][0].get())
        self.duty=float(self.entry[4][0].get())

        self.frekuensi=float(self.entry[0][1].get())
        self.rIl=float(self.entry[1][1].get())
        self.rVo=float(self.entry[2][1].get())
        self.vf=float(self.entry[3][1].get())
        self.acInd=float(self.entry[4][1].get())

        self.dBobInd=float(self.entry[0][2].get())
        self.acTraf=float(self.entry[1][2].get())
        self.dBobTraf=float(self.entry[2][2].get())
        self.bMax=float(self.entry[3][2].get())
        self.J=float(self.entry[4][2].get())

        self.s=float(self.entry[0][3].get())
        self.sigmaSplit=float(self.entry[1][3].get())
        #RUMUS
        self.duty=self.duty/100
        self.frekuensi=self.frekuensi*1000
        self.rIl=self.rIl/100

        self.rasio = self.vOut/(self.vinMax*self.duty)
        self.outLabel[0][0].config(text=str(self.rasio))

        self.vin_a=self.vinMax/(2*(1/self.rasio)-(2*self.vf))
        self.dIlx = self.rIl*self.iOut
        self.Lx=(1/self.dIlx)*(self.vin_a-self.vOut)*(1/(2*self.frekuensi))*(((self.vOut+(2*self.vf))/(self.vinMax+(2*self.vf)))
       
        self.Lx=self.Lx*1000000
        self.outLabel[3][1].config(text="{:.2f}".format(self.Lx))
    def default(self):
        self.vinMax=100
        self.entry[0][0].insert(0,str(self.vinMax))
        self.vinMin=100
        self.entry[1][0].insert(0,str(self.vinMin))
        self.vOut=19
        self.entry[2][0].insert(0,str(self.vOut))
        self.iOut=3
        self.entry[3][0].insert(0,str(self.iOut))
        self.duty=40
        self.entry[4][0].insert(0,str(self.duty))

        self.frekuensi=40
        self.entry[0][1].insert(0,str(self.frekuensi))
        self.rIl=20
        self.entry[1][1].insert(0,str(self.rIl))
        self.rVo=0.1
        self.entry[2][1].insert(0,str(self.rVo))
        self.vf=1.2
        self.entry[3][1].insert(0,str(self.vf))
        self.acInd=1.61
        self.entry[4][1].insert(0,str(self.acInd))

        self.dBobInd=16
        self.entry[0][2].insert(0,str(self.dBobInd))
        self.acTraf=1.96
        self.entry[1][2].insert(0,str(self.acTraf))
        self.dBobTraf=17
        self.entry[2][2].insert(0,str(self.dBobTraf))
        self.bMax=0.25
        self.entry[3][2].insert(0,str(self.bMax))
        self.J=4.5
        self.entry[4][2].insert(0,str(self.J))

        self.s=4.5
        self.entry[0][3].insert(0,str(self.s))
        self.sigmaSplit=10
        self.entry[1][3].insert(0,str(self.sigmaSplit))
  


screen = Page(root)
root.mainloop()