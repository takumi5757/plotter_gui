#import Libs
#import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')
import tkinter as Tk
import statistics as st

#Global Objects
global value
global value2

#Window title
root = Tk.Tk()
root.title(u"Plot_Graph Ver 1.0")
root.geometry("700x420")

#labeles
Static1 = Tk.Label(text=r"File Name")
Static1.pack(anchor=Tk.W)

#Entry
EditBox = Tk.Entry(width=70)
EditBox.insert(Tk.END,  "Input the file name.")
EditBox.pack(anchor=Tk.W)

def GetEditBoxValue(event):
    global value
    value = EditBox.get()
    print(value)

def GetEditBoxValue2(event):
    global value2
    value2 = EditBox2.get()
    print(value2)

def DeleteEntryValue(event):
    EditBox.delete(0, Tk.END)

def DeleteEntryValue2(event):
    EditBox2.delete(0, Tk.END)

#Button
Button_InputVal = Tk.Button(text=u'Input File Name', width=20)
Button_InputVal.bind("<Button-1>", GetEditBoxValue)
Button_InputVal.pack(anchor=Tk.W)

Button_Clear = Tk.Button(text=u'Clear File Name', width=20)
Button_Clear.bind("<Button-1>", DeleteEntryValue)
Button_Clear.pack(anchor=Tk.W)

#Labeles
Static2 = Tk.Label(text=u'Signal Name')
Static2.pack(anchor=Tk.W)

EditBox2 = Tk.Entry(width=70)
EditBox2.insert(Tk.END, "Input the signal name.")
EditBox2.pack(anchor=Tk.W)

#Button
Button_InputVal2 = Tk.Button(text=u'Input File Name', width=20)
Button_InputVal2.bind("<Button-1>", GetEditBoxValue2)
Button_InputVal2.pack(anchor=Tk.W)

Button_Clear2 = Tk.Button(text=u'Clear File Name', width=20)
Button_Clear2.bind("<Button-1>", DeleteEntryValue2)
Button_Clear2.pack(anchor=Tk.W)

def donothing():
    filein = Tk.Toplevel(root)
    button = Tk.Button(filein, text="Not Supported")
    button.pack()

#Create the Animation on the Graph
def UpdateData_Graph(event):
    #Set files name to read
    Kaikaku_FileName = value #Result of PZ1A file name

    SigName = value2

    #Set parameters
    PickUpSigName = SigName
    TitleName = PickUpSigName

    PickUpSigNameForFile = PickUpSigName.replace(".","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace("[","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace("]","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace(":","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace("/","_")

    KaikakuOutputFileName = PickUpSigNameForFile + 'csv'

    csv_input2 = pd.read_csv(filepath_or_buffer = Kaikaku_FileName, sep=",")
    csv_input2.to_csv(KaikakuOutputFileName, index = False, columns=[PickUpSigName])

    y = pd.read_csv(filepath_or_buffer=KaikakuOutputFileName, sep=",")
    x = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, usecols=[0])

    plt.title(TitleName)
    plt.xlabel('time')
    plt.grid(True)
    plt.plot(x,y)
    plot.show()


#Labeles
Static_Tollgate = Tk.Label(text=u'Plot Graph')
Static_Tollgate.place(x=500, y=305)

Button_TollMap = Tk.Button(text=u'Execute', width=20)
Button_TollMap.bind("<Button-1>", UpdateData_Graph)
Button_TollMap.place(x=500, y=330)

Static10 = Tk.Label(text=u'Copyright (c) 2020 Nissan Motor Co.,Ltd. All rights reserved')
Static10.pack(anchor=Tk.W)
Static10.place(x=0, y=390)

menubar = Tk.Menu(root)
filemenu = Tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save Result", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Tool", menu=filemenu)

helpmenu = Tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About us", command=donothing)
helpmenu.add_command(label="manual", command=donothing)
helpmenu.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

Tk.mainloop()
