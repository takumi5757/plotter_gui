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

        self.view1()
        self.view2()
        self.view3()
        self.view4()

        self.Static10 = tk.Label(text=u'Copyright (c) 2020 Nissan Motor Co.,Ltd. All rights reserved')
        self.Static10.pack(anchor=tk.W)
        self.Static10.place(x=0, y=390)


    def view1(self):
        #labeles
        self.Static1 = tk.Label(text=r"File Name")
        self.Static1.pack(anchor=tk.W)

        #Entry
        self.EditBox1 = tk.Entry(width=70)
        self.EditBox1.insert(tk.END,  "Input the file name.")
        self.EditBox1.pack(anchor=tk.W)

        #Button
        self.Button_InputVal1 = tk.Button(text=u'Input File Name', width=20)
        self.Button_InputVal1.pack(anchor=tk.W)

        self.Button_Clear1 = tk.Button(text=u'Clear File Name', width=20)
        self.Button_Clear1.pack(anchor=tk.W)

    def view2(self):
        #labeles
        self.Static2 = tk.Label(text=r"File Name")
        self.Static2.pack(anchor=tk.W)

        #Entry
        self.EditBox2 = tk.Entry(width=70)
        self.EditBox2.insert(tk.END,  "Input the file name.")
        self.EditBox2.pack(anchor=tk.W)

        #Button
        self.Button_InputVal2 = tk.Button(text=u'Input File Name', width=20)
        self.Button_InputVal2.pack(anchor=tk.W)

        self.Button_Clear2 = tk.Button(text=u'Clear File Name', width=20)
        self.Button_Clear2.pack(anchor=tk.W)

    def view3(self):
        #Labeles
        self.Static3 = tk.Label(text=u'Signal Name')
        self.Static3.pack(anchor=tk.W)

        self.EditBox3 = tk.Entry(width=70)
        self.EditBox3.insert(tk.END, "Input the signal name.")
        self.EditBox3.pack(anchor=tk.W)

        #Button
        self.Button_InputVal3 = tk.Button(text=u'Input File Name', width=20)
        self.Button_InputVal3.pack(anchor=tk.W)

        self.Button_Clear3 = tk.Button(text=u'Clear File Name', width=20)
        self.Button_Clear3.pack(anchor=tk.W)

    def view4(self):
        #Labeles
        self.Static_Tollgate = tk.Label(text=u'Plot Graph')
        self.Static_Tollgate.place(x=500, y=305)

        self.Button_TollMap = tk.Button(text=u'Execute', width=20)
        self.Button_TollMap.place(x=500, y=330)


class Controller():
    def __init__(self,master,model,view):
        self.master = master
        self.model = model
        self.view = view

        self.view.Button_InputVal1["command"] = self.GetEditBoxValue1
        self.view.Button_Clear1["command"] = self.DeleteEntryValue1
        self.view.Button_InputVal2["command"] = self.GetEditBoxValue2
        self.view.Button_Clear2["command"] = self.DeleteEntryValue2
        self.view.Button_InputVal3["command"] = self.GetEditBoxValue3
        self.view.Button_Clear3["command"] = self.DeleteEntryValue3
        self.view.Button_TollMap["command"] = self.UpdateData_Graph

    def GetEditBoxValue1(self):
        value = self.view.EditBox1.get()
        print(value)

    def DeleteEntryValue1(self):
        self.view.EditBox1.delete(0, tk.END)

    def GetEditBoxValue2(self):
        value = self.view.EditBox2.get()
        print(value)

    def DeleteEntryValue2(self):
        self.view.EditBox2.delete(0, tk.END)

    def GetEditBoxValue3(self):
        value = self.view.EditBox3.get()
        print(value)

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