import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
import os
import shutil



class multifilesApp(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)   
        self.selected_files = []
        self.file_type_dict = {}
        self.dropdown_var = "Failu tips"
        self.script_dir = os.path.dirname(os.path.realpath(__file__))

    #Lietotāja interfeiss
    def initializeUI(self):
        self.master.title("Failu organizātors")

        #Failu izvēlēšanās poga
        self.button1 = tk.Button(text = "Izvēlieties failus", command = self.selectFiles, width = 15,
                                 background = "light gray", fg = "black")
        self.button1.place(x = 15, y = 10)

        #Izveido tekstu
        self.text_dropdown = tk.Label(text = "Faili tiks organizēti pēc failu tipa.",
                                      background = "light gray", fg = "black")
        self.text_dropdown.place(x = 145, y = 12)

        #Izveido tekstu
        self.text_placeholder = tk.Label(text = "Mapītes ar izvēlētajiem failiem atradīsies tur pat, kur šī programma.",
                                      background = "light gray", fg = "black")
        self.text_placeholder.place(x = 15, y = 40)

        #Izveido pogu, kas sāk failu organizāciju
        self.button2 = tk.Button(text = "Organizēt failus", command = self.OrganizeByFileType, width = 15,
                                 background = "light gray", fg = "black")
        self.button2.place(x = 275, y = 265)

    #Atver izvēlētāju, lai ievadītu failus
    def selectFiles(self):
     
        #Izvēlas failus
        file_paths = filedialog.askopenfilenames(title = "Izvēlieties failus", filetypes = (("Visi faili", "*.*"),))
        self.selected_files.extend(file_paths)
        
        #Pievieno faila tipus vārdnīcai
        for file in file_paths:
            file_type = file.split('.')[-1]
            if file_type not in self.file_type_dict:
                self.file_type_dict[file_type] = []
            self.file_type_dict[file_type].append(file)

    #Organizē izvēlētos failus pēc to paplašinājumiem
    def OrganizeByFileType(self):
        for file_type in self.file_type_dict:
            newpath_type = os.path.join(self.script_dir, file_type)

            os.makedirs(newpath_type, exist_ok = True)           #izveido mapi
            print("Home directory %s was created." %newpath_type)
            print("Directory {0} was created.".format(newpath_type))

            #Pievieno izvēlētos failus
            for file in self.file_type_dict[file_type]:
                shutil.move(file, newpath_type)        #pārvieto failus
            self.file_type_dict[file_type].clear()
        
    #Izvēlas failu orgnizēšanas parametru
    def on_dropdown_select(self):
        selected_value = self.dropdown_var.get()
        if selected_value == "Failu tips" and self.selected_files:
            self.OrganizeByFileType()
        else:
            self.button2.config(state = DISABLED)

#Atver lietotāja interfeisu
def interfeiss():
    root = tk.Tk()
    root.configure(background = "gray")
    root.resizable(False, False)
    root.geometry("400x300")

    #Atļauj programmai lasīt kodu
    app = multifilesApp(master = root)
    app.initializeUI()
    app.mainloop()

#Tur programmu vaļā līdz to aizver lietotājs
interfeiss()
