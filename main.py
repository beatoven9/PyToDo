import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter import font
import json

class Activity_Input(tk.Frame):
    def __init__(self, parent, label, default=""):

        self.new_activity = tk.StringVar()
        self.parent = parent

        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text=label)
        self.entry = tk.Entry(self, textvariable=self.new_activity) 
        self.entry.insert(0, default)
        self.enter_button = tk.Button(self, text="Enter", command=self.entered)

        self.label.pack(side='left')
        self.entry.pack(side='left', expand=True, fill=tk.X)
        self.enter_button.pack(side='left')

    def entered(self):
        self.parent.add_activity(self.new_activity.get())
        

class Activity_Listing(tk.Frame):
    def __init__(self, parent, new_activity=''):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.checked = tk.BooleanVar()
        self.crossed_off = False
        self.default_font = font.Font(family='Courier', size=10, weight=font.NORMAL, overstrike=0)
        self.striked_font = font.Font(family='Courier', size=10, weight=font.NORMAL, overstrike=1)

        self.number = tk.Label(self, text='1')
        self.check_box = tk.Checkbutton(self, variable=self.checked, onvalue=1, offvalue=0, command=self.check_box_checked)
        self.label = tk.Label(self, text=new_activity, font=self.default_font)
        self.cross_button = tk.Button(self, text="Cross off", command=self.toggle_crossed_off)
        self.delete_button = tk.Button(self, text="delete", command=self.delete_self)

        self.check_box.pack(side="left")
        self.number.pack(side='left')
        self.label.pack(side="left", anchor='w', expand=True)
        self.delete_button.pack(side="right")
        self.cross_button.pack(side="right")

    def toggle_crossed_off(self):
        if self.crossed_off:
            self.set_crossed_off(False)
        else:
            self.set_crossed_off(True)

    def set_crossed_off(self, crossed):
        if crossed:    
            self.label.configure(font=self.striked_font)
            self.crossed_off = True
        else:
            self.label.configure(font=self.default_font)
            self.crossed_off = False


    def delete_self(self):
        answer = askyesno(title="Deletion Inquiry", message="Delete this activity?")
        if answer:
            self.parent.destroy_listing(int(self.number.cget('text')) - 1 )
        else:
            return

    def check_box_checked(self):
        print(self.checked.get())

class Activities_Container(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent) 
        self.activity_input = Activity_Input(self, "input", default="Input activity")
        self.activity_list = []
        self.activity_input.pack(side="top", fill=tk.X)

    def add_activity(self, new_activity, crossed_off=False):
        activity = Activity_Listing(self, new_activity=new_activity)
        self.activity_list.append(activity)
        activity.number.config(text=str(len(self.activity_list)))
        activity.set_crossed_off(crossed_off)
        activity.pack(side="top", fill=tk.X)

    def clear_listings(self):
        for _i in range(len(self.activity_list)):
            self.destroy_listing(-1)
 
    def update_activity_list(self):
        for i in range(len(self.activity_list)):
            if self.activity_list[i]: 
                self.activity_list[i].number.config(text=str(i+1))
            else:
                print("This listing doesnt exist")

    def destroy_listing(self, listing_number):
        self.activity_list[listing_number].destroy()
        self.activity_list.pop(listing_number) 
        self.update_activity_list()

    def export_json_dict(self):
        dictionary = {}
        for activity in self.activity_list:
            dictionary[activity.number.cget('text')] = [activity.label.cget('text'), activity.crossed_off]
        with open("test.json", "w") as outfile:
            json.dump(dictionary, outfile)

    def import_json_dict(self):
        json_dict = open('test.json')
        loaded_dict = json.load(json_dict)
        self.load_dict(loaded_dict)

    def load_dict(self, loaded_dict):
        self.clear_listings()
        for i in range(len(loaded_dict.keys())):
            self.add_activity(loaded_dict[str(i+1)][0], loaded_dict[str(i+1)][1])


class UI_Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
     
        self.label = tk.Label(self, text="To-do list")
        self.activities_container = Activities_Container(self)
        self.save_button = tk.Button(text="Save", command=self.save_list)
        self.load_button = tk.Button(text="load", command=self.load_list)
        self.clear_button = tk.Button(text="Clear", command=self.clear_listings)


        self.label.pack(side="top")
        self.activities_container.pack(side="top", fill=tk.X)
        self.save_button.pack(side="bottom")
        self.load_button.pack(side="bottom")
        self.clear_button.pack(side="bottom")


    def save_list(self):
        self.activities_container.export_json_dict()

    def load_list(self):
        self.activities_container.import_json_dict()

    def clear_listings(self):
        self.activities_container.clear_listings()
        


class To_Do():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.new_activity = tk.StringVar()
        self.ui_frame = UI_Frame(self.root)
        self.ui_frame.pack(side="top", fill=tk.X)
        self.root.mainloop()

if __name__=="__main__":
    app = To_Do()

