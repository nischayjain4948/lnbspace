from tkinter import *
import time

root=Tk()
root.title("N_T Calculator")
#root.geometry("400x400")
root.config(bg="white")
root.iconbitmap(r'D:\calculator\ntlogo.ico')
def Result(x):
    if x=="=":
        try:
            s1.set(eval(s1.get()))
        
        except Exception as e:
            s1.set(e)
    elif x=="C":
        s1.set("")
    elif x=="CE":
        data=s1.get()
        data=data[:len(data)-1]
        s1.set(data)
    else:
        s1.set(s1.get()+x)


def onbutton(e):
    b1['bg']='white'

def leavebutton(e):
    b1['bg']='grey'
        
s1=StringVar()
e1=Entry(root,textvariable=s1,font="arial 20 bold",bg="white",justify=RIGHT,relief="raised")
e1.grid(row=0,column=0,columnspan=4,padx=5,pady=5,ipadx=10,ipady=10,sticky="nswe")
i=1
for data in ["789/","456*","123+",".0-=",["C","CE"]]:
    j=0
    for t in data:
        b1=Button(root,text=t,font="arial 20 bold",bg="grey",relief="raised",
                  command=lambda x=t:Result(x))

        
        if t in ['C','CE']:
            b1.grid(row=i,column=j,columnspan=2,padx=5,pady=5,ipadx=10,ipady=10,sticky="nswe")
            j+=2
        else:
            b1.grid(row=i,column=j,padx=5,pady=5,ipadx=10,ipady=10,sticky="nswe")
            j+=1
    i+=1
def Display():
    l1['text']=time.ctime()
    l1.after(1000,Display)
l1=Label(root,font="arial 20 bold",bg="#c0c0c0",relief="raised")
l1.grid(row=6,column=0,columnspan=4,padx=10,pady=10,ipadx=10,ipady=10,sticky="nswe")


Display()
for i in range(7):
    root.rowconfigure(i,weight=1)

for i in range(4):
    root.columnconfigure(i,weight=20)
root.mainloop()
