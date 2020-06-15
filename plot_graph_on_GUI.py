import pandas as pd
import matplotlib.pyplot as plt
import tkinter as Tk
import statistics as st


def hexadecimal_to_decimal(df, PickUpSigName):
    """ 
    16進数のデータを10進数に変換,0x◯◯のようなデータも扱う
    "0x◯◯"がstr型の場合に動作
    @params:
        df: pd.DataFrame
    @return:
        df: pd.DataFrame
    """
    map_obj = map(lambda x: int(x, base=16), df[PickUpSigName])
    df = pd.DataFrame(map_obj, columns=[PickUpSigName])
    return df

#Create the Animation on the Graph
def UpdateData_Graph(event):
    #Set files name to read
    Kaikaku_FileName = value #Result of PZ1A file name
    Kaikaku_FileName2 = value3
    SigName = value2

    #Set parameters
    PickUpSigName = SigName
    TitleName = PickUpSigName

    PickUpSigNameForFile = PickUpSigName.replace(".","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace("[","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace("]","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace(":","_")
    PickUpSigNameForFile = PickUpSigNameForFile.replace("/","_")

    KaikakuOutputFileName = PickUpSigNameForFile + '.csv'
    KaikakuOutputFileName2 = PickUpSigNameForFile + '2.csv'

    csv_input2 = pd.read_csv(filepath_or_buffer = Kaikaku_FileName, sep=",")
    csv_input2.to_csv(KaikakuOutputFileName, index = False, columns=[PickUpSigName])

    csv_input2 = pd.read_csv(filepath_or_buffer = Kaikaku_FileName2, sep=",")
    csv_input2.to_csv(KaikakuOutputFileName2, index = False, columns=[PickUpSigName])

    y_1 = pd.read_csv(filepath_or_buffer=KaikakuOutputFileName, sep=",")
    y_2 = pd.read_csv(filepath_or_buffer=KaikakuOutputFileName2, sep=",")
    x = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, usecols=[0])

    #暫定的な処理
    if type(y_1[PickUpSigName][1]) is str:
        y_1 = hexadecimal_to_decimal(y_1, PickUpSigName)

    if type(y_2[PickUpSigName][1]) is str:
        y_2 = hexadecimal_to_decimal(y_2, PickUpSigName)
    """
    if "0x" in y_1[PickUpSigName][1]:
        pass
    if "0x" in y_2[PickUpSigName][1]:
        pass
    """
    plt.title(TitleName)
    plt.xlabel('time')
    plt.grid(True)
    plt.plot(x, y_1)
    plt.plot(x, y_2)
    plt.show()
    plt.savefig(f'png/{PickUpSigNameForFile}.png')#動いてない


def set_menubar(root):

    def donothing():
        filein = Tk.Toplevel(root)
        button = Tk.Button(filein, text="Not Supported")
        button.pack()

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

def set_gui():

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

    def GetEditBoxValue3(event):
        global value3
        value3 = EditBox3.get()
        print(value3)

    def DeleteEntryValue3(event):
        EditBox3.delete(0, Tk.END)

    #labeles
    Static1 = Tk.Label(text=r"File Name")
    Static1.pack(anchor=Tk.W)

    #Entry
    EditBox = Tk.Entry(width=70)
    EditBox.insert(Tk.END,  "Input the file name.")
    EditBox.pack(anchor=Tk.W)

    #Button
    Button_InputVal = Tk.Button(text=u'Input File Name', width=20)
    Button_InputVal.bind("<Button-1>", GetEditBoxValue)
    Button_InputVal.pack(anchor=Tk.W)

    Button_Clear = Tk.Button(text=u'Clear File Name', width=20)
    Button_Clear.bind("<Button-1>", DeleteEntryValue)
    Button_Clear.pack(anchor=Tk.W)

    #Entry
    EditBox3 = Tk.Entry(width=70)
    EditBox3.insert(Tk.END,  "Input the file name.")
    EditBox3.pack(anchor=Tk.W)

    #Button
    Button_InputVal3 = Tk.Button(text=u'Input File Name', width=20)
    Button_InputVal3.bind("<Button-1>", GetEditBoxValue3)
    Button_InputVal3.pack(anchor=Tk.W)

    Button_Clear3 = Tk.Button(text=u'Clear File Name', width=20)
    Button_Clear3.bind("<Button-1>", DeleteEntryValue3)
    Button_Clear3.pack(anchor=Tk.W)

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

    #Labeles
    Static_Tollgate = Tk.Label(text=u'Plot Graph')
    Static_Tollgate.place(x=500, y=305)

    Button_TollMap = Tk.Button(text=u'Execute', width=20)
    Button_TollMap.bind("<Button-1>", UpdateData_Graph)
    Button_TollMap.place(x=500, y=330)

    Static10 = Tk.Label(text=u'Copyright (c) 2020 Nissan Motor Co.,Ltd. All rights reserved')
    Static10.pack(anchor=Tk.W)
    Static10.place(x=0, y=390)


def main():
    #Global Objects
    global value
    global value2
    global value3

    #Window title
    root = Tk.Tk()
    root.title(u"Plot_Graph Ver 1.0")
    root.geometry("700x420")

    set_gui()

    set_menubar(root)

    Tk.mainloop()


if __name__ == "__main__":
    main()