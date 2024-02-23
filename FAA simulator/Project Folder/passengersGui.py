# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
'''
Group 4 (Arshan, Ben, Chris, Ryan, Mathew)
CS50 AP
Passengers Table GUI
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from global_database import GlobalDb


class PassengersGUI:
    
    def quitProgram(self):
        self.passengersWindow.destroy()

    def showAbout(self):
        tk.messagebox.showinfo(title = "About", message = "GUI for Passengers.")

    def __init__(self):

        self.p_pos = 0
        self.db = GlobalDb()

        self.passengersWindow = tk.Tk()
        self.passengersWindow.title("Passengers")
        self.frame = tk.Frame(self.passengersWindow)
        self.passengersWindow.geometry("800x475")
        self.passengerFrame = tk.Frame(self.passengersWindow, width = 800, height = 475)

        #MENU FOR THE FIRST TABLE: PASSENGERS
        self.passengerMenu = Menu(self.passengersWindow)
            #FILE TAB ON MENU
        self.passengerFile = Menu(self.passengerMenu, tearoff = 0)
        self.passengerMenu.add_cascade(label = "File", menu = self.passengerFile)
        self.passengerFile.add_command(label = "Connect", command = self.connect)
        self.passengerFile.add_command(label = "Disconnect", command = self.disconnect)
        self.passengerFile.add_command(label = "Exit", command = self.quitProgram)
        

        self.passengerFile.add_separator()
            #EDIT TAB ON MENU
        self.passengerEdit = Menu(self.passengerMenu, tearoff = 0)
        self.passengerMenu.add_cascade(label = "Edit", menu = self.passengerEdit)
        self.passengerEdit.add_command(label = "Add", command = lambda: self.db.insertPassengers(self.getPInfo()))
        self.passengerEdit.add_command(label = "Update", command = lambda: self.db.updatePassengers(self.getPInfo()))
        self.passengerEdit.add_command(label = "Delete", command = lambda: self.db.deletePassengers())
        

        self.passengerEdit.add_separator()
            #NAVIGATE TAB FOR MENU
        self.passengerNav = Menu(self.passengerMenu, tearoff = 0)
        self.passengerMenu.add_cascade(label = "Navigate", menu = self.passengerNav)
        self.passengerNav.add_command(label = "First", command =  lambda: self.p_jumpRec(0 - self.p_len))
        self.passengerNav.add_command(label = "3rd Previous", command =  lambda: self.p_jumpRec(-3))
        self.passengerNav.add_command(label = "Previous", command = lambda: self.p_jumpRec(-1))
        self.passengerNav.add_command(label = "Next", command =  lambda: self.p_jumpRec(1) )
        self.passengerNav.add_command(label = "3rd Next", command = lambda: self.p_jumpRec(3))
        self.passengerNav.add_command(label = "Last", command = lambda: self.p_jumpRec(self.p_len))
            

        self.passengerNav.add_separator()
            #HELP TAB FOR MENU
        self.passengerHelp = Menu(self.passengerMenu, tearoff = 0)
        self.passengerMenu.add_cascade(label = "Help", menu = self.passengerHelp)
        self.passengerHelp.add_command(label = "About", command = self.showAbout)

        self.passengersWindow.config(menu = self.passengerMenu)

        #Creating Foward & Backward
        
        #BUTTONS FOR FIRST TABLE: PASSENGERS
        #Arshan Rahman
        self.btnStartP = tk.Button(self.passengerFrame, text = "|<", command = lambda: self.p_jumpRec(0 - self.p_len))
        
        self.btnLastP = tk.Button(self.passengerFrame, text = ">|", command = lambda: self.p_jumpRec(self.p_len))         
        
        self.btnplusoneP = tk.Button(self.passengerFrame, text = ">", command = lambda: self.p_jumpRec(1))
        
        self.btnminusoneP = tk.Button(self.passengerFrame, text = "<", command =  lambda: self.p_jumpRec(-1))

        self.btnplusfiveP = tk.Button (self.passengerFrame, text = ">>", command = lambda: self.p_jumpRec(3))
        
        self.btnminusfiveP = tk.Button(self.passengerFrame, text = "<<", command = lambda: self.p_jumpRec(-3))

        self.btnInsertP = tk.Button(self.passengerFrame, text = "Add", command = lambda: self.db.insertPassengers(self.getPInfo()))

        self.btnDeleteP = tk.Button(self.passengerFrame, text = "Delete", command = lambda: self.db.deletePassengers())

        self.btnUpdateP = tk.Button(self.passengerFrame, text = "Update", command = lambda: self.db.updatePassengers(self.getPInfo()))

        self.btnconnect = tk.Button(self.passengerFrame, text = "Connect", command = self.connect)

        #self.btnSave = tk.Button(self.passengerFrame, text = "Save", command = self.db.saveChanges)

        #self.btndisconnect = tk.Button(self.passengerFrame, text = "Disconnect", command = self.disconnect)

        #PLACING BUTTONS FOR FIRST TABLE: PASSENGERS
        self.btnStartP.place(x = 350, y = 430)
        self.btnLastP.place(x = 600, y = 430)       
        self.btnplusoneP.place(x = 500, y = 430)
        self.btnminusoneP.place(x = 450, y = 430) 
        self.btnplusfiveP.place(x = 550 , y = 430)
        self.btnminusfiveP.place(x = 400, y = 430)
        self.btnInsertP.place(x = 600, y = 250)
        self.btnDeleteP.place(x = 600, y = 350)
        self.btnUpdateP.place(x = 600, y = 300)
        self.btnconnect.place(x = 150, y = 430)
        #self.btnSave.place(x=600, y=200)
        #self.btndisconnect.place(x = 200 , y = 100)

        #LABELS FOR FIRST TABLE: PASSENGERS
        self.lblfirstName = tk.Label(self.passengerFrame, text = "First Name:")

        self.lbllastName = tk.Label(self.passengerFrame, text = "Last Name:")

        self.lbllicenseNum = tk.Label(self.passengerFrame, text = "License Number:")

        self.lblgender = tk.Label(self.passengerFrame, text = "Gender:")

        self.lblnationality = tk.Label(self.passengerFrame, text = "Nationality:")

        self.lblnoFlyStatus = tk.Label(self.passengerFrame, text = "NO-FLY Status:")

        #PLACING LABELS FOR FIRST TABLE: PASSENGERS
        self.lblfirstName.place(x = 350, y = 150)
        self.lbllastName.place(x = 350, y = 200)
        self.lbllicenseNum.place(x = 350, y = 250)
        self.lblgender.place(x = 350, y = 300)
        self.lblnationality.place(x = 350, y = 350)
        self.lblnoFlyStatus.place(x = 350, y = 400)

        #ENTRIES FOR FIRST TABLE: PASSNEGERS
        self.entryfirstName = tk.Entry(self.passengerFrame, bd = 3)

        self.entrylastName = tk.Entry(self.passengerFrame, bd = 3)

        self.entrylicenseNum = tk.Entry(self.passengerFrame, bd = 3)

        self.entrygender = ttk.Combobox(self.passengerFrame, state = 'readonly', background = 'white', values = ["M", "F"])

        self.entrynationality = tk.Entry(self.passengerFrame, bd = 3)

        self.entrynoFlyStatus = ttk.Combobox(self.passengerFrame, state = 'readonly', background = 'white', values = ["FLY", "NOFLY"])

        #PLACING ENTRIES FOR FIRST TABLE: PASSNEGERS
        self.entryfirstName.place(x = 440, y = 150)
        self.entrylastName.place(x = 440, y = 200)
        self.entrylicenseNum.place(x = 440, y = 250)
        self.entrygender.place(x = 440, y = 300)
        self.entrynationality.place(x = 440, y = 350)
        self.entrynoFlyStatus.place(x = 440, y = 400)

        self.p_refresh()
        self.passengerFrame.grid(row = 1, column = 0)
        self.passengersWindow.resizable(False, False)
        self.passengersWindow.mainloop()

        #Arshan Rahman
    def connect(self):
        self.db.createConnection()
        self.p_refresh()
        #Arshan Rahman

    def disconnect(self):
        self.db.breakConnection()
        self.p_clearEntries()


    def p_jumpRec(self, jump):
        # Chris Cruz
        try:
            self.p_pos += jump
            if (self.p_pos > self.p_len-1):
                self.p_pos = self.p_len-1

            if (self.p_pos < 0):
                self.p_pos = 0
            self.p_refresh()
        except:
            return "Error jumping record (Passenger Table)"
    
    def p_refresh(self):
        # Ryan Kennedy
        try:
            self.p_clearEntries()
            self.db.loadPassengers()
            self.db.setPassengerRecord(self.p_pos)
            record = self.db.p_record
            self.entryfirstName.insert(0, record[1])
            self.entrylastName.insert(0, record[2])
            self.entrylicenseNum.insert(0, record[3])
            self.entrygender.set(record[4])
            self.entrynationality.insert(0, record[5])
            self.entrynoFlyStatus.set(record[6])
            self.p_len = len(self.db.p_records)
        except:
            return "Error refreshing GUI (Passenger Table)"

    def p_clearEntries(self):
        # Ryan Kennedy
        self.entryfirstName.delete(0, END)
        self.entrylastName.delete(0, END)
        self.entrylicenseNum.delete(0, END)
        self.entrygender.set("")
        self.entrynationality.delete(0, END)
        self.entrynoFlyStatus.set("")

    def getPInfo(self):
        # Chris Cruz
        result = ["", "", "", "", "", ""]
        result[0] = self.entryfirstName.get()
        result[1] = self.entrylastName.get()
        result[2] = self.entrylicenseNum.get()
        result[3] = self.entrygender.get()
        result[4] = self.entrynationality.get()
        result[5] = self.entrynoFlyStatus.get()
        return result
