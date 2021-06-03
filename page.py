#from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox,ttk,Tk,Frame,Label,Button,Entry,PhotoImage,END,Toplevel,NW,CENTER
import math
import os
import threading
import time
import subprocess

windowPage=0
tfall=[]
splitL=[]
splitP=[]
wireLengthTolerance=[]
additionalWinding=[]
effesiensi=[]
vinMax=[]
vinMin=[]
vOut=[]
iOut=[]
duty=[]
frekuensi=[]
rIl=[]
rVo=[]
Vf=[]
ac_ind=[]
dBob_ind=[]
ac_trafo=[]
dBob_trafo=[]
bMax=[]
j=[]
s=[]
sigma_split=[]
cnt=0

fulltext=[0 for x in range(88)]  
flag=0
scaleW=1
scaleH=1
root=Tk()

SCREENWIDTH_unscaled = int(root.winfo_screenwidth())
SCREENHEIGHT_unscaled = int(root.winfo_screenheight())
SCREENWIDTH = int(root.winfo_screenwidth()*scaleW)
SCREENHEIGHT = int(root.winfo_screenheight()*scaleH)
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(SCREENWIDTH, SCREENHEIGHT))
root.iconbitmap('logo.ico')
def clear(s):
    result=""
    for i in s:
        if i !='[' and i !=']':
            result=result+i
    return(result)
