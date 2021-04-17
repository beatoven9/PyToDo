import tkinter as tk

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

        self.check_box = tk.Checkbutton(self)
        self.label = tk.Label(self, text=new_activity)
        self.button = tk.Button(self, text="delete", command=self.delete_self)

    def delete_self(self):
        answer = tk.messagebox.askyesno(title="Deletion Inquiry", message="Delete this activity?")
        if answer:
            self.destroy()
        else:
            return

class UI_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
     
        self.label = tk.Label(self, text="To-do list")
        self.activity_input = Activity_Input(self, "input", default="Input activity")

        self.label.pack(side="top")
        self.activity_input.pack(side="top")

    def add_activity(self, new_activity):
        print(new_activity.get())

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

