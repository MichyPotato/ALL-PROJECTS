# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
'''
Group 4 (Arshan, Ben, Chris, Ryan, Mathew)
CS50 AP
Passenger Lists Table GUI
'''
import tkinter as tk
from tkinter import *
from global_database import GlobalDb
from global_database import GlobalDb
from tkinter import ttk 
from PIL import ImageTk, Image
from tkinter import ttk

class PassengersListsGUI:

    def donothing(self):
        pass
    def __init__(self):


        self.plist_pos = 0
        self.db = GlobalDb()
        self.connected = False

        self.passengerlistsWindow = tk.Tk()
        self.passengerlistsWindow.title("Passenger Lists")
        self.frame = tk.Frame(self.passengerlistsWindow)
        self.passengerlistsWindow.geometry("800x475")
        self.passengerlistsFrame = tk.Frame(self.passengerlistsWindow, width = 800, height = 475)


        #MENU FOR THE SECOND TABLE: PASSENGER LISTS
        self.passengerlistsMenu = Menu(self.passengerlistsWindow)
            #FILE TAB ON MENU
        self.passengerlistsFile = Menu(self.passengerlistsMenu, tearoff = 0)
        self.passengerlistsMenu.add_cascade(label = "File", menu = self.passengerlistsFile)
        self.passengerlistsFile.add_command(label = "Connect", command = self.connect)
        self.passengerlistsFile.add_command(label = "Disconnect", command = self.disconnect)
        self.passengerlistsFile.add_command(label = "Exit", command = self.donothing())
        

        self.passengerlistsFile.add_separator()
            #EDIT TAB ON MENU
        self.passengerlistsEdit = Menu(self.passengerlistsMenu, tearoff = 0)
        self.passengerlistsMenu.add_cascade(label = "Edit", menu = self.passengerlistsEdit)
        self.passengerlistsEdit.add_command(label = "Add", command = lambda: self.db.insertPassengersLists(self.getPlistInfo()))
        self.passengerlistsEdit.add_command(label = "Update", command = lambda: self.db.updatePassengersLists(self.getPlistInfo()))
        self.passengerlistsEdit.add_command(label = "Delete", command = lambda: self.db.deletePassengersLists())
        

        self.passengerlistsEdit.add_separator()
            #NAVIGATE TAB FOR MENU
        self.passengerlistsNav = Menu(self.passengerlistsMenu, tearoff = 0)
        self.passengerlistsMenu.add_cascade(label = "Navigate", menu = self.passengerlistsNav)
        self.passengerlistsNav.add_command(label = "First", command =  lambda: self.plist_jumpRec(0 - self.plist_len))
        self.passengerlistsNav.add_command(label = "3rd Previous", command =  lambda: self.plist_jumpRec(-3))
        self.passengerlistsNav.add_command(label = "Previous", command = lambda: self.plist_jumpRec(-1))
        self.passengerlistsNav.add_command(label = "Next", command =  lambda: self.plist_jumpRec(1) )
        self.passengerlistsNav.add_command(label = "3rd Next", command = lambda: self.plist_jumpRec(3))
        self.passengerlistsNav.add_command(label = "Last", command = lambda: self.plist_jumpRec(self.plist_len))
            

        self.passengerlistsNav.add_separator()
            #HELP TAB FOR MENU
        self.passengerlistsHelp = Menu(self.passengerlistsMenu, tearoff = 0)
        self.passengerlistsMenu.add_cascade(label = "Help", menu = self.passengerlistsHelp)
        self.passengerlistsHelp.add_command(label = "About", command = self.donothing())

        self.passengerlistsWindow.config(menu = self.passengerlistsMenu)
        




        #BUTTONS FOR SECOND TABLE: PASSENGER LISTS
        self.btnconnect = tk.Button(self.passengerlistsFrame, text = "Connect", command = self.connect)

        #self.btndisconnect = tk.Button(self.passengerlistsFrame, text = "Disconnect", command = self.disconnect)    

        self.btnStartPL = tk.Button(self.passengerlistsFrame, text = "|<", command = lambda: self.plist_jumpRec(0 - self.plist_len))
        
        self.btnLastPL = tk.Button(self.passengerlistsFrame, text = ">|", command = lambda: self.plist_jumpRec(self.plist_len))         
        
        self.btnplusonePL = tk.Button (self.passengerlistsFrame, text = ">", command = lambda: self.plist_jumpRec(1))
        
        self.btnminusonePL = tk.Button(self.passengerlistsFrame, text = "<", command = lambda: self.plist_jumpRec(-1))

        self.btnplusfivePL = tk.Button (self.passengerlistsFrame, text = ">>", command = lambda: self.plist_jumpRec(3))
        
        self.btnminusfivePL = tk.Button(self.passengerlistsFrame, text = "<<", command = lambda: self.plist_jumpRec(-3)) 

        self.btnInsertPL = tk.Button(self.passengerlistsFrame, text = "Add", command = lambda: self.db.insertPassengersLists(self.getPlistInfo())) 

        self.btnDeletePL = tk.Button(self.passengerlistsFrame, text = "Delete", command = lambda: self.db.deletePassengersLists())

        self.btnUpdatePL = tk.Button(self.passengerlistsFrame, text = "Update", command = lambda: self.db.updatePassengersLists(self.getPlistInfo()))  

        self.btnSavePL = tk.Button(self.passengerlistsFrame, text = "Save", command = self.db.saveChanges) 

        #PLACING BUTTONS FOR SECOND TABLE: PASSENGER LISTS 
        self.btnStartPL.place(x = 350, y = 430)
        self.btnLastPL.place(x = 600, y = 430)
        self.btnplusonePL.place(x = 500, y = 430)
        self.btnminusonePL.place(x = 450, y = 430)
        self.btnplusfivePL.place(x = 550 , y = 430)
        self.btnminusfivePL.place(x = 400, y = 430)
        self.btnconnect.place(x = 150, y = 430)
        #self.btndisconnect.place(x = 200, y =100)
        self.btnInsertPL.place(x = 600, y = 250)
        self.btnDeletePL.place(x = 600, y = 350)
        self.btnUpdatePL.place(x = 600, y = 300)
        self.btnSavePL.place(x=600, y=200)

        #LABELS FOR SECOND TABLE: PASSENGER LISTS
        self.lblpass1Id = tk.Label(self.passengerlistsFrame, text = "Passenger ID:")

        self.lblpass1Present = tk.Label(self.passengerlistsFrame, text = "Present:")
        
        self.lblpass2Id = tk.Label(self.passengerlistsFrame, text = "Passenger ID: ")

        self.lblpass2Present = tk.Label(self.passengerlistsFrame, text = "Present:")

        self.lblpass3Id = tk.Label(self.passengerlistsFrame, text = "Passenger ID: ")
        
        self.lblpass3Present = tk.Label(self.passengerlistsFrame, text = "Present:")

        self.lblpass4Id = tk.Label(self.passengerlistsFrame, text = "Passenger ID:")

        self.lblpass4Present = tk.Label(self.passengerlistsFrame, text = "Present:")

        self.lblpass5Id = tk.Label(self.passengerlistsFrame, text = "Passenger ID:")

        self.lblpass5Present = tk.Label(self.passengerlistsFrame, text = "Present:")

        #PLACING LABELS FOR SECOND TABLE: PASSENGER LISTS
        self.lblpass1Id.place(x = 100, y = 175)
        self.lblpass1Present.place(x = 350, y = 175)

        self.lblpass2Id.place(x = 100, y = 225)
        self.lblpass2Present.place(x = 350, y = 225)

        self.lblpass3Id.place(x = 100, y = 275)
        self.lblpass3Present.place(x = 350, y = 275)

        self.lblpass4Id.place(x = 100, y = 325)
        self.lblpass4Present.place(x = 350, y = 325)

        self.lblpass5Id.place(x = 100, y = 375)
        self.lblpass5Present.place(x = 350, y = 375)

        #ENTRIES FOR SECOND TABLE: PASSENGER LISTS
        self.entrypass1Id = tk.Entry(self.passengerlistsFrame, bd = 1)
        self.entrypass1Present = ttk.Combobox(self.passengerlistsFrame, state = 'readonly', background = 'white', values = ["PRESENT","ABSENT"])

        self.entrypass2Id = tk.Entry(self.passengerlistsFrame, bd = 1)
        self.entrypass2Present = ttk.Combobox(self.passengerlistsFrame, state = 'readonly', background = 'white', values = ["PRESENT","ABSENT"])

        self.entrypass3Id = tk.Entry(self.passengerlistsFrame, bd = 1)
        self.entrypass3Present = ttk.Combobox(self.passengerlistsFrame, state = 'readonly', background = 'white', values = ["PRESENT","ABSENT"])

        self.entrypass4Id = tk.Entry(self.passengerlistsFrame, bd = 1)
        self.entrypass4Present = ttk.Combobox(self.passengerlistsFrame, state = 'readonly', background = 'white', values = ["PRESENT","ABSENT"])

        self.entrypass5Id = tk.Entry(self.passengerlistsFrame, bd = 1)
        self.entrypass5Present = ttk.Combobox(self.passengerlistsFrame, state = 'readonly', background = 'white', values = ["PRESENT","ABSENT"])
        
        #PLACING ENTRIES FOR SECOND TABLE: PASSENGER LISTS
        self.entrypass1Present.place(x = 420, y = 175)
        self.entrypass1Id.place(x = 220, y = 175)

        self.entrypass2Present.place(x = 420, y = 225)
        self.entrypass2Id.place(x = 220, y = 225)

        self.entrypass3Present.place(x = 420, y = 275)
        self.entrypass3Id.place(x = 220, y = 275)

        self.entrypass4Present.place(x = 420, y = 325)
        self.entrypass4Id.place(x = 220, y = 325)

        self.entrypass5Present.place(x = 420, y = 375)
        self.entrypass5Id.place(x = 220, y = 375)
        

        self.passengerlistsFrame.grid(row = 1, column = 0)
        
        self.plist_refresh()
        self.passengerlistsWindow.mainloop()



    def connect(self):
        self.db.createConnection()
        self.connected = True
        self.plist_refresh()
    
    def disconnect(self):
        self.db.breakConnection()
        self.connected = False
        self.plist_clearEntries()

    def plist_jumpRec(self, jump):
        # Ryan Kennedy
        try:
            self.plist_pos += jump
            if (self.plist_pos > self.plist_len-1):
                self.plist_pos = self.plist_len-1

            if (self.plist_pos < 0):
                self.plist_pos = 0
            self.plist_refresh()
        except:
            return "Error jumping record (PassengersLists Table)"
    
    def plist_refresh(self):
        # Ryan Kennedy
        try:
            self.plist_clearEntries()
            self.db.loadPassengersLists()
            self.db.setPassengersListsRecord(self.plist_pos)
            record = self.db.plist_record
            self.entrypass1Id.insert(0, record[1])
            self.entrypass1Present.set(record[2])
            self.entrypass2Id.insert(0, record[3])
            self.entrypass2Present.set(record[4])
            self.entrypass3Id.insert(0, record[5])
            self.entrypass3Present.set(record[6])
            self.entrypass4Id.insert(0,record[7])
            self.entrypass4Present.set(record[8])
            self.entrypass5Id.insert(0, record[9])
            self.entrypass5Present.set(record[10])
            self.plist_len = len(self.db.plist_records)
        except:
            return "Error refreshing GUI (PassengersLists Table)"

    def plist_clearEntries(self):
        # Ryan Kennedy
        self.entrypass1Id.delete(0, END)
        self.entrypass1Present.set("")
        self.entrypass2Id.delete(0, END)
        self.entrypass2Present.set("")
        self.entrypass3Id.delete(0, END)
        self.entrypass3Present.set("")
        self.entrypass4Id.delete(0, END)
        self.entrypass4Present.set("")
        self.entrypass5Id.delete(0, END)
        self.entrypass5Present.set("")

    def getPlistInfo(self):
        # Chris Cruz
        plist_result = [self.entrypass1Id.get(), self.entrypass1Present.get(),self.entrypass2Id.get(), self.entrypass2Present.get(), self.entrypass3Id.get(), self.entrypass3Present.get(), self.entrypass4Id.get(), self.entrypass4Present.get(), self.entrypass5Id.get(), self.entrypass5Present.get()]
        return plist_result
