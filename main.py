import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
import os
import shutil
import datetime


class multifilesApp(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)   
        self.selected_files = []
        self.file_type_dict = {}
        self.file_size_dict = {}
        self.file_age_dict = {}
        self.dropdown_var = tk.StringVar()

    #Lietotāja interfeiss
    def initializeUI(self):
        self.master.title("Failu organizātors")

        #Failu izvēlēšanās poga
        self.button1 = tk.Button(text = "Izvēlieties failus", command = self.selectFiles, width = 15)
        self.button1.place(x = 15, y = 10)

        #Izveido tekstu virs izvēlnes
        self.text_dropdown = tk.Label(text = "Izvēlieties orgnizēšanas parametru")
        self.text_dropdown.place(x = 145, y = 5)

        #Izveido izvēlni, lai izvēlētos parametru, pēc kura organizēs failus
        self.dropdown_var = tk.StringVar()
        self.dropdown = ttk.Combobox(textvariable = self.dropdown_var, state = "readonly",
                                values = ("Failu tips", "Failu vecums"))
        self.dropdown.place(x = 165, y = 30)

        #Izveido pogu, kas sāk failu organizāciju
        self.button2 = tk.Button(text = "Organizēt failus", command = self.OrganizeByFileType, width = 15)
        self.button2.place(x = 275, y = 265)

    #Atver izvēlētāju, lai ievadītu failus
    def selectFiles(self):
     
        #Izvēlas failus
        file_paths = filedialog.askopenfilenames(title = "Izvēlieties failus", filetypes = (("Visi faili", "*.*"),))
        self.selected_files.extend(file_paths)

        #Pārbauda, vai ir izvēlēti faili
        if not file_paths:
            raise FileNotFoundError("Nav izvēlēts neviens fails.")
        
        #Pievieno faila tipus vārdnīcai
        for file in file_paths:
            file_type = file.split('.')[-1]
            if file_type not in self.file_type_dict:
                self.file_type_dict[file_type] = []
            self.file_type_dict[file_type].append(file)

    #Organizē izvēlētos failus pēc to paplašinājumiem
    def OrganizeByFileType(self):
        for file_type in self.file_type_dict:
            newpath_type = os.path.join(r"C:\Users\user\Desktop", file_type)

            os.makedirs(newpath_type, exist_ok = True)           #izveido mapi
            print("Home directory %s was created." %newpath_type)
            print("Directory {0} was created.".format(newpath_type))

            #Pievieno izvēlētos failus
            for file in self.file_type_dict[file_type]:
                shutil.move(file, newpath_type)        #pārvieto failus
            self.file_type_dict[file_type].clear()

    #Nestrādā
    def OrganizeByFileAge(self):
        now = datetime.datetime.now()
        for file_age in self.file_age_dict:
            newpath_age = os.path.join(r"C:\Users\user\Desktop", str(now.year) + "-" + str(file_age))
            os.makedirs(newpath_age, exist_ok=True)

            for file in self.file_age_dict[file_age]:
                file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file))
                folder_name = str(file_mtime.year) + "-" + str(file_mtime.month)
                newpath_age_folder = os.path.join(newpath_age, folder_name)
                os.makedirs(newpath_age_folder, exist_ok=True)
                shutil.move(file, newpath_age_folder)
            self.file_age_dict[file_age].clear()
        
    #Izvēlas failu orgnizēšanas parametru
    def on_dropdown_select(self):
        selected_value = self.dropdown_var.get()
        if selected_value == "Failu tips" and self.selected_files:
            self.OrganizeByFileType()
        elif selected_value == "Failu vecums" and self.selected_files:
            self.OrganizeByFileAge()
        else:
            self.button2.config(state = DISABLED)

#Atver lietotāja interfeisu
def interfeiss():
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("400x300")

    #Atļauj programmai lasīt kodu
    app = multifilesApp(master = root)
    app.initializeUI()
    app.mainloop()

#Tur programmu vaļā līdz to aizver lietotājs
interfeiss()