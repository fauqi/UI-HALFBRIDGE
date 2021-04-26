from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import math
import os
import threading
import time
scaleW=1
scaleH=1
root=Tk()

SCREENWIDTH = int(root.winfo_screenwidth()*scaleW)
SCREENHEIGHT = int(root.winfo_screenheight()*scaleH)
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(SCREENWIDTH, SCREENHEIGHT))

# root.resizable(True,True)
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        self.flag=0
        pad=0
        
        master.bind('<Escape>',self.escape)
        master.bind('<F>',self.full)
        master.bind('<f>',self.full)      
    def escape(self,event):
        global SCREENHEIGHT,SCREENWIDTH,scaleH,scaleW
        if self.flag==0:
            self.master.overrideredirect(False)
            self.flag=1
            scaleH=0.9259
            

        else:
            self.master.overrideredirect(True)
            self.flag=0
            scaleH=1
            
        Page(root)
        
    def full(self,event):
        global SCREENHEIGHT,SCREENWIDTH,scaleH,scaleW
        self.master.overrideredirect(True)
        self.flag=0
        scaleH=1
        
        Page(root)
        
      
app = FullScreenApp(root)
class Page:
    def __init__(self,master):
        global SCREENHEIGHT,SCREENWIDTH,scaleH,scaleW
        SCREENWIDTH = int(root.winfo_screenwidth()*scaleW)
        SCREENHEIGHT = int(root.winfo_screenheight()*scaleH)
        master.geometry("{0}x{1}+0+0".format(SCREENWIDTH, SCREENHEIGHT))
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
        self.frame.place_forget()
        self.frame2.place_forget()
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
        self.photo6=Image.open("foto/default.png")
        self.photo6 = self.photo6.resize((int(self.sW*0.0276), int(self.sH*0.14)), Image.ANTIALIAS)
        self.defaultImage = ImageTk.PhotoImage(self.photo6)
        self.photo7=Image.open("foto/help.png")
        self.photo7 = self.photo7.resize((int(self.sW*0.026), int(self.sH*0.0488)), Image.ANTIALIAS)
        self.helpImage = ImageTk.PhotoImage(self.photo7)
        self.photo8=Image.open("foto/history.png")
        self.photo8= self.photo8.resize((int(self.sW*0.062), int(self.sH*0.036)), Image.ANTIALIAS)
        self.historyImage = ImageTk.PhotoImage(self.photo8)


        self.labelImage=Label(self.frame,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar)
        self.labelImage2=Label(self.frame2,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar2)
        self.exitButton = Button(self.frame,command=self.exit,bg="#9561EB",text="EXIT",font='Helvetica 30 bold')
        self.startButton = Button(self.frame,command=self.start,bg="#EF5858",text="START",font='Helvetica 30 bold')
        self.backBtn=Button(self.frame2,image=self.backImage,command=self.back)
        self.calculateBtn=Button(self.frame2,activebackground="#67B840",image=self.calculateImage,command=self.calculate,borderwidth=0,bg="#67B840")
        self.resetBtn=Button(self.frame2,activebackground="#67B840",image=self.resetImage,command=self.reset,borderwidth=0,bg="#67B840")
        self.defaultBtn=Button(self.frame2,command=self.default,image=self.defaultImage,activebackground="#67B840",bg="#67B840",borderwidth=0)
        self.helpBtn=Button(self.frame2,command=self.help,image=self.helpImage,activebackground="#40AD0C",bg="#40AD0C",borderwidth=0)
        self.historyBtn=Button(self.frame2,command=self.history,image=self.historyImage,activebackground="#40AD0C",bg="#40AD0C",borderwidth=0)
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
        self.defaultBtn.place(x=0.7395*self.sW,y=self.sH*0.3896,width=self.sW*0.0276,height=self.sH*0.14)
        self.helpBtn.place(x=0.962*self.sW,y=self.sH*0.0175,width=self.sW*0.026,height=self.sH*0.0488)
        self.historyBtn.place(x=0.892*self.sW,y=self.sH*0.0244,width=self.sW*0.062,height=self.sH*0.036)
       
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
        
        #self.entry[2][3].place_forget()
        self.entry[3][3].place_forget()
        self.entry[4][3].place_forget()

        # self.outLabel[4][1].place_forget()
        # self.outLabel[3][3].place_forget()
        self.outLabel[4][3].place_forget()
   
        self.master.bind('<Return>',self.enter)
    def history(self):
        pass
    def help(self):
        Page2()

        
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
        self.tfall=float(self.entry[2][3].get())
        #RUMUS
        self.duty=self.duty/100
        self.frekuensi=self.frekuensi*1000
        self.rIl=self.rIl/100
        self.rVo=self.rVo/100
        self.dBobInd=self.dBobInd/10
        self.tfall=self.tfall*0.000000001
        self.rasio = self.vOut/(self.vinMax*self.duty)
        self.outLabel[0][0].config(text=str(self.rasio))

        #Lx
        self.vin_a=self.vinMax/(2*(1/self.rasio)-(2*self.vf))
        self.dIlx = self.rIl*self.iOut
        self.Lx=(1/self.dIlx)*(self.vin_a-self.vOut)*(1/(2*self.frekuensi))*(((self.vOut+(2*self.vf))/(self.vinMax+(2*self.vf))))
 

        #iL(avg) & iL(max)
        self.iL_avg = self.iOut
        self.iL_max = self.iL_avg+(self.dIlx/2)


        #winding number
        self.n=((self.Lx*self.iL_max)/(self.bMax*self.acInd))*pow(10,4)
        
        #wire size
        self.kBobInd = 3.14*self.dBobInd
        self.wireLength = (self.n*self.kBobInd*self.sigmaSplit)+(0.4*(self.n*self.kBobInd*self.sigmaSplit))
      

        #mulai trafo
        #N1
        self.T=1/self.frekuensi
        self.N1_min=((self.duty*self.T*self.vinMax)/(2*self.bMax*self.acTraf))*pow(10,4)
        self.N1=2*self.N1_min
        #N2
        self.N2= self.N1*self.rasio
        #I1(rms)dan I2(rms)
        self.I1_rms=self.rasio*self.iOut*math.sqrt(self.duty)
        self.I2_rms=0.5*self.iOut*math.sqrt(self.duty+1)
        #d1 dan d2
        self.d1=math.sqrt((4*self.I1_rms)/(3.14*self.s))
        self.d2=math.sqrt((4*self.I2_rms)/(3.14*self.s))
        #wire lengh trafo
        self.kBobTraf=3.14*self.dBobTraf
        self.length_p=(self.N1*self.kBobTraf*self.sigmaSplit)+(0.3*(self.N1*self.kBobTraf*self.sigmaSplit))
        self.length_s=(self.N2*self.kBobTraf*self.sigmaSplit)+(0.3*(self.N2*self.kBobTraf*self.sigmaSplit))
        #R
        self.R=self.vOut/self.iOut

        #Co
        self.dVo=self.rVo*self.vOut
        self.Co=((1-self.duty)/(8*self.Lx*pow(2*self.frekuensi,2)))*(self.vOut/self.dVo)

        #Rs dan Cs
        self.voff=(self.vinMax/2)-(self.Lx*(self.dIlx/(self.duty*self.T)))-self.vOut
        self.Cs = (self.iOut*self.tfall)/(2*self.voff)
    
        self.Rs=(self.duty*self.T)/(2*self.Cs)

        self.Lx=self.Lx*1000000
        self.Co=self.Co*1000000
        self.length_p=self.length_p/10#dijadikan cm
        self.length_s=self.length_s/10
        self.Cs=self.Cs*1000000000
        self.outLabel[3][1].config(text="{:.2f}".format(self.Lx))
        self.outLabel[4][0].config(text="{:.2f}".format(self.iL_avg))
        self.outLabel[0][1].config(text="{:.2f}".format(self.iL_max))
        self.outLabel[3][0].config(text="{:.2f}".format(self.n))
        self.outLabel[1][0].config(text="{:.2f}".format(self.wireLength))
        self.outLabel[0][2].config(text="{:.2f}".format(self.N1))
        self.outLabel[1][2].config(text="{:.2f}".format(self.N2))
        self.outLabel[2][2].config(text="{:.2f}".format(self.I1_rms))
        self.outLabel[3][2].config(text="{:.2f}".format(self.I2_rms))
        self.outLabel[4][2].config(text="{:.2f}".format(self.d1))
        self.outLabel[0][3].config(text="{:.2f}".format(self.d2))
        self.outLabel[1][1].config(text="{:.2f}".format(self.kBobInd))
        self.outLabel[2][0].config(text="{:.2f}".format(self.R))
        self.outLabel[2][1].config(text="{:.2f}".format(self.Co))
        self.outLabel[1][3].config(text="{:.2f}".format(self.length_p))
        self.outLabel[2][3].config(text="{:.2f}".format(self.length_s))
        self.outLabel[4][1].config(text="{:.2f}".format(self.Rs))
        self.outLabel[3][3].config(text="{:.2f}".format(self.Cs))



    
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
        self.tfall=75
        self.entry[2][3].insert(0,str(self.tfall))
