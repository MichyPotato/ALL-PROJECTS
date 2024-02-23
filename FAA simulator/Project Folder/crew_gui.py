# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
"""
Nameer Sadiq and Omar Jibreen
Cmdr. Schenk
Crew Management(GUI)
23 March 2023
"""

import os, sys
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
from tkinter import *
from global_database import GlobalDb

class CrewGUI:
  #Initiate - Nameer
  def __init__(self):
    
    self.db = GlobalDb()
    self.connected = False  
    self.currentX = 1 
    self.currentY = [] 
    self.Window()
    self.Menu()
    self.root.mainloop()

  #Connect - Nameer 
  def connect(self):
    if (self.connected == False):
      connectionResult = self.db.createConnection()
      if (connectionResult == 1):
        self.connected = False
      else:
        print("Database Connection Successful")
        self.connected = True


  #Disconnect - Nameer 
  def disconnect(self):
    if (self.connected == True):
      connectionResult = self.db.breakConnection()
      if (connectionResult == 1):#Error Code
        self.connected = True
      else:
        print("Database Disconnect Successful")
        self.connected = False

  #Navugation Methods - Nameer
  def fetch_first(self):
    self.selected_crew = self.db.fetch_first(1)
    self.populate_CrewSpecs(self.selected_crew)
    
  def fetch_last(self):
    self.currentX = 5
    self.selected_crew = self.db.fetch_last(self.currentX)
    self.populate_crewSpecs(self.selected_crew)
  def next(self):
    self.currentX += 1
    self.selected_crew = self.db.next(self.currentX)
    self.populate_crewSpecs(self.selected_crew)
  def forward2(self):
    self.currentX += 2
    self.selected_crew = self.db.forward2(self.currentX)
    self.populate_crewSpecs(self.selected_crew)
  def back(self):
    self.currentX -= 1
    self.selected_crew = self.db.back(self.currentX)
    self.populate_crewSpecs(self.selected_crew)
  def back2(self):
    self.currentX -= 2
    self.selected_crew = self.db.back2(self.currentX)
    self.populate_crewSpecs(self.selected_crew)


  def populate_crewSpecs(self, selected_crew):
    print("selected crew", self.selected_crew)
    self.CrewIDEntry.delete(0, END)
    self.CrewIDEntry.insert(END, self.selected_crew[0])
    self.CaptainIDEntry.delete(0, END)
    self.CaptainIDEntry.insert(END, self.selected_crew[1])
    self.CoPilotIDEntry.delete(0, END)
    self.CoPilotIDEntry.insert(END, self.selected_crew[2])
    self.SeniorFAIDEntry.delete(0, END)
    self.SeniorFAIDEntry.insert(END, self.selected_crew[3])
    self.FA2IDEntry.delete(0, END)
    self.FA2IDEntry.insert(END, self.selected_crew[4])
  
  #Navigation Methods - Nameer
  def start(self):
    self.currentX = 1
    self.readCrew(self.currentX)
    self.moveRec(0)

  def end(self):
    self.currentEntryNumber = len(self.allCrew)
    self.readCrew(self.currentEntryNumber)
    self.moveRec(0)

  def moveRec(self, increment):
    self.allCrew = self.db.fetchByCrewID(increment)   
    self.currentX += increment
    if (self.currentX > len(self.allCrew)):
      self.currentX = len(self.allCrew)
    elif (self.currentX < 1): 
      self.currentX = 1
    self.currentY = self.allCrew[self.currentX-1] 
    try:
      self.ClearFields()
      self.CrewIDEntry.insert(0, str(self.currentX[1]))
      self.CaptainIDEntry.insert(0, str(self.currentX[2]))
      self.CoPilotIDEntry.insert(0, str(self.currentX[3]))
      self.SeniorFAIDEntry.insert(0, str(self.currentX[4]))
      self.FA2IDEntry.set(self.currentX[5])
    except:
      pass

  # Read - Nameer
  def readCrew(self, increment):
    self.Crew = self.db.fetchByCrewID(increment)
    self.moveRec(0)


  #Clear - Nameer 
  def clearFields(self):
    self.CrewIdEntry.delete(0, 'end')
    self.CaptainIDEntry.delete(0, 'end')
    self.CoPilotIDEntry.delete(0, 'end')
    self.SeniorFAIDEntry.delete(0, 'end')
    self.FA2IDEntry.delete(0, 'end')
    
  #Insert - Nameer
  def insert(self):
    if (self.connected == False):
      print("Connect to the database.")
    else:
      CaptainID = str(self.CaptainIDEntry.get())
      CoPilotID = str(self.CoPilotIDEntry.get())
      SeniorFAID = str(self.SeniorFAIDEntry.get())
      FA2ID = str(self.FA2IDEntry.get())
      try:
        self.db.createCrew(CaptainID, CoPilotID, SeniorFAID, FA2ID)
      except:
        print("Failed to add record.")

  #Delete - Nameer
  def delete(self):
    if (self.connected == False):
      print("Connect to the database.")
    else:
      self.db.deleteCrew(str(self.CrewIDEntry.get()))
  
  #Update - Nameer  
  def update(self):
    if (self.connected == False):
      print("Connect to the database.")
    else:
     CrewID = str(self.CrewIDEntry.get()) 
     CaptainID = str(self.CaptainIDEntry.get())
     CoPilotID = str(self.CoPilotIDEntry.get())
     SeniorFAID = str(self.SeniorFAIDEntry.get())
     FA2ID = str(self.FA2IDEntry.get())
    try:
     self.db.updateCrew(CrewID, CaptainID, CoPilotID, SeniorFAID, FA2ID)
    except: 
     print("Failed to update record.")

     #Menu - Omar
  def Menu(self):
    self.Menubar = Menu(self.root)
    self.root.config(menu = self.Menubar)
    #Menu File - Omar
    self.FileMenu = Menu(self.Menubar, tearoff = 0)   
    self.FileMenu.add_command(label = "Connect", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.connect)
    self.FileMenu.add_command(label = "Disconnect", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.disconnect)    
    self.FileMenu.add_command(label = "Exit", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.root.destroy)
    self.Menubar.add_cascade(label = "File", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.FileMenu)

    #Menu Update - Omar
    self.EditMenu = Menu(self.Menubar, tearoff = 0)  
    self.EditMenu.add_command(label = "Add", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.EditMenu.add_command(label = "Update", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.EditMenu.add_command(label = "Delete", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.Menubar.add_cascade(label = "Edit", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.EditMenu)
    
    #Menu Navigate - Omar
    self.NavMenu = Menu(self.Menubar, tearoff = 0)    
    self.NavMenu.add_command(label = "First", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.start) 
    self.NavMenu.add_command(label = "3rd Previous", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveRec(-2))
    self.NavMenu.add_command(label = "Previous", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveRec(-1))
    self.NavMenu.add_command(label = "Next", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveRec(1))
    self.NavMenu.add_command(label = "3rd Next", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveRec(2))
    self.NavMenu.add_command(label = "Last", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.end)
    self.Menubar.add_cascade(label = "Navigate", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.NavMenu)
    
    #Menu Help - Omar
    self.HelpMenu = Menu(self.Menubar, tearoff = 0)
    self.HelpMenu.add_command(label = "About", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.Menubar.add_cascade(label = "Help", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.HelpMenu)
    
 
  def Window(self):
    #Window - Nameer
    self.root = tk.Tk()
    self.root.title("Crew")
    self.root.geometry("800x475")
    
 
    self.Menu()
    #Left - Nameer
    self.LeftFrame = tk.Frame(master = self.root, width = 320, height = 235)
    self.LeftFrame.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
  
    self.BtnFrame = tk.Frame(self.LeftFrame)
    self.BtnFrame.place(x = 20, y = 20)

    self.ExitBtn = tk.Button(self.BtnFrame, text = "Exit", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 8, command = self.root.destroy)
    self.ConnectBtn = tk.Button(self.BtnFrame, text = "Connect", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 9, command = self.connect) 
    self.ExitBtn.grid(row = 0, column = 1, padx = 15)
    self.ConnectBtn.grid(row = 0, column = 2)

     #Right - Nameer
    self.rFrame = tk.Frame(self.root, width = 450, height = 310)
    self.rFrame.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
  
    #Name - Nameer
    self.nameLabel = tk.Label(self.root, text = "Crew", font = ("Times New Roman", 16), fg = ("royalblue4"))
    self.nameLabel.place(x = 360, y = 25)
  
    self.rrFrame = tk.Frame(self.rFrame, width = 450, height = 330)
    self.rrFrame.place(x = 0, y = 10)

    self.dFrame = tk.Frame(self.rrFrame, width = 280, height = 510)
    self.dFrame.place(x = 8, y = 68)
  
    self.CrewIDLBL = tk.Label(self.dFrame, text = "CrewID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.CaptainIDLBL = tk.Label(self.dFrame, text = "CaptainID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.CoPilotIDLBL = tk.Label(self.dFrame, text = "CoPilotID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.SeniorFAIDLBL = tk.Label(self.dFrame, text = "SeniorFAID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.FA2IDLBL = tk.Label(self.dFrame, text = "FA2ID", font = ("Times New Roman", 12), fg = ("royalblue4"))
  
    self.CrewIDEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    self.CaptainIDEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    self.CoPilotIDEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    self.SeniorFAIDEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    self.FA2IDEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    
    self.CrewIDLBL.grid(row = 0, sticky = "W", pady = 10)
    self.CrewIDEntry.grid(row = 0, column = 1, sticky = "W", pady = 10)
    self.CaptainIDLBL.grid(row = 1, sticky = "W", pady = 10)
    self.CaptainIDEntry.grid(row = 1, column = 1, sticky = "W", pady = 10)
    self.CoPilotIDLBL.grid(row = 2, sticky = "W", pady = 10)
    self.CoPilotIDEntry.grid(row = 2, column = 1, sticky = "W", pady = 10)
    self.SeniorFAIDLBL.grid(row = 3, sticky = "W", pady = 10)
    self.SeniorFAIDEntry.grid(row = 3, column = 1, sticky = "W", pady = 10)
    self.FA2IDLBL.grid(row = 4, sticky = "W", pady = 10)
    self.FA2IDEntry.grid(row = 4, column = 1, sticky = "W", pady = 10)
  
  
      
    #CRUD buttons - Omar
    self.crudFrame = tk.Frame(self.rrFrame, width = 200, height = 240)
    self.crudFrame.place(x = 360, y = 95)
  
    self.clearBtn = tk.Button(self.crudFrame, text = "Clear", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.clearFields)
    self.insertBtn = tk.Button(self.crudFrame, text = "Insert", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.insert)
    self.updateBtn = tk.Button(self.crudFrame, text = "Update", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.update)
    self.deleteBtn = tk.Button(self.crudFrame, text = "Delete", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.delete)
  
    self.clearBtn.grid(row = 0, column = 0, pady = 10)
    self.insertBtn.grid(row = 1, column = 0, pady = 10)
    self.updateBtn.grid(row = 3, column = 0, pady = 10)
    self.deleteBtn.grid(row = 5, column = 0, pady = 10)
  
    #NAV buttons - Omar
    self.navFrame = tk.Frame(self.root, width = 700, height = 80)
    self.navFrame.place(x = 130, y = 385)
  
    self.firstBtn = tk.Button(self.navFrame, text = "<<|", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.start) 
    self.prev2Btn = tk.Button(self.navFrame, text = "<<", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveRec(-3))
    self.prevBtn = tk.Button(self.navFrame, text = "<", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveRec(-1))
    self.nextBtn = tk.Button(self.navFrame, text = ">", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveRec(1))
    self.next2Btn = tk.Button(self.navFrame, text = ">>", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveRec(3))
    self.lastBtn = tk.Button(self.navFrame, text = "|>>", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.end)
  
    self.firstBtn.grid(row = 0, column = 0, padx = 15)
    self.prev2Btn.grid(row = 0, column = 2, padx = 13)
    self.prevBtn.grid(row = 0, column = 4, padx = 11)
    self.nextBtn.grid(row = 0, column = 6, padx = 13)
    self.next2Btn.grid(row = 0, column = 8, padx = 15)
    self.lastBtn.grid(row = 0, column = 10)
