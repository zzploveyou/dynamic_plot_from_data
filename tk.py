#coding:utf8
from Tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

filename="123.txt"
entrys=["one","two","three"]
dic={}
id=0
now_time=0
num=len(entrys)

for line_f in open(filename):
    tmp=line_f.strip().split("\t")
    for i in range(0,num):
        if(entrys[i] not in dic):
            dic[entrys[i]]=[float(tmp[i])]
        else:
            dic[entrys[i]].append(float(tmp[i]))

total_time=len(dic[entrys[0]])

def update(data):
    line.set_xdata(range(len(data)))
    line.set_ydata(data)
    color_list()
    print data
    return line,

def color_list():
    '''
    for index in range(len(entrys)):
        if(dic[entrys[index]][listbox.curselection()[0]]>0.5):
            listbox.itemconfig(index,bg='red')
    '''

    if(dic[entrys[0]][now_time]>0.5):
        listbox.itemconfig(0,bg='red')
    else:
        listbox.itemconfig(0,bg='blue')

    if(dic[entrys[1]][now_time]>15):
        listbox.itemconfig(1,bg='red')
    else:
        listbox.itemconfig(1,bg='blue')

    if(dic[entrys[2]][now_time]>50):
        listbox.itemconfig(2,bg='red')
    else:
        listbox.itemconfig(2,bg='blue')

def data_gen():
    while(True):
        #yield dic[entrys[id]][:now_time+1]
        global now_time
        now_time +=1
        print now_time
        id=listbox.curselection()[0]
        data=dic[entrys[id]][:now_time+1]
        plt.axis([0,now_time,min(data)*0.8,max(data)*1.2])
        yield data

def plot_sec(id,now_time):
    if(now_time<total_time):
        xx=range(0,now_time)
        yy=dic[entrys[id]][:now_time]
        #print xx,yy
        #print len(xx),len(yy)
        fig=plt.figure()
        axes1=fig.add_subplot(111)
        line,=axes1.plot(yy)
        global line
        ani=animation.FuncAnimation(fig,update,data_gen,interval=1000)
        plt.show()

def plot_canvas(event):
    id=listbox.curselection()[0]
    plot_sec(id,now_time)
    #print listbox.get(listbox.curselection())
    #id=listbox.curselection()[0]
    #canvas.create_line((1,2),(3,4),(5,6),width=5,)
class App:
    def __init__(self,master):
        self.frame=Frame(master)
        #LEFT
        self.frmL=Frame(self.frame)

        self.frmLT=Frame(self.frmL)
        Label(self.frmLT, text = '指标搜索:').pack(side=LEFT)
        Entry(self.frmLT,width=8).pack(side=RIGHT)
        self.frmLT.pack(side=TOP)
        
        self.frmLB=Frame(self.frmL)
        scrollbar = Scrollbar(self.frmLB,width=10)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox=Listbox(self.frmLB,selectmode=BROWSE,yscrollcommand=scrollbar.set)
        global listbox
        for item in entrys:
            listbox.insert(END,item)
        #listbox.itemconfig(1,bg='black')
        listbox.pack(side=LEFT,fill=BOTH)
        listbox.bind("<Double-Button-1>",plot_canvas)
        #listbox.bind("<Double-Button-1>",App.plot_canvas(listbox.curselection()))
        scrollbar.config(command=listbox.yview)
        self.frmLB.pack(side=BOTTOM)
        self.frmL.pack(side=LEFT)
        #RIGHT
        '''
        self.frmR=Frame(self.frame)
        canvas=Canvas(self.frmR,bg="white")
        global canvas
        canvas.pack()
        self.frmR.pack(side=LEFT)
        '''
        self.frame.pack()

if __name__=='__main__':
    root=Tk()
    app=App(root)
    root.mainloop()
    root.destroy()
