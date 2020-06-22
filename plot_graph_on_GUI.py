import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import os

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

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
        self.view2()
        self.view3()
        self.menu()

        self.Static10 = tk.Label(text=u'Copyright (c) 2020 Nissan Motor Co.,Ltd. All rights reserved')
        self.Static10.pack(anchor=tk.W)
        self.Static10.place(x=0, y=390)

        self.Static_png = tk.Label(text=u'Graph → png/(filename)_csv_(signalname).png')
        self.Static_png.pack(anchor=tk.W)
        self.Static_png.place(x=0, y=330)


    def view1(self):
        #labeles
        self.Static1 = tk.Label(text=r"File Name (ex. 1.csv,2.csv)")
        self.Static1.place(x=0, y=10)

        #GUIからファイルを選択
        self.EditBox1 = tk.Entry(text="",textvariable= self.filename ,width=70)
        self.EditBox1.place(x=0, y=30)

        self.Button_Clear1 = tk.Button(text=u'Clear File Name', width=20)
        self.Button_Clear1.place(x=0, y=50)

    def view2(self):
        #Labeles
        self.Static2 = tk.Label(text=u'Signal Name (ex. signal.txt or sig1,sig2)')
        self.Static2.place(x=0, y=230)

        self.EditBox2 = tk.Entry(text="", textvariable= self.filename2, width=70)
        self.EditBox2.place(x=0, y=250)

        #Button
        self.Button_Clear2 = tk.Button(text=u'Clear column Name', width=20)
        self.Button_Clear2.place(x=0, y=270)

    def view3(self):
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
        self.view.Button_TollMap["command"] = self.list_to_graph_conveter

        self.view.filemenu.add_command(label="Open", command=self.donothing)
        self.view.filemenu.add_command(label="Save Result", command=self.donothing)
        self.view.filemenu.add_command(label="Save as...", command=self.donothing)
        self.view.filemenu.add_command(label="Close", command=self.donothing)
        self.view.filemenu.add_command(label="Exit", command=self.master.quit)
        self.view.helpmenu.add_command(label="About us", command=self.donothing)
        self.view.helpmenu.add_command(label="manual", command=self.donothing)

    

    def donothing(self):
        self.filein = tk.Toplevel(self.master)
        self.button = tk.Button(self.filein, text="Not Supported")
        self.button.pack()

    def DeleteEntryValue1(self):
        self.view.EditBox1.delete(0, tk.END)

    def DeleteEntryValue2(self):
        self.view.EditBox2.delete(0, tk.END)
    
    def list_to_graph_conveter(self):
        #Set files name to read
        FileName_list = self.view.EditBox1.get()
        SigName_list = self.view.EditBox2.get() # *.txtも可

        FileName_list = FileName_list.split(',')

        if str(os.path.splitext(SigName_list)[1]) == '.txt':
            f = open(SigName_list)
            data = f.read()
            SigName_list = data.split('\n')
        else:#直接入力を想定
            SigName_list = SigName_list.split(',')
        

        for i,sig_ in enumerate(SigName_list):
            plot_win = tk.Toplevel(self.master)
            plot_win.geometry("300x300")
            fig = plt.figure()
            ax = fig.add_subplot(111)

            for file_ in FileName_list: 
                self.UpdateData_Graph(file_, sig_, ax)

            plt.savefig(f'png/test_{sig_}.png')

            
            #tkinterのウインド上部にグラフを表示する
            canvas = FigureCanvasTkAgg(fig, master=plot_win)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
            #tkinterのウインド下部にツールを追加する
            toolbar = NavigationToolbar2Tk(canvas, plot_win)
            toolbar.update()

    #Create the Animation on the Graph
    def UpdateData_Graph(self, FileName, SigName, ax):

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

        y = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, sep=",", usecols=[PickUpSigName])
        x = pd.read_csv(filepath_or_buffer=Kaikaku_FileName, usecols=[0])

        #base==16 →　base==10 if data is 'str'
        if type(y[PickUpSigName][1]) is str:
            y = hexadecimal_to_decimal(y, PickUpSigName)

        ax.set_title(TitleName)
        ax.set_xlabel('time')
        ax.grid(True)
        ax.plot(x, y)


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.model = Model()

        master.geometry(str(self.model.width)+"x"+str(self.model.height))
        master.title("Plot_Graph Ver 1.1")

        self.view = View(master,self.model)

        self.controller = Controller(master,self.model,self.view)
        

def main():
    win = tk.Tk()
    app = Application(master=win)
    app.mainloop()

if __name__ == "__main__":
    main()