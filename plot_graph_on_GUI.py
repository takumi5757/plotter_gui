import tkinter as tk
#import random as rd
#import time
import pandas as pd
import matplotlib.pyplot as plt
import os

class Model():
    def __init__(self):
        self.width=700
        self.height=420


class View():
    def __init__(self,master,model):
        self.master = master
        self.model = model

        self.filename = tk.StringVar(value="Input the File Name or Path.")
        self.filename2 = tk.StringVar(value="Input the Signal Name or Text Path.")

        self.view1()
        #self.view2()
        self.view3()
        self.view4()
        self.menu()

        self.Static10 = tk.Label(text=u'Copyright (c) 2020 Nissan Motor Co.,Ltd. All rights reserved')
        self.Static10.pack(anchor=tk.W)
        self.Static10.place(x=0, y=390)


    def view1(self):
        #labeles
        self.Static1 = tk.Label(text=r"File Name")
        self.Static1.place(x=0, y=10)

        #GUIからファイルを選択
        self.EditBox1 = tk.Entry(text="",textvariable= self.filename ,width=70)
        self.EditBox1.place(x=0, y=30)
        self.FileDialogButton1 = tk.Button(text='open')
        self.FileDialogButton1.place(x=0, y=50)

        self.Button_Clear1 = tk.Button(text=u'Clear File Name', width=20)
        self.Button_Clear1.place(x=60, y=50)

    def view3(self):
        #Labeles
        self.Static3 = tk.Label(text=u'Signal Name')
        self.Static3.place(x=0, y=230)

        self.EditBox3 = tk.Entry(text="", textvariable= self.filename2, width=70)
        self.EditBox3.place(x=0, y=250)

        self.FileDialogButton3 = tk.Button(text='open')
        self.FileDialogButton3.place(x=0, y=270)

        #Button
        self.Button_Clear3 = tk.Button(text=u'Clear column Name', width=20)
        self.Button_Clear3.place(x=60, y=270)

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
        self.view.Button_Clear3["command"] = self.DeleteEntryValue3
        self.view.Button_TollMap["command"] = self.list_to_graph_conveter

        self.view.FileDialogButton1["command"] = self.openfiledialog1
        self.view.FileDialogButton3["command"] = self.openfiledialog2

        self.view.filemenu.add_command(label="Open", command=self.donothing)
        self.view.filemenu.add_command(label="Save Result", command=self.donothing)
        self.view.filemenu.add_command(label="Save as...", command=self.donothing)
        self.view.filemenu.add_command(label="Close", command=self.donothing)
        self.view.filemenu.add_command(label="Exit", command=self.master.quit)
        self.view.helpmenu.add_command(label="About us", command=self.donothing)
        self.view.helpmenu.add_command(label="manual", command=self.donothing)

    def openfiledialog1(self):
        fTyp = [("","*.csv")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file_list = tk.filedialog.askopenfilenames(filetypes = fTyp,initialdir = iDir)
        self.file_list = list(file_list)
        self.view.filename.set(file_list)

    def openfiledialog2(self):
        fTyp = [("","*.txt")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file_ = tk.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        self.view.filename2.set(file_)

    def donothing(self):
        self.filein = tk.Toplevel(self.master)
        self.button = tk.Button(self.filein, text="Not Supported")
        self.button.pack()

    def DeleteEntryValue1(self):
        self.view.EditBox1.delete(0, tk.END)

    def DeleteEntryValue3(self):
        self.view.EditBox3.delete(0, tk.END)

    def list_to_graph_conveter(self):
        #Set files name to read
        FileName_list = self.file_list #Result of PZ1A file name
        SigName_list = self.view.EditBox3.get() # list.txt

        if str(os.path.splitext(SigName_list)[1]) == '.txt':
            f = open(SigName_list)
            data = f.read()
            SigName_list = data.split('\n')

        
        #plot_num = len(SigName_list)
        #fig,axes = plt.subplots(nrows=1,ncols=plot_num,figsize=(10,8))
        for sig_ in SigName_list:
            for file_ in FileName_list:
                self.UpdateData_Graph(file_, sig_)


    #Create the Animation on the Graph
    def UpdateData_Graph(self, FileName, SigName):
        print("filesig")
        print(FileName,SigName)

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
        Kaikaku_FileName = FileName

        #Set parameters
        PickUpSigName = SigName
        TitleName = PickUpSigName
        
        PickUpSigNameForFile = PickUpSigName.replace(".","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace("[","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace("]","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace(":","_")
        PickUpSigNameForFile = PickUpSigNameForFile.replace("/","_")

        CSVName = os.path.split(FileName)[1].replace(".","_")

        print(f"kaikaku_filename=={Kaikaku_FileName}")
        y_1 = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, sep=",", usecols=[PickUpSigName])
        x = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, usecols=[0])

        #base==16 →　base==10 if data is 'str'
        if type(y_1[PickUpSigName][1]) is str:
            y_1 = hexadecimal_to_decimal(y_1, PickUpSigName)

        plt.title(TitleName)
        plt.xlabel('time')
        plt.grid(True)
        plt.plot(x, y_1)
        plt.savefig(f'png/{CSVName}_{PickUpSigNameForFile}.png')
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