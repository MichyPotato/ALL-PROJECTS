# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C 
"""
2/8/2023
Flight Attendant and Pilot GUI
APCSP
Sprint 1 Group 5
"""
import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import Button
import os,sys
import mysql.connector
from global_database import GlobalDb
sys.path.append("Class-Sprint-main\pilot_fa")
from global_database import GlobalDb
from tkinter import messagebox


class PilotGUI():
  def __init__(self):
    self.db = GlobalDb()
    self.connected = False  
    self.currentPilot = 1  
    self.midInsert = False
    #Window and canvas geometry
    self.pilotTableRoot = tk.Tk()
    self.pilotTableRoot.title("Pilot/Flight Attendants Tables")
    self.pilotTableRoot.geometry("800x470")
    self.pilotTableCanvas = tk.Canvas(self.pilotTableRoot,
                                      width=800,
                                      height=470)
    self.pilotTableCanvas.pack()

    #DROPDOWN MENU VARIABLES
    self.pilotVP = tk.StringVar(self.pilotTableRoot)
    self.pilotVP.set("blank")
    self.varPQ1 = tk.StringVar(self.pilotTableRoot)
    self.varPQ1.set("No")
    self.varPQ2 = tk.StringVar(self.pilotTableRoot)
    self.varPQ2.set("No")
    self.varPQ3 = tk.StringVar(self.pilotTableRoot)
    self.varPQ3.set("No")

    #SQL TABLE NAME LABELS
    self.fnLabel = tk.Label(self.pilotTableCanvas, text="First Name", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.lnLabel = tk.Label(self.pilotTableCanvas, text="Last Name", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.posLabel = tk.Label(self.pilotTableCanvas, text="Position", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.pq1 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 1", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.pq2 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 2", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.pq3 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 3", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.idLabel = tk.Label(self.pilotTableCanvas, text="Entry Id:", font = ("Times New Roman", 12), fg = ("royalblue4"),)

    self.fnLabel.place(x=20, y=50)
    self.lnLabel.place(x=20, y=80)
    self.posLabel.place(x=20, y=110)
    self.pq1.place(x=20, y=140)
    self.pq2.place(x=20, y=170)
    self.pq3.place(x=20, y=200)
    self.idLabel.place(x=20, y=20)

    #USER ENTRY WIDGETS
    self.pilotFirstName = tk.Entry(self.pilotTableCanvas)
    self.pilotLastName = tk.Entry(self.pilotTableCanvas)
    self.pilotVarPos = tk.OptionMenu(self.pilotTableCanvas, self.pilotVP,
                                     "First Officer", "Flight Engineer")
    self.planeQualification1 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ1, "Yes", "No")
    self.planeQualification2 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ2, "Yes", "No")
    self.planeQualification3 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ3, "Yes", "No")
    self.pilotId = tk.Text(self.pilotTableCanvas, height=1, width=5)
    self.pilotId.configure(state="disabled")

    self.pilotId.place(x=90, y=20)
    self.pilotFirstName.place(x=90, y=50)
    self.pilotLastName.place(x=90, y=80)
    self.pilotVarPos.place(x=150, y=105)
    self.planeQualification1.place(x=150, y=135)
    self.planeQualification2.place(x=150, y=165)
    self.planeQualification3.place(x=150, y=195)

    #BUTTONS TO NAVIGATE THROUGH THE DATABASE (READ)
    self.pilotsVeryLastButton = Button(self.pilotTableCanvas,
                                       text="<--", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.placeholder)
    self.pilotsLastLastButton = Button(self.pilotTableCanvas,
                                       text="<<", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.placeholder)
    self.pilotsLastButton = Button(self.pilotTableCanvas,
                                   text="<", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                   command=lambda: self.placeholder)
    self.pilotsNextButton = Button(self.pilotTableCanvas,
                                   text=">", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                   command=lambda: self.placeholder)
    self.pilotsNextNextButton = Button(self.pilotTableCanvas,
                                       text=">>", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.placeholder)
    self.pilotsVeryNextButton = Button(self.pilotTableCanvas,
                                       text="-->", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.placeholder)

    self.pilotsVeryLastButton.place(x=30, y=235)
    self.pilotsLastLastButton.place(x=80, y=235)
    self.pilotsLastButton.place(x=120, y=235)
    self.pilotsNextButton.place(x=150, y=235)
    self.pilotsNextNextButton.place(x=180, y=235)
    self.pilotsVeryNextButton.place(x=230, y=235)

    #Data editing frames
    self.edit = tk.Frame(self.pilotTableCanvas, width=140, height=90)
    self.edit.place(x=300, y=105)
    self.pilot_insertFrame = tk.Frame(self.pilotTableCanvas, width=120, height=10)
    self.pilot_insertFrame.place(x=300, y=90)
    #INSERTION BUTTONs
    self.pilot_createbtn = Button(
      self.pilot_insertFrame,
      text="Insert",font = ("Times New Roman", 12), fg = ("royalblue4"),
      command= self.placeholder)
    self.pilot_savebtn = Button(self.pilot_insertFrame, text="Save Insert", command=self.placeholder, font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.pilot_cancelbtn = Button(self.pilot_insertFrame, text="Cancel Insert", command=self.placeholder, font = ("Times New Roman", 12), fg = ("royalblue4"))
    #UPDATE BUTTON
    self.pilot_updatetbn = Button(
      self.pilotTableCanvas, font = ("Times New Roman", 12), fg = ("royalblue4"),
      text="Update",
      command=self.placeholder)

    #DELETE BUTTON
    self.pilot_deletebtn = Button(
      self.pilotTableCanvas, font = ("Times New Roman", 12), fg = ("royalblue4"),
      text="Delete",
      command=self.placeholder)

    self.pilot_createbtn.grid(row=0, column=0)
    self.pilot_updatetbn.grid(row=1, column=0)
    self.pilot_deletebtn.grid(row=2, column=0)

    self.pilotTableRoot.mainloop()
    
  # Pilot Crud methods written by Kingsley
  def clearP(self): #clears all entry fields
    self.pilotFirstName.delete(0, tk.END)
    self.pilotLastName.delete(0, tk.END)
    self.pilotVP.set("blank")
    self.varPQ1.set("No")
    self.varPQ2.set("No")
    self.varPQ3.set("No")
  
  def connectDb(self):
     if (self.connected == False):
      connectionResult = self.db.createConnection()
      if (connectionResult == 1):  # Error
        self.connected = False
      else:  # Success
        self.execConnectBtn.grid_forget()
        self.execDisconnectBtn.grid(row = 0, column = 2)
        print("Database Connection Successful")
        self.connected = True
        
  def disconnectDB(self):
    if (self.connected == True):
      connectionResult = self.db.breakConnection()  
      if (connectionResult == 1):  
        self.connected = True
      else:
        self.connected = False
        print("Database Disconnect Successful")
        self.connected = False
    
  #Pilot insert method 
  #TODO pilot crud methods
  def insertP(self):
    #Checks if the database is connected
    if(self.connected):
      if(not self.midInsert):
        self.clearP()
        self.midInsert = True
        self.pilot_insertFrame.config(height =50)
        self.pilot_savebtn.grid(row=1)
        self.pilot_cancelbtn.grid(row=2)
        self.pilot_createbtn.config(text="Cleared")
        self.pilot_createbtn['state'] = DISABLED
    else:
      print("Error")
      
  def saveP(self):
    if(self.midInsert):
      self.pullP()
      self.db.createPilots()
      self.midInsert = False
      self.clearP()
      self.pilot_insertFrame.config(height=10)
      self.pilot_savebtn.grid_forget()
      self.pilot_cancelbtn.grid_forget()
      self.pilot_createbtn['STATE'] = NORMAL
      self.pilot_createbtn.config(text="Insert")
      self.displayP(0)
      
  def cancelP(self):
    self.pilot_insertFrame.config(height=10)
    self.pilot_savebtn.grid_forget()
    self.pilot_cancelbtn.grid_forget()
    self.pilot_createbtn['state'] = NORMAL
    self.pilot_createbtn.config(text="New")
    self.feedback.config(text="Insert cancelled") #Needs feedback label
    self.midInsert = False
    self.clearP()
    self.displayP(0)
    
  def pullP(self): #Read method
    self.first_name = self.pilotFirstName.get()
    self.last_name = self.pilotLastName.get()
    self.position = self.pilotVP.get()
    self.qual1 = self.varPQ1.get()
    self.qual2 = self.varPQ2.get()
    self.qual3 = self.varPQ3.get()
    
    self.db.insert_pi = [self.first_name, self.last_name, self.position, self.qual1, self.qual2, self.qual3]
  
  def displayP(self, pId):
    try:
      self.holdP =self.db.pilots[self.currentPilot]
      (self.IDcurrent, self.first_name, self.last_name, self.position, self.qual1, self.qual2, self.qual3) = self.holdP
      
      self.clearP()
      self.pilotID.config(text=str(self.IDcurrent)) #Needs to do this
      self.pilotFirstName.insert(0, self.first_name)
      self.pilotLastName.insert(0, self.last_name)
      self.pilotVp.set(self.position)
      self.varPQ1.set(self.qual1)
      self.varPQ2.set(self.qual2)
      self.varPQ3.set(self.qual3)
      print
    except IndexError as s:
      tk.messagebox.showerror("Error", message=("Index  Error: "+ str(s) +" \n No records available."))
    
      
  
  def saveP(self): #Update method
    if(self.db.connect):
      self.IDcurrent = self.IDcurrent
      self.first_name = self.pilotFirstName.get()
      self.last_name = self.pilotLastName.get()
      self.position = self.pilotVarPos.get()
      self.qual1 = self.varPQ1.get()
      self.qual2 = self.varPQ2.get()
      self.qual3 = self.varPQ3.get()
      #Actually updating now
      self.db.update_pi = [self.IDcurrent, self.first_name, self.last_name, self.position, self.qual1, self.qual2, self.qual3]
      self.a = self.db.updatePilots()
      print("Updated pilot")
      a2 = self.db.loadPilots()
      self.feedback.config(text=a2)
      self.displayP(0)
      self.feedback.config(text=self.a)
    else:
      self.feedback.config(text="Not connected") #Need to implement feedback label
  
  def deleteP(self, IDcurrent):
    print("ID= "+str(self.IDcurrent))
    a = self.result = self.db.deletePilots(IDcurrent)
    self.feedback.config(text=self.result)
    self.currentPilot +=-1
    self.feedback.config(text=a)
    self.displayP(0)
  
  def zero_set(self):
    self.currentPilot = 0
  
  def navigateP(self, speed):
    pass
  
    #Pilot Gui written by Nicholas
  def __init__(self):
    
    self.db = GlobalDb()
    self.holdP = (0,"","","","","","")
    self.connected = False  
    self.currentPilot = 1  
    self.midInsert = False
    #Window and canvas geometry
    self.pilotTableRoot = tk.Tk()
    self.pilotTableRoot.title("Pilot/Flight Attendants Tables")
    self.pilotTableRoot.geometry("800x470")
    self.pilotTableCanvas = tk.Canvas(self.pilotTableRoot,
                                      width=800,
                                      height=470)
    self.pilotTableCanvas.pack()

    #DROPDOWN MENU VARIABLES
    self.pilotVP = tk.StringVar(self.pilotTableRoot)
    self.pilotVP.set("blank")
    self.varPQ1 = tk.StringVar(self.pilotTableRoot)
    self.varPQ1.set("No")
    self.varPQ2 = tk.StringVar(self.pilotTableRoot)
    self.varPQ2.set("No")
    self.varPQ3 = tk.StringVar(self.pilotTableRoot)
    self.varPQ3.set("No")

    #SQL TABLE NAME LABELS
    self.fnLabel = tk.Label(self.pilotTableCanvas, text="First Name", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.lnLabel = tk.Label(self.pilotTableCanvas, text="Last Name", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.posLabel = tk.Label(self.pilotTableCanvas, text="Position", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.pq1 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 1", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.pq2 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 2", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.pq3 = tk.Label(self.pilotTableCanvas, text="Plane Qualification 3", font = ("Times New Roman", 12), fg = ("royalblue4"),)
    self.idLabel = tk.Label(self.pilotTableCanvas, text="Entry Id:", font = ("Times New Roman", 12), fg = ("royalblue4"),)

    self.fnLabel.place(x=20, y=50)
    self.lnLabel.place(x=20, y=80)
    self.posLabel.place(x=20, y=110)
    self.pq1.place(x=20, y=140)
    self.pq2.place(x=20, y=170)
    self.pq3.place(x=20, y=200)
    self.idLabel.place(x=20, y=20)

    #USER ENTRY WIDGETS
    self.pilotFirstName = tk.Entry(self.pilotTableCanvas)
    self.pilotLastName = tk.Entry(self.pilotTableCanvas)
    self.pilotVarPos = tk.OptionMenu(self.pilotTableCanvas, self.pilotVP,
                                     "First Officer", "Flight Engineer")
    self.planeQualification1 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ1, "Yes", "No")
    self.planeQualification2 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ2, "Yes", "No")
    self.planeQualification3 = tk.OptionMenu(self.pilotTableCanvas,
                                             self.varPQ3, "Yes", "No")
    self.pilotId = tk.Text(self.pilotTableCanvas, height=1, width=5)
    self.pilotId.configure(state="disabled")

    self.pilotId.place(x=90, y=20)
    self.pilotFirstName.place(x=90, y=50)
    self.pilotLastName.place(x=90, y=80)
    self.pilotVarPos.place(x=150, y=105)
    self.planeQualification1.place(x=150, y=135)
    self.planeQualification2.place(x=150, y=165)
    self.planeQualification3.place(x=150, y=195)

    #BUTTONS TO NAVIGATE THROUGH THE DATABASE (READ)
    self.pilotsVeryLastButton = Button(self.pilotTableCanvas,
                                       text="<--", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.data.placeholder)
    self.pilotsLastLastButton = Button(self.pilotTableCanvas,
                                       text="<<", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.data.placeholder)
    self.pilotsLastButton = Button(self.pilotTableCanvas,
                                   text="<", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                   command=lambda: self.data.placeholder)
    self.pilotsNextButton = Button(self.pilotTableCanvas,
                                   text=">", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                   command=lambda: self.data.placeholder)
    self.pilotsNextNextButton = Button(self.pilotTableCanvas,
                                       text=">>", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.data.placeholder)
    self.pilotsVeryNextButton = Button(self.pilotTableCanvas,
                                       text="-->", font = ("Times New Roman", 12), fg = ("royalblue4"),
                                       command=lambda: self.data.placeholder)

    self.pilotsVeryLastButton.place(x=30, y=235)
    self.pilotsLastLastButton.place(x=80, y=235)
    self.pilotsLastButton.place(x=120, y=235)
    self.pilotsNextButton.place(x=150, y=235)
    self.pilotsNextNextButton.place(x=180, y=235)
    self.pilotsVeryNextButton.place(x=230, y=235)

    #Data editing frames
    self.edit = tk.Frame(self.pilotTableCanvas, width=140, height=90)
    self.edit.place(x=300, y=105)
    self.pilot_insertFrame = tk.Frame(self.pilotTableCanvas, width=120, height=10)
    self.pilot_insertFrame.place(x=300, y=90)
    #INSERTION BUTTONs
    self.pilot_createbtn = Button(
      self.pilot_insertFrame,
      text="Insert",font = ("Times New Roman", 12), fg = ("royalblue4"),
      command= self.data.placeholder)
    self.pilot_savebtn = Button(self.pilot_insertFrame, text="Save Insert", command=self.data.placeholder, font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.pilot_cancelbtn = Button(self.pilot_insertFrame, text="Cancel Insert", command=self.data.placeholder, font = ("Times New Roman", 12), fg = ("royalblue4"))
    #UPDATE BUTTON
    self.pilot_updatetbn = Button(
      self.pilotTableCanvas, font = ("Times New Roman", 12), fg = ("royalblue4"),
      text="Update",
      command=self.data.placeholder)

    #DELETE BUTTON
    self.pilot_deletebtn = Button(
      self.pilotTableCanvas, font = ("Times New Roman", 12), fg = ("royalblue4"),
      text="Delete",
      command=self.data.placeholder)

    self.pilot_createbtn.grid(row=0, column=0)
    self.pilot_updatetbn.grid(row=1, column=0)
    self.pilot_deletebtn.grid(row=2, column=0)

    self.pilotTableRoot.mainloop()

class FAttGUI():
   #Flight attendant Gui written by Nicholas up to "***"
  def __init__(self):
    #Window and canvas geometry
    self.flightAttendantRoot = tk.Tk()
    self.flightAttendantRoot.title("Flight Attendants Tables")
    self.flightAttendantRoot.geometry("800x470")
    self.flightAttendantCanvas = tk.Canvas(self.flightAttendantRoot,
                                           width=450,
                                           height=300)
    self.flightAttendantCanvas.pack()

    #DROPDOWN MENU VARIABLES
    self.faVarPos = tk.StringVar(self.flightAttendantRoot)
    self.faVarPos.set("placeholder1")

    self.fnLabel = tk.Label(self.flightAttendantCanvas, text="First Name")
    self.lnLabel = tk.Label(self.flightAttendantCanvas, text="Last Name")
    self.posLabel = tk.Label(self.flightAttendantCanvas, text="Position")
    self.idLabel = tk.Label(self.flightAttendantCanvas, text="Entry Id:")

    self.fnLabel.place(x=20, y=50)
    self.lnLabel.place(x=20, y=80)
    self.posLabel.place(x=20, y=110)
    self.idLabel.place(x=20, y=20)

    #USER ENTRY WIDGETS
    self.faFirstName = tk.Entry(self.flightAttendantCanvas)
    self.faLastName = tk.Entry(self.flightAttendantCanvas)
    self.pos = tk.OptionMenu(self.flightAttendantCanvas, self.faVarPos,
                             "placeholder1", "placeholder2", "placeholder3",
                             "placeholder4")
    self.faId = tk.Text(self.flightAttendantCanvas, height=1, width=5)
    self.faId.configure(state="disabled")

    self.faFirstName.place(x=90, y=50)
    self.faLastName.place(x=90, y=80)
    self.pos.place(x=90, y=110)
    self.faId.place(x=90, y=20)

    #BUTTONS TO NAVIGATE THROUGH THE DATABASE (READ)
    self.faVeryLastButton = tk.Button(self.flightAttendantCanvas,
                                      text="<--",
                                      command=lambda: self.placeholder)
    self.faLastLastButton = tk.Button(self.flightAttendantCanvas,
                                      text="<<",
                                      command=lambda: self.placeholder)
    self.faLastButton = tk.Button(self.flightAttendantCanvas,
                                  text="<",
                                  command=lambda: self.placeholder)
    self.faNextButton = tk.Button(self.flightAttendantCanvas,
                                  text=">",
                                  command=lambda: self.placeholder)
    self.faNextNextButton = tk.Button(self.flightAttendantCanvas,
                                      text=">>",
                                      command=lambda: self.placeholder)
    self.faVeryNextButton = tk.Button(self.flightAttendantCanvas,
                                      text="-->",
                                      command=lambda: self.placeholder)

    self.faVeryLastButton.place(x=30, y=150)
    self.faLastLastButton.place(x=80, y=150)
    self.faLastButton.place(x=120, y=150)
    self.faNextButton.place(x=150, y=150)
    self.faNextNextButton.place(x=180, y=150)
    self.faVeryNextButton.place(x=230, y=150)

    #***#

    #Flight attendants Gui (Andy and Kinsley)
    # Connection

    #CREATE
    self.flightAttendantsCreateBtn = Button(
      self.flightAttendantCanvas,
      text="Insert",
      command=lambda: self.SqlCommandClass.createFa())
    #READ
    #UPDATE
    #Andy
    self.flightAttendantsUpdateButton = Button(
      self.flightAttendantCanvas,
      text='Update',
      command=lambda: self.SqlCommandClass.updateFa())

    #Andy
    #DELETE
    self.flightAttendantsDeleteButton = Button(
      self.flightAttendantCanvas,
      text='Delete',
      command=lambda: self.SqlCommandClass.deleteFA())

    self.flightAttendantsUpdateButton.place(x=300, y=75)
    self.flightAttendantsDeleteButton.place(x=300, y=125)
    self.flightAttendantsCreateBtn.place(x=300, y=35)
    
    self.flightAttendantRoot.mainloop()




# class TableGui():

#   def aboutOpen(self):
#     #WINDOW THAT IS OPENED WHEN ABOUT TAB PRESSED

#     self.aboutWindow = tk.Tk()
#     self.aboutWindow.title("About")
#     self.aboutWindow.geometry("150x100")

#     self.aboutDesc = Label(
#       self.aboutWindow,
#       text=
#       "GUI/CRUD of Flight Attendants and Pilots for CS50 Period 6 by Group 5",
#       wraplength=100)
#     self.aboutDesc.pack()

# #Method that allows user to return to the main menu

#   def __init__(self):

#     #table gui opener by nicholas
#     self = GlobalDb()
#     self.root = tk.Tk()

#     #menubar for miscelaneous commands
    
#     self.menubar = tk.Menu(self.root)
#     self.root.config(menu=self.menubar)
#     self.filemenu = tk.Menu(self.menubar, tearoff=0)
#     self.filemenu.add_command(label="Exit", command=self.root.quit)
#     self.menubar.add_cascade(label="File", menu=self.filemenu)

#     self.helpmenu = tk.Menu(self.menubar, tearoff=0)
#     self.helpmenu.add_command(label="About", command=self.aboutOpen)
#     self.menubar.add_cascade(label="Help", menu=self.helpmenu)

#     self.connectMenu = tk.Menu(self.menubar, tearoff=0)
#     self.connectMenu.add_command(label="Connect",
#                                  command=lambda: self.createConnection)
#     self.connectMenu.add_command(
#       label="Disconnect", command=lambda: GlobalDb.disconnect(self))
#     self.menubar.add_cascade(label="Database", menu=self.connectMenu)

#     self.recordMenu = tk.Menu(self.menubar, tearoff=0)

#     #Object of the database class
    
#     self.root.title("Opener")
#     self.root.geometry("450x300")

#     self.pilotOpener = Button(self.root,
#                               command=self.pilotWindowOpen,
#                               text="Open Pilot Window")
#     self.flightAttendantOpener = Button(self.root,
#                                         command=self.flightAttendantWindowOpen,
#                                         text="Open FA Window")

#     self.pilotOpener.place(x=60, y=120)
#     self.flightAttendantOpener.place(x=300, y=120)
    
#     self.root.mainloop()



