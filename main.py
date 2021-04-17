import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter import font


class Activity_Input(tk.Frame):
    def __init__(self, parent, label, default=""):

        self.new_activity = tk.StringVar()
        self.parent = parent

        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=label)
        self.entry = tk.Entry(self, textvariable=self.new_activity) 
        self.entry.insert(0, default)
        self.enter_button = tk.Button(self, text="Enter", command=self.entered)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.enter_button.grid(row=0, column=2)

    def entered(self):
        self.parent.add_activity(self.new_activity)

class Activity_Listing(tk.Frame):
    def __init__(self, parent, new_activity=''):
        tk.Frame.__init__(self, parent)

        self.checked = tk.BooleanVar()
        self.crossed_off = False
        self.default_font = font.Font(family='Courier', size=10, weight=font.NORMAL, overstrike=0)
        self.striked_font = font.Font(family='Courier', size=10, weight=font.NORMAL, overstrike=1)


        self.check_box = tk.Checkbutton(self, variable=self.checked, onvalue=1, offvalue=0, command=self.check_box_checked)
        self.label = tk.Label(self, text=new_activity, font=self.default_font)
        self.cross_button = tk.Button(self, text="Cross off", command=self.cross_off)
        self.delete_button = tk.Button(self, text="delete", command=self.delete_self)



       # self.check_box.grid(row=0, column=0)
       # self.label.grid(row=0, column=1)
       # self.button.grid(row=0, column=2)
        
        self.check_box.pack(side="left")
        self.label.pack(side="left")
        self.delete_button.pack(side="right")
        self.cross_button.pack(side="right")

    def cross_off(self):
        if self.crossed_off:
            self.label.configure(font=self.default_font)
            self.crossed_off = False
        else:
            self.label.configure(font=self.striked_font)
            self.crossed_off = True
        

    def delete_self(self):
        answer = askyesno(title="Deletion Inquiry", message="Delete this activity?")
        if answer:
            self.destroy()
        else:
            return

    def check_box_checked(self):
        print(self.checked.get())

class Activities_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


class UI_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
     
        self.label = tk.Label(self, text="To-do list")
        self.activity_input = Activity_Input(self, "input", default="Input activity")

        self.activity_list = []

        self.label.pack(side="top")
        self.activity_input.pack(side="top")

    def add_activity(self, new_activity):
        print(new_activity.get())
        activity = Activity_Listing(self, new_activity=new_activity.get())
        self.activity_list.append(activity)
        activity.pack(side="top")
        

    def update_activity_list(self):
        for activity in self.activity_list:
            print('packing')
            activity.pack(side="top")
            print(activity.label)

class To_Do():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("320x500")

        self.new_activity = tk.StringVar()

        self.ui_frame = UI_Frame(self.root)

        self.ui_frame.pack(side="top")


        self.root.mainloop()
        
    def add_activity(self, activity):
        print(activity.get())


if __name__=="__main__":
    app = To_Do()

