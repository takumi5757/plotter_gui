import tkinter as tk
import random as rd
import time
import pandas as pd
import matplotlib.pyplot as plt

class Model():
    def __init__(self):
        self.width=700
        self.height=420


class View():
    def __init__(self,master,model):
        self.master = master
        self.model = model

        self.filename = tk.StringVar(value="Input the File Name or Path.")
        self.filename2 = tk.StringVar(value="Input the File Name or Path.")

        self.view1()
        self.view2()
        self.view3()
        self.view4()
        self.menu()

        self.Static10 = tk.Label(text=u'Copyright (c) 2020 Nissan Motor Co.,Ltd. All rights reserved')
        self.Static10.pack(anchor=tk.W)
        self.Static10.place(x=0, y=390)


    def view1(self):
        #labeles
        self.Static1 = tk.Label(text=r"File Name 1")
        self.Static1.place(x=0, y=10)

        #GUIからファイルを選択
        self.EditBox1 = tk.Entry(text="",textvariable= self.filename ,width=70)
        self.EditBox1.place(x=0, y=30)
        self.FileDialogButton1 = tk.Button(text='open')
        self.FileDialogButton1.place(x=0, y=50)

        self.Button_Clear1 = tk.Button(text=u'Clear File Name', width=20)
        self.Button_Clear1.place(x=60, y=50)

    def view2(self):
        #labeles
        self.Static2 = tk.Label(text=r"File Name 2")
        self.Static2.place(x=0, y=110)

        #Entry
        #GUIからファイルを選択
        self.EditBox2 = tk.Entry(text="",textvariable= self.filename2 ,width=70)
        self.EditBox2.place(x=0, y=130)
        self.FileDialogButton2 = tk.Button(text='open')
        self.FileDialogButton2.place(x=0, y=150)

        self.Button_Clear2 = tk.Button(text=u'Clear File Name', width=20)
        self.Button_Clear2.place(x=60, y=150)

    def view3(self):
        #Labeles
        self.Static3 = tk.Label(text=u'Signal Name')
        self.Static3.place(x=0, y=230)

        self.EditBox3 = tk.Entry(width=70)
        self.EditBox3.insert(tk.END, "Input the signal name.")
        self.EditBox3.place(x=0, y=250)

        #Button
        self.Button_Clear3 = tk.Button(text=u'Clear column Name', width=20)
        self.Button_Clear3.place(x=0, y=270)

    def view4(self):
        self.Button_TollMap = tk.Button(text=u'Plot', width=20)
        self.Button_TollMap.place(x=500, y=330)

    def menu(self):

        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_separator()
        self.menubar.add_cascade(label="Tool", menu=self.filemenu)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.master.config(menu=self.menubar)


class Controller():
    def __init__(self,master,model,view):
        self.master = master
        self.model = model
        self.view = view

        self.view.Button_Clear1["command"] = self.DeleteEntryValue1
        self.view.Button_Clear2["command"] = self.DeleteEntryValue2
        self.view.Button_Clear3["command"] = self.DeleteEntryValue3
        self.view.Button_TollMap["command"] = self.UpdateData_Graph

        self.view.FileDialogButton1["command"] = self.openfiledialog1
        self.view.FileDialogButton2["command"] = self.openfiledialog2

        self.view.filemenu.add_command(label="Open", command=self.donothing)
        self.view.filemenu.add_command(label="Save Result", command=self.donothing)
        self.view.filemenu.add_command(label="Save as...", command=self.donothing)
        self.view.filemenu.add_command(label="Close", command=self.donothing)
        self.view.filemenu.add_command(label="Exit", command=self.master.quit)
        self.view.helpmenu.add_command(label="About us", command=self.donothing)
        self.view.helpmenu.add_command(label="manual", command=self.donothing)

    def openfiledialog1(self):
        file = tk.filedialog.askopenfilename()
        self.view.filename.set(file)
    def openfiledialog2(self):
        file = tk.filedialog.askopenfilename()
        self.view.filename2.set(file)

    def donothing(self):
        self.filein = tk.Toplevel(self.master)
        self.button = tk.Button(self.filein, text="Not Supported")
        self.button.pack()

    def DeleteEntryValue1(self):
        self.view.EditBox1.delete(0, tk.END)


    def DeleteEntryValue2(self):
        self.view.EditBox2.delete(0, tk.END)

    def DeleteEntryValue3(self):
        self.view.EditBox3.delete(0, tk.END)

    #Create the Animation on the Graph
    def UpdateData_Graph(self):

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

        #Set files name to read
        Kaikaku_FileName = self.view.EditBox1.get() #Result of PZ1A file name
        Kaikaku_FileName2 = self.view.EditBox2.get()
        SigName = self.view.EditBox3.get()

        #Set parameters
        PickUpSigName = SigName
        TitleName = PickUpSigName
        
        PickUpSigNameForFile = PickUpSigName.replace(".","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace("[","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace("]","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace(":","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace("/","_")
        
        y_1 = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, sep=",", usecols=[PickUpSigName])
        y_2 = pd.read_csv(filepath_or_buffer=Kaikaku_FileName2, sep=",", usecols=[PickUpSigName])
        x = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, usecols=[0])

        #base==16 →　base==10 if data is 'str'
        if type(y_1[PickUpSigName][1]) is str:
            y_1 = hexadecimal_to_decimal(y_1, PickUpSigName)

        if type(y_2[PickUpSigName][1]) is str:
            y_2 = hexadecimal_to_decimal(y_2, PickUpSigName)

        plt.title(TitleName)
        plt.xlabel('time')
        plt.grid(True)
        plt.plot(x, y_1)
        plt.plot(x, y_2)
        plt.savefig(f'png/{PickUpSigNameForFile}.png')
        plt.show()

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.model = Model()

        master.geometry(str(self.model.width)+"x"+str(self.model.height))
        master.title("Plot_Graph Ver 1.0")

        self.view = View(master,self.model)

        self.controller = Controller(master,self.model,self.view)
        

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()