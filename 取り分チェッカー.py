# coding: utf-8
from pdb import lasti2lineno
import tkinter as tk

version = "v1.0"

class Window(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.menu()

    def menu(self):
        self.start_menu = tk.Frame(self)
        self.start_menu.pack()

        self.startbutton = tk.Button(self.start_menu,text="起動",command=lambda:self.guzai_setting())
        self.startbutton.pack()

        self.endbutton = tk.Button(self.start_menu,text="終了",command=lambda:self.master.destroy())
        self.endbutton.pack()

    def guzai_setting(self):
        self.reset(self.start_menu)
        
        self.setting_frame = tk.Frame(self)
        self.setting_frame.pack(side=tk.LEFT)
    
        label = tk.Label(self.setting_frame,text="具材を入力してください")
        label.pack()

        self.t = tk.StringVar()

        self.entrybox = tk.Entry(self.setting_frame,textvariable=self.t)
        self.entrybox.bind("<Return>",lambda event:self.add_guzai())
        self.entrybox.pack()

        add_button = tk.Button(self.setting_frame,text="具材追加",command=lambda:self.add_guzai())
        add_button.pack()

        decide_button = tk.Button(self.setting_frame,text="具材の確定",command=lambda:self.get_list())
        decide_button.pack()

        self.guzai_list = tk.Listbox(self.setting_frame)
        self.guzai_list.bind("<<ListboxSelect>>",lambda event:self.guzai_list.delete(self.guzai_list.curselection()))
        self.guzai_list.pack()

        self.num_frame = tk.Frame(self)
        self.num_frame.pack(side=tk.LEFT)
        
    def add_guzai(self):
        self.guzai_list.insert(tk.END,self.entrybox.get())
        self.t.set("")

    def get_list(self):
        l = self.guzai_list.get(0,tk.END)
        self.add_label(self.num_frame,l)

    def add_label(self,frame,guzai_list):
        dic = {}
        num_dic = {}
        num = {}
        i = 0

        for guzai in guzai_list:
            dic[i] = tk.Label(frame,text=guzai)
            dic[i].pack()
            
            num[i] = tk.StringVar()
            num_dic[i] = tk.Spinbox(frame,state="readonly",textvariable=num[i],values=[x+1 for x in range(9)])
            num_dic[i].pack()

            i += 1

    def reset(self,frame):
        widgets = frame.winfo_children()
        for widget in widgets:
            widget.destroy()

class App:
    def run(self):
        root = tk.Tk()
        root.title("取り分チェッカー {}".format(version))
        root.geometry("1000x800+300+100")
        Window(root)
        root.mainloop()
        

if __name__ == "__main__":
    app = App()
    app.run()