screen = Page(root)
def unloading():
    screen.Giflabel.place_forget()
frameCnt = 29
frames = [PhotoImage(file='loading gif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]       
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    screen.Giflabel.configure(image=frame,bg="WHITE")
    screen.frame.after(100, update, ind)

def loadGif():    
    screen.Giflabel.place(x=screen.sW*0.5,y=screen.sH*0.5,width = 150,height=150,anchor=CENTER)
    screen.frame.after(0, update, 0)
class Page2:
    def __init__(self):
        self.help=Toplevel()
        self.help.title("HELP")
        self.a=int(0.55*screen.sW)
        self.help.geometry("%dx%d+%d+0" % (int(screen.sW*0.44), int(screen.sH*0.9),self.a))
        self.frame=Frame(self.help)
        self.page_init()
        self.show()
    def page_init(self):
        self.photo=Image.open("foto/help_page.png")
        self.photo= self.photo.resize((int(screen.sW*0.44), int(screen.sH*0.9)), Image.ANTIALIAS)
        self.helpPageImage = ImageTk.PhotoImage(self.photo)
        self.photo2=Image.open("foto/pdf.png")
        self.photo2= self.photo2.resize((int(screen.sW*0.0458), int(screen.sH*0.077)), Image.ANTIALIAS)
        self.pdfImage = ImageTk.PhotoImage(self.photo2)
        self.Giflabel = Label(root)

        self.labelImage=Label(self.help,width=int(screen.sW*0.44),height= int(screen.sH*0.9),bg="WHITE")
        self.pdfBtn=Button(self.help,command=self.pdf,activebackground="#1F4DC5",bg="#1F4DC5",borderwidth=0,image=self.pdfImage)
        
    def show(self):
        self.frame.place(x=0,y=0,width=int(screen.sW*0.44),height=int(screen.sH*0.9))
        self.labelImage.place(x=0,y=0)
        self.labelImage.config(image=self.helpPageImage)
        self.pdfBtn.place(y=screen.sH*0.715,x=screen.sW*0.061,width=screen.sW*0.0458,height=screen.sH*0.077,anchor=NW)
        self.help.mainloop()
    def pdf(self):
        root.after(0,loadGif)
        threadPdf.set()
        
def timer():
    while True:
        time.sleep(0.1)
        if threadPdf.is_set():
            os.system("pdf.pdf")
            screen.frame.after(100,unloading)

threadPdf=threading.Event()
t1= threading.Thread(target=timer)
t1.start()
screen = Page(root)
root.mainloop()