def splitter(s,maksChar):
    total =0
    result=""
    c = s.split()
    for i in range(len(c)):
        counter=len(c[i])
        total=total+counter
     
        if(total<maksChar):
            result=result+" "+c[i]
        else :
            result=result+"\n"+c[i]
            total=0
    return (result)
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
        # if self.flag==0:
        self.master.overrideredirect(False)
        self.flag=1
        scaleH=0.9


        # else:
        #     self.master.overrideredirect(True)
        #     self.flag=0
        #     scaleH=1
            
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
        self.master.title("HALF BRIDGE CALCULATION SOFTWARE")
        self.sW=SCREENWIDTH
        self.sH=SCREENHEIGHT
        self.frame=Frame(self.master,bg="RED")
        self.frame2=Frame(self.master,bg="RED")
        self.frame3=Frame(self.master,bg="#D7D3D3")
        self.entry =[[0 for x in range(6)]  for x in range(6)]
        self.outLabel =[[0 for x in range(5)]  for x in range(5)]
        self.btnHistory=[0 for x in range(88)]
        self.labelHistory=[0 for x in range(88)]   
        self.indeks=0
        self.page_init()
        self.showLayar()
        self.master.bind('<Enter>',self.off)
    def off(self,event):
        global proc
        threadPdf.clear()
        self.unloading()

        # os._exit()
        #sys.exit()
    def page_init(self):
        x=0
        self.Giflabel = Label(root)
        self.frame.place_forget()
        self.frame2.place_forget()
        self.frame3.place_forget()
        self.photo=Image.open("foto/awal.png")
        self.photo = self.photo.resize((self.sW, self.sH), Image.ANTIALIAS)
        self.gambar = ImageTk.PhotoImage(self.photo)
        self.photo2=Image.open("foto/tab2.png")
        self.photo2 = self.photo2.resize((self.sW, self.sH), Image.ANTIALIAS)
        self.gambar2 = ImageTk.PhotoImage(self.photo2)
        self.photo3=Image.open("foto/back.png")
        self.photo3 = self.photo3.resize((int(self.sW*0.032), int(self.sH*0.06)), Image.ANTIALIAS)
        self.backImage = ImageTk.PhotoImage(self.photo3)
        # self.photo4=Image.open("foto/calculate.png")
        # self.photo4 = self.photo4.resize((int(self.sW*0.132), int(self.sH*0.06)), Image.ANTIALIAS)
        # self.calculateImage = ImageTk.PhotoImage(self.photo4)
        self.photo5=Image.open("foto/reset.png")
        self.photo5 = self.photo5.resize((int(self.sW*0.1322), int(self.sH*0.0537)), Image.ANTIALIAS)
        self.resetImage = ImageTk.PhotoImage(self.photo5)
        self.photo6=Image.open("foto/default.png")
        self.photo6 = self.photo6.resize((int(self.sW*0.1322), int(self.sH*0.0537)), Image.ANTIALIAS)
        self.defaultImage = ImageTk.PhotoImage(self.photo6)
        self.photo7=Image.open("foto/help.png")
        self.photo7 = self.photo7.resize((int(self.sW*0.026), int(self.sH*0.0488)), Image.ANTIALIAS)
        self.helpImage = ImageTk.PhotoImage(self.photo7)
        self.photo8=Image.open("foto/history.png")
        self.photo8= self.photo8.resize((int(self.sW*0.062), int(self.sH*0.036)), Image.ANTIALIAS)
        self.historyImage = ImageTk.PhotoImage(self.photo8)
        self.photo9=Image.open("foto/history_page.png")
        self.photo9= self.photo9.resize((int(self.sW*0.312), int(self.sH*0.683)), Image.ANTIALIAS)
        self.historyPageImage = ImageTk.PhotoImage(self.photo9)
        self.photo10=Image.open("foto/history_bar.png")
        self.photo10= self.photo10.resize((int(self.sW*0.296), int(self.sH*0.083)), Image.ANTIALIAS)
        self.historyBarImage = ImageTk.PhotoImage(self.photo10)
        self.photo11=Image.open("foto/close.png")
        self.photo11= self.photo11.resize((int(self.sW*0.0145), int(self.sH*0.027)), Image.ANTIALIAS)
        self.closeImage = ImageTk.PhotoImage(self.photo11)

        self.labelImage=Label(self.frame,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar)
        self.labelImage2=Label(self.frame2,height=SCREENHEIGHT,width=SCREENWIDTH,image=self.gambar2)
        self.labelImage3=Label(self.frame3,height=self.sH*0.683,width=self.sW*0.312,image=self.historyPageImage)
        self.exitButton = Button(self.frame,command=self.exit,bg="#EF5858",text="EXIT",font='Helvetica 30 bold')
        self.exitButton2 = Button(self.frame2,command=self.exit,bg="#EF5858",text="EXIT",font='Helvetica 20 bold')
        self.startButton = Button(self.frame,command=self.start,bg="#9561EB",text="START",font='Helvetica 30 bold')
        self.backBtn=Button(self.frame2,image=self.backImage,command=self.back)
        self.calculateBtn=Button(self.frame2,activebackground="#1687A7",command=self.calculate,borderwidth=0,bg="#1687A7",text="calculate",font='Helvetica 20 bold')
        self.resetBtn=Button(self.frame2,activebackground="#67B840",image=self.resetImage,command=self.reset,borderwidth=0,bg="#67B840")
        self.defaultBtn=Button(self.frame2,command=self.default,image=self.defaultImage,activebackground="#67B840",bg="#67B840",borderwidth=0)
        self.helpBtn=Button(self.frame2,command=self.help,image=self.helpImage,activebackground="#40AD0C",bg="#40AD0C",borderwidth=0)
        self.historyBtn=Button(self.frame2,command=self.history,image=self.historyImage,activebackground="#40AD0C",bg="#40AD0C",borderwidth=0)
        self.closeBtn=Button(self.frame3,command=self.close,image=self.closeImage,activebackground="#687BDC",bg="#687BDC",borderwidth=0)
        self.rekomBtn=Button(self.frame2,text="CEK REKOMENDASI",command=self.popRekomen)
        
        #self.entry[0][0]=Entry(self.frame2,font=20)
        for x in range(6):
            for y in range(5):    
                self.entry[x][y] = Entry(self.frame2,font='Helvetica 13 bold',justify='center')
        for j in range(5):
            for k in range(5):    
                self.outLabel[j][k] = Label(self.frame2,font='Helvetica 13 bold',bg="#7BD152")
        for z in range(80):
            self.btnHistory[z]=Button(self.frame3,image=self.historyBarImage,bg="#D7D3D3",borderwidth=0,activebackground="#D7D3D3")
            self.btnHistory[z].config(command=lambda x=z:self.btnHistory_func(x))
            self.labelHistory[z]=Label(self.frame3,bg="WHITE",borderwidth=0)  
        self.show_historyPage()
    def popRekomen(self):
               # print(self.rekom(self.Co,self.vOut,1))
        
        # print(self.rekom(self.Cs,1000,3))
        try:
            text="Co="+self.rekom(self.Co,self.vOut,1)+"\n"+"Cs="+self.rekom(self.Cs,1000,3)+"\nRs="+self.rekom(self.Rs,10,2)
            messagebox.showinfo(title="REKOMENDASI", message=text)
        except:
            messagebox.showerror(title="ERROR DETECTED!",message="rating terlalu besar, pastikan sudah memasukkan parameter dengan benar")
    def rekom(self,nilai,rate,flag):
        self.dataCo=[0.1,0.22,0.33,0.47,1,2.2,3.3,4.7,10,22,33,47,100,220,330,470,1000,2200,3300]
        self.voltrate=[10,16,35,50,63,100,250,400,500,1000,2000,3000,4000]
        self.resistor=[0.1,0.12,0.15,0.18,0.2,0.22,1,1.2,1.5,1.8,2,2.2,2.7,3.3,3.9,4.7,5.1,5.6,6.8,8.2,10,12,15,18,22,27,33,39,47,56,68,75,82,100,120,150,180,220,270,330,390,470,560,680,820,1000,1200,1500,1800,2200,2700,3300,3900,4700,5600,6800]
        self.resistorRate=[0.25,0.5,9,10,11,13,14,15,16,17]
        if flag==1:
            for x in self.dataCo:
                if x>=nilai:
                    hasil=x
                    break
            for y in self.voltrate:
                if y >= 2*rate:
                    rating=y
                    break
                    
            result=str(hasil)+"mikro Farad"+","+str(rating)+"volt"

        elif flag==2:
            for x in self.resistor:
                if x>=nilai/2:
                    hasil=x
                    break
            for y in self.resistorRate:
                if y>=rate:
                    rating=y
                    break
            result=str(hasil)+"ohm"+","+str(rating)+"watt"
        elif flag==3:
            for x in self.dataCo:
                if x>=nilai:
                    hasil=x
                    break
            for y in self.voltrate:
                if y >=rate:
                    rating=y
                    break
            result=str(hasil)+"nano Farad"+","+str(rating)+"volt"            
        return result

            
        

    def btnHistory_func(self,x):
        global splitL,splitP,wireLengthTolerance,additionalWinding,vinMax,vinMin,vOut,iOut,duty,frekuensi,rIl,rVo,Vf,ac_ind,dBob_ind,ac_trafo,dBob_trafo,bMax,j,s,sigma_split,tfall,cnt,fulltext
        
        self.reset()
        self.vinMax=vinMax[x]
        self.entry[0][0].insert(0,str(self.vinMax))
        self.effesiensi=effesiensi[x]
        self.entry[1][0].insert(0,str(self.effesiensi))
        self.vOut=vOut[x]
        self.entry[2][0].insert(0,str(self.vOut))
        self.iOut=iOut[x]
        self.entry[3][0].insert(0,str(self.iOut))
        self.duty=duty[x]
        self.entry[4][0].insert(0,str(self.duty))
        self.tfall=tfall[x]
        self.entry[5][0].insert(0,str(self.tfall))
        

        self.frekuensi=frekuensi[x]
        self.entry[0][1].insert(0,str(self.frekuensi))
        self.rIl=rIl[x]
        self.entry[1][1].insert(0,str(self.rIl))
        self.rVo=rVo[x]
        self.entry[2][1].insert(0,str(self.rVo))
        self.vf=Vf[x]
        self.entry[3][1].insert(0,str(self.vf))
        self.acInd=ac_ind[x]
        self.entry[4][1].insert(0,str(self.acInd))
        self.additionalWInding=additionalWinding[x]
        self.entry[5][1].insert(0,str(self.additionalWInding))

        self.dBobInd=dBob_ind[x]
        self.entry[0][2].insert(0,str(self.dBobInd))
        self.acTraf=ac_trafo[x]
        self.entry[1][2].insert(0,str(self.acTraf))
        self.dBobTraf=dBob_trafo[x]
        self.entry[2][2].insert(0,str(self.dBobTraf))
        self.bMax=bMax[x]
        self.entry[3][2].insert(0,str(self.bMax))
        self.J=j[x]
        self.entry[4][2].insert(0,str(self.J))
        self.wireLengthTolerance=wireLengthTolerance[x]
        self.entry[5][2].insert(0,str(self.wireLengthTolerance))

        self.splitP=splitP[x]
        self.entry[0][3].insert(0,str(self.splitP))
        self.splitL=splitL[x]
        self.entry[1][3].insert(0,str(self.splitL))
        # self.tfall=tfall[x]
        # self.entry[2][3].insert(0,str(self.tfall))
    def close(self):
        self.frame3.place_forget()
    def unloading(self):
        self.Giflabel.place_forget()
    def showLayar(self):
        global windowPage
        if windowPage==0:
            self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH)
            self.labelImage.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH)
            self.exitButton.place(x=self.sW*0.573 ,y=self.sH*0.77,width=self.sW*0.251,height=self.sH*0.1)
            self.startButton.place(x=self.sW*0.215 ,y=self.sH*0.77,width=self.sW*0.251,height=self.sH*0.1)
        elif windowPage==1:
            self.start()
    def exit(self):
        a=messagebox.askyesno(title="EXIT?",message="Apakah anda yakin ingin menutup aplikasi?")
        if a == True:
            root.destroy()
        
    def start(self):
        global windowPage
        windowPage=1
        self.frame.place_forget()
        self.frame2.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH)
        self.labelImage2.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH)
        self.backBtn.place(x=self.sW*0.01,y=self.sH*0.02,width=self.sW*0.032, height=self.sH*0.06)
        self.calculateBtn.place(x=self.sW*0.774,y=self.sH*0.298,width=self.sW*0.132, height=self.sH*0.1)
        self.resetBtn.place(x=self.sW*0.774,y=self.sH*0.47,width=self.sW*0.1322, height=self.sH*0.0537)
        self.defaultBtn.place(x=0.773*self.sW,y=self.sH*0.411,width=self.sW*0.1322,height=self.sH*0.0537)
        self.helpBtn.place(x=0.962*self.sW,y=self.sH*0.0175,width=self.sW*0.026,height=self.sH*0.0488)
        self.historyBtn.place(x=0.892*self.sW,y=self.sH*0.0244,width=self.sW*0.062,height=self.sH*0.036)
        self.exitButton2.place(x=0.77*self.sW,y=0.011*self.sH,width=0.09*self.sW,height=0.054*self.sH)
        
       
        j=0
        k=0
        x=0
        y=0
        offsetH=self.sH*0.173
        offsetW=self.sW*0.181
        jarakW=self.sW*0.141
        jarakH=self.sH*0.0146
        entryWidth=self.sW*0.065
        entryHeight=self.sH*0.044
        
        for j in range(6):
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
        self.entry[5][3].place_forget()

        # self.outLabel[4][1].place_forget()
        # self.outLabel[3][3].place_forget()
        #self.outLabel[4][3].place_forget()
   
        self.master.bind('<Return>',self.enter)
        self.reset()
        self.default()
        # self.calculate()
    def history(self):
        global vinMax,cnt
        a = len(vinMax)
        self.frame3.place(x=self.sW*0.68,y=self.sH*0.036,width=self.sW*0.312,height=self.sH*0.683)
        self.labelImage3.place(x=0,y=0,height=self.sH*0.683,width=self.sW*0.312)
        self.closeBtn.place(x=self.sW*0.289,y=self.sH*0.0117,width=self.sW*0.0145,height=self.sH*0.027)
        for x in range (a):
            self.labelHistory[x].bind('<Button-1>',lambda event,obj=x:self.btnHistory_event(event,obj))
    def btnHistory_event(self,event,a):
        self.btnHistory_func(a)
    def help(self):
        self.page=Page2()

        
    def enter(self,event):
        self.calculate()
        

    def back(self):
        global windowPage
        windowPage=0
        self.showLayar()
        self.frame2.place_forget()
        self.frame.place(x=0,y=0,height=SCREENHEIGHT,width=SCREENWIDTH)
        self.master.unbind('<Return>')
    def calculate(self):
        global vinMax,cnt
        try:
            self.hitung()
            self.show_historyPage()
            
        except ValueError :
             messagebox.showerror("warning","ganti koma(,) dengan titik(.) untuk pecahan dan pastikan semua parameter terisi(jika tidak digunakan isi dengan nol(0))")
        
    def show_historyPage(self):
        global vinMax,cnt
        a=len(vinMax)
        jarak = self.sH*0.0094
        offsetH= self.sH*0.0732
        offsetW = self.sW*0.00729
        width = self.sW*0.296
        height = self.sH*0.083

        jarak2 = self.sH*0.03
        offsetH2= self.sH*0.083
        offsetW2 = self.sW*0.0625
        width2 = self.sW*0.222
        height2 = self.sH*0.063
        
       
        for x in range(a):
            if x < 6:
                self.btnHistory[x].place(x=offsetW,y=offsetH+(x*(jarak+height)),width=width,height=height)
                self.labelHistory[x].place(x=offsetW2,y=offsetH2+(x*(jarak2+height2)),width=width2,height=height2)
                fulltext[x]="vin="+str(vinMax[x])+"v"+" eff="+str(effesiensi[x])+"%"+" vOut="+str(vOut[x])+"v"+"Iout="+str(iOut[x])+"A"+" D="+str(duty[x])+"%"+" tfall="+str(tfall[x])+"ns"+" f="+str(frekuensi[x])+"kHz"+" rIl="+str(rIl[x])+"%"+" rVo="+str(rVo[x])+"%"+" Vf="+str(Vf[x])+"volt"+" ac_ind="+str(ac_ind[x])+"cm2"+" dBob_ind="+str(dBob_ind[x])
                self.labelHistory[x].config(text=splitter(fulltext[x],45))
    def reset(self):
        for x in range(6):
            for y in range(5):
                self.entry[x][y].delete(0,END)
        for x in range(5):
            for y in range(5):    
                self.outLabel[x][y].config(text="")
        self.rekomBtn.place_forget()
    def hitung(self):
        global vinMax,vinMin,vOut,iOut,duty,frekuensi,rIl,rVo,Vf,ac_ind,dBob_ind,ac_trafo,dBob_trafo,bMax,j,s,sigma_split,tfall,cnt,fulltext,effesiensi,additionalWinding,wireLengthTolerance,splitL,splitP
        
        self.vinMax=float(self.entry[0][0].get())
        self.effesiensi=float(self.entry[1][0].get())
        self.vOut=float(self.entry[2][0].get())
        self.iOut=float(self.entry[3][0].get())
        self.duty=float(self.entry[4][0].get())
        self.tfall=float(self.entry[5][0].get())
        vinMax.insert(0,self.vinMax)
        vinMin.insert(0,self.vinMin)
        effesiensi.insert(0,self.effesiensi)
        vOut.insert(0,self.vOut)
        iOut.insert(0,self.iOut)
        duty.insert(0,self.duty)
        tfall.insert(0,self.tfall)



        self.frekuensi=float(self.entry[0][1].get())
        self.rIl=float(self.entry[1][1].get())
        self.rVo=float(self.entry[2][1].get())
        self.vf=float(self.entry[3][1].get())
        self.acInd=float(self.entry[4][1].get())
        self.additionalWInding=float(self.entry[5][1].get())
        frekuensi.insert(0,self.frekuensi)
        rIl.insert(0,self.rIl)
        rVo.insert(0,self.rVo)
        Vf.insert(0,self.vf)
        ac_ind.insert(0,self.acInd)
        additionalWinding.insert(0,self.additionalWInding)
        


        self.dBobInd=float(self.entry[0][2].get())
        self.acTraf=float(self.entry[1][2].get())
        self.dBobTraf=float(self.entry[2][2].get())
        self.bMax=float(self.entry[3][2].get())
        self.J=float(self.entry[4][2].get())
        self.wireLengthTolerance=float(self.entry[5][2].get())
        dBob_ind.insert(0,self.dBobInd)
        ac_trafo.insert(0,self.acTraf)
        dBob_trafo.insert(0,self.dBobTraf)
        bMax.insert(0,self.bMax)
        j.insert(0,self.J)
        wireLengthTolerance.insert(0,self.wireLengthTolerance)
        self.dBobTraf=self.dBobTraf*0.1

        self.splitP=float(self.entry[0][3].get())
        self.splitL=float(self.entry[1][3].get())
        # self.tfall=float(self.entry[2][3].get())

        splitP.insert(0,self.splitP)
        splitL.insert(0,self.splitL)
        # tfall.insert(0,self.tfall)
        
        self.s=4.5
        #RUMUS
        self.duty=self.duty/100
        self.frekuensi=self.frekuensi*1000
        self.rIl=self.rIl/100
        self.rVo=self.rVo/100
        self.dBobInd=self.dBobInd/10
        self.tfall=self.tfall*0.000000001
        self.rasio = self.vOut/(self.vinMax*self.duty)
       

        #Lx
        self.vin_a=self.vinMax/(2*(1/self.rasio)-(2*self.vf))
        self.dIlx = self.rIl*self.iOut
        self.Lx=(1/self.dIlx)*(self.vin_a-self.vOut)*(1/(2*self.frekuensi))*(((self.vOut+(2*self.vf))/(self.vinMax+(2*self.vf))))
 

        #iL(avg) & iL(max)
        self.iL_avg = self.iOut
        self.iL_max = self.iL_avg+(self.dIlx/2)


        #winding number
        self.n=((self.Lx*self.iL_max)/(self.bMax*self.acInd))*pow(10,4)
        #airgap
        self.airGap=((4*3.14*0.0000001*self.Lx*math.pow(self.iL_max,2))/(math.pow(self.bMax,2)*self.acInd))*10000
        print(self.Lx)
        #wire size
        self.iL_rms_split=self.iL_avg/self.splitL
        self.qwL_split=self.iL_rms_split/self.J
        self.dwL_split=math.sqrt(4*self.qwL_split/3.14)
        self.kBobInd = 3.14*self.dBobInd
        self.wireLength = (math.ceil(self.n)*self.kBobInd*self.splitL)+(0.4*(self.n*self.kBobInd*self.splitL))
      

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
        # #d1 dan d2
        # self.d1=math.sqrt((4*self.I1_rms)/(3.14*self.s))
        # self.d2=math.sqrt((4*self.I2_rms)/(3.14*self.s))

        #R
        self.R=self.vOut/self.iOut
        #d1/dw primer
        self.i1_rms_split=self.I1_rms/self.splitP
        self.qwp_split=self.i1_rms_split/self.J
        self.dwp_split=math.sqrt(4*self.qwp_split/3.14)
        #split sekunder
        self.dws_split=self.dwp_split

        self.qws_split=(pow(self.dws_split,2)*3.14)/4
        self.I2_rms_split=self.J*self.qws_split
        self.splitS=self.I2_rms/self.I2_rms_split
        # print(self.I2_rms)
        # print(self.qws_split)
        #wire lengh trafo
        self.kBobTraf=3.14*self.dBobTraf
        self.length_p=(self.N1*self.kBobTraf*self.splitP)+(0.3*(self.N1*self.kBobTraf*self.splitP))
        self.length_s=(self.N2*self.kBobTraf*self.splitS)+(0.3*(self.N2*self.kBobTraf*self.splitS))
        self.totalLength=self.length_p+self.length_s
        #Co
        self.dVo=self.rVo*self.vOut
        self.Co=((1-self.duty)/(8*self.Lx*pow(2*self.frekuensi,2)))*(self.vOut/self.dVo)
        #LM
        self.Lm=((self.vin_a*self.duty*self.T)/(0.2*(self.I1_rms+(self.rasio*self.I2_rms))))
        #Rs dan Cs
        self.ion=self.iOut
        self.voff=(self.vinMax/2)-(self.Lx*(self.dIlx/(self.duty*self.T)))-self.vOut
        self.Cs = (self.ion*self.tfall)/(2*self.voff)
    
        self.Rs=(self.duty*self.T)/(2*self.Cs)
        self.Lm=self.Lm*1000000
        self.Lx=self.Lx*1000000
        self.Co=self.Co*1000000
        self.length_p=self.length_p/100
        self.length_s=self.length_s/100
        self.totalLength=math.ceil(self.length_p)+math.ceil(self.length_s)
        # print(self.length_s)
        self.wireLength=self.wireLength/100
        self.Cs=self.Cs*1000000000
        self.airGap=self.airGap*1000

        self.outLabel[0][0].config(text="{:.2f}".format(self.rasio))
        self.outLabel[1][0].config(text="{:.2f}".format(self.I2_rms))
        self.outLabel[2][0].config(text="{:.0f}".format(math.ceil(self.N1)))
        self.outLabel[3][0].config(text="{:.0f}".format(math.ceil(self.N2)))
        self.outLabel[4][0].config(text="{:.0f}".format(math.ceil(self.splitS)))

        self.outLabel[0][1].config(text="{:.2f}".format(self.dwp_split))
        self.outLabel[1][1].config(text="{:.2f}".format(self.kBobTraf))
        self.outLabel[2][1].config(text="{:.0f}".format(math.ceil(self.length_p)))
        self.outLabel[3][1].config(text="{:.0f}".format(math.ceil(self.length_s)))
        self.outLabel[4][1].config(text="{:.0f}".format(math.ceil(self.totalLength)))
        # print(self.length_p)
        # print(self.length_s)
        
        
        self.outLabel[0][2].config(text="{:.0f}".format(math.ceil(self.Lx)))
        self.outLabel[1][2].config(text="{:.0f}".format(math.ceil(self.n)))
        self.outLabel[2][2].config(text="{:.4f}".format(self.airGap))
        self.outLabel[3][2].config(text="{:.2f}".format(self.dwL_split))
        self.outLabel[4][2].config(text="{:.0f}".format(math.ceil(self.wireLength)))
        
        self.outLabel[0][3].config(text="{:.0f}".format(math.ceil(self.Co))) 
        self.outLabel[1][3].config(text="{:.2f}".format(self.ion))
        self.outLabel[2][3].config(text="{:.2f}".format(self.voff))
        self.outLabel[3][3].config(text="{:.0f}".format(math.ceil(self.Cs)))
        self.outLabel[4][3].config(text="{:.0f}".format(math.ceil(self.Rs)))
        cnt=cnt+1
        # self.popRekomen()
        self.rekomBtn.place(x=0.736*self.sW,y=self.sH*0.555,width=0.1234*self.sW,height=self.sH*0.0263)
        # print(self.rekom(self.Co,self.vOut,1))
        
        # print(self.rekom(self.Cs,1000,3))
        
    
    def default(self):
        self.reset()
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
        self.tfall=75
        self.entry[5][0].insert(0,str(self.tfall))

        self.frekuensi=40
        self.entry[0][1].insert(0,str(self.frekuensi))
        self.rIl=20
        self.entry[1][1].insert(0,str(self.rIl))
        self.rVo=0.1
        self.entry[2][1].insert(0,str(self.rVo))
        self.vf=1.5
        self.entry[3][1].insert(0,str(self.vf))
        self.acInd=1.61
        self.entry[4][1].insert(0,str(self.acInd))
        self.additionalWInding=3
        self.entry[5][1].insert(0,str(self.additionalWInding))


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
        self.wireLengthTolerance=30
        self.entry[5][2].insert(0,str(self.wireLengthTolerance))

        self.splitP=1.6
        self.entry[0][3].insert(0,str(self.splitP))
        self.splitL=9.6
        self.entry[1][3].insert(0,str(self.splitL))
        self.tfall=25
        self.entry[2][3].insert(0,str(self.tfall))
screen = Page(root)

frameCnt = 29
frames = [PhotoImage(file='foto/loading gif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]       
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    screen.Giflabel.configure(image=frame,bg="WHITE")
    screen.frame.after(100, update, ind)

def loadGif():    
    screen.Giflabel.place(x=SCREENWIDTH_unscaled*0.5,y=SCREENHEIGHT_unscaled*0.5,width = 150,height=150,anchor=CENTER)
    screen.frame.after(0, update, 0)
class Page2:
    def __init__(self):
        self.help=Toplevel()
        self.help.bind('<Escape>',app.escape)
        self.help.bind('<F>',app.full)
        self.help.bind('<f>',app.full)
        self.help.title("HELP PAGE")
        self.a=int(0.55*screen.sW)
        self.help.geometry("%dx%d+%d+0" % (int(screen.sW*0.44), int(screen.sH*0.9),self.a))
        self.frame=Frame(self.help)
        self.help.resizable(0,0)
        self.help.attributes('-toolwindow', True)
        #root.after(0,loadGif)
        self.page_init()
        self.show()
    def page_init(self):
        self.photo=Image.open("foto/help_page.png")
        self.photo= self.photo.resize((int(screen.sW*0.44), int(screen.sH*0.9)), Image.ANTIALIAS)
        self.helpPageImage = ImageTk.PhotoImage(self.photo)
        self.photo2=Image.open("foto/pdf.png")
        self.photo2= self.photo2.resize((int(screen.sW*0.0458), int(screen.sH*0.077)), Image.ANTIALIAS)
        self.pdfImage = ImageTk.PhotoImage(self.photo2)
        

        self.labelImage=Label(self.help,width=int(screen.sW*0.44),height= int(screen.sH*0.9),bg="WHITE")
        self.pdfBtn=Button(self.help,command=self.pdf,activebackground="#1F4DC5",bg="#1F4DC5",borderwidth=0,image=self.pdfImage)
        
    def show(self):
        self.frame.place(x=0,y=0,width=int(screen.sW*0.44),height=int(screen.sH*0.9))
        self.labelImage.place(x=0,y=0)
        self.labelImage.config(image=self.helpPageImage)
        self.pdfBtn.place(y=screen.sH*0.715,x=screen.sW*0.061,width=screen.sW*0.0458,height=screen.sH*0.077,anchor=NW)
        self.help.mainloop()
    def pdf(self):
        global flag
        
        if flag == 0:
            self.help.after(0,loadGif)
            threadPdf.set()
            flag=1
        else:
            messagebox.showerror("warning","File PDF MANUAL CALCULATION SUDAH TERBUKA SILAHKAN CEK PADA TASKBAR ANDA")
        app.escape(root)
def kill():
    
    screen.unloading()
def timer():
    global flag,proc
    while True:
        time.sleep(0.1)

        if threadPdf.is_set():
            threadPdf.clear()
            #screen.frame.after(1000,kill)
            # os.open("pdf.pdf")
            subprocess.Popen(["pdf.pdf"], shell=True)
            flag=0

            

threadPdf=threading.Event()
t1= threading.Thread(target=timer)
t1.start()


root.mainloop()