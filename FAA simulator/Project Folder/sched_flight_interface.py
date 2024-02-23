# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, C       

"""
Moses Dong, Michelle Luo, Lindsay Wang, Erin Li, Thomas Lucas
2 March 2023
AP Computer Science Principles
Period 6
Sprint 2 Scheduled Flights GUI
"""

# Everyone Should Mark Their Own Work (Highlighted Areas Are Done By ___)

import os, sys
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
from tkinter.messagebox import askyesno
from global_database import GlobalDb

class ScheduledGUI:
  #Initiate
  def __init__(self):
    #Work Done by Moses
    self.db = GlobalDb()
    self.connected = False  # Boolean determing whether database is connected or not
    self.currentEntryNumber = 1  # Keeps track of current entry index (not database id)
    self.currentSchedFlights = []  # Keeps track of current database entry and all of its values
    self.schedWindow()
    self.schedMenu()
    self.disableEverything()
    self.root.resizable(False, False)
    self.root.mainloop()

  def disableEverything(self):
    for element in self.schedAUDBtnFrame.winfo_children():
      element.configure(state='disable')
    
    for element in self.schedDataFrame1.winfo_children():
      element.configure(state='disable')

    for element in self.schedDataFrame2.winfo_children():
      element.configure(state='disable')
  
    for element in self.schedRBottomFrame.winfo_children():
      element.configure(state='disable')


  def enableEverything(self):
    for element in self.schedAUDBtnFrame.winfo_children():
      element.configure(state='normal')
    
    for element in self.schedDataFrame1.winfo_children():
      element.configure(state='normal')

    for element in self.schedDataFrame2.winfo_children():
      element.configure(state='normal')

    for element in self.schedRBottomFrame.winfo_children():
      element.configure(state='normal')

  #Connect to Database from Main Window
  def connectDB(self):
    if (self.connected == False):
      connectionResult = self.db.createConnection()
      if (connectionResult == 1):# Error
        self.connected = False
      else:# Success
        self.enableEverything()
        self.connected = True
        self.schedConnectBtn.grid_forget()
        self.schedDisconnectBtn.grid(row = 0, column = 2)
        print("Database Connection Successful")
    # Temporary Solution For Screens 
    self.moveEntrySched(0)
    #schedGuiConnect = self.db.createConnection() #Lindsay
    #self.schedIDDisplay["text"] = (schedGuiConnect[0]) #Lindsay

  #Disconnect database from Main window
  def disconnectDB(self):
    if (self.connected == True):
      connectionResult = self.db.breakConnection()#Possibly add error detection later
      if (connectionResult == 1):#Error Code
        self.connected = True
      else:
        self.disableEverything()
        self.connected = False
        self.schedDisconnectBtn.grid_forget()
        self.schedConnectBtn.grid(row = 0, column = 2)
        print("Database Disconnect Successful")
  #Moses Work Ends

  #Clear Scheduled Flights Screen
  def schedClearScreen(self):
    self.schedLeftFrame.destroy()
    self.schedRightFrame.destroy()

  # Navigation Methods for Scheduled Flights - All by Moses
  # Go To First Entry
  def goToStartSched(self):
    self.currentEntryNumber = 1
    self.readScheduledFlight()
    self.moveEntrySched(0)
    self.schedIDDisplay["text"] = self.currentEntryNumber
    self.db.setSchedId(self.currentEntryNumber)

  # Go To Last Entry
  def goToEndSched(self):
    self.currentEntryNumber = len(self.allSchedFlights)
    self.readScheduledFlight()
    self.moveEntrySched(0)
    self.schedIDDisplay["text"] = self.currentEntryNumber #Lindsay
    self.db.setSchedId(self.currentEntryNumber) #Lindsay

  # Go To Certain Increment
  def moveEntrySched(self, increment):
    self.allSchedFlights = self.db.selectAllScheduledFlights()   
    self.currentEntryNumber += increment
    if (self.currentEntryNumber > len(self.allSchedFlights)):
      self.currentEntryNumber = len(self.allSchedFlights)
    elif (self.currentEntryNumber < 1): 
      self.currentEntryNumber = 1
    self.currentSchedFlights = self.allSchedFlights[self.currentEntryNumber-1]
    print(str(self.currentSchedFlights[0]))
    self.schedClearFields()
    self.schedIDDisplay.config(text = str(self.currentSchedFlights[0]))
    #Show All Entries 
    try:
      self.schedClearFields()
      self.schedIDDisplay["text"] = self.currentSchedFlights[0] #Lindsay
      self.db.setSchedId(self.currentEntryNumber) #Lindsay
      self.schedNameEntry.insert(0, str(self.currentSchedFlights[1]))
      self.schedAirlineIDEntry.insert(0, str(self.currentSchedFlights[2]))
      self.schedDepFieldIDEntry.insert(0, str(self.currentSchedFlights[3]))
      self.schedArrFieldIDEntry.insert(0, str(self.currentSchedFlights[4]))
      self.schedFlightTypeEntry.set(self.currentSchedFlights[5])
      self.schedDistanceEntry.insert(0, str(self.currentSchedFlights[6])) #Currently Not Existing
      self.schedLaunchEntry.insert(0, str(self.currentSchedFlights[7]))
      self.schedLandEntry.insert(0, str(self.currentSchedFlights[8]))
      self.schedAircraftIDEntry.insert(0, str(self.currentSchedFlights[9]))
      self.schedCrewIDEntry.insert(0, str(self.currentSchedFlights[10]))
      self.schedFFPointsEntry.insert(0, str(self.currentSchedFlights[11]))
    except:
      pass

  # Read Scheduled Flight - Moses
  def readScheduledFlight(self):
    self.scheduledFlights = self.db.selectAllScheduledFlights()
    self.moveEntrySched(0)

  # Add's Cancel/Commit Interface - Moses
  def prepareNewScheduledFlight(self):
    self.schedClearFields()
    self.schedAddBtn.grid_forget()
    self.schedUpdateBtn.grid_forget()
    self.schedDeleteBtn.grid_forget()
    self.schedFirstBtn.grid_forget()
    self.schedPrevious3Btn.grid_forget()
    self.schedPreviousBtn.grid_forget()
    self.schedNextBtn.grid_forget()
    self.schedNext3Btn.grid_forget()
    self.schedLastBtn.grid_forget()
    self.schedCommitAddBtn.grid(row = 2, column = 0)
    self.schedCancelCommitBtn.grid(row = 4, column = 0)

  # Leaving Add's Cancel/Commit Interface - Moses
  def leaveNewScheduledInterface(self):
    self.schedFirstBtn.grid(row = 0, column = 0, padx = 15)
    self.schedPrevious3Btn.grid(row = 0, column = 2, padx = 13)
    self.schedPreviousBtn.grid(row = 0, column = 4, padx = 11)
    self.schedNextBtn.grid(row = 0, column = 6, padx = 13)
    self.schedNext3Btn.grid(row = 0, column = 8, padx = 15)
    self.schedLastBtn.grid(row = 0, column = 10)
    self.schedAddBtn.grid(row = 1, column = 0, pady = 10)
    self.schedUpdateBtn.grid(row = 3, column = 0, pady = 10)
    self.schedDeleteBtn.grid(row = 5, column = 0, pady = 10)
    self.schedCommitAddBtn.grid_forget()
    self.schedCancelCommitBtn.grid_forget()
    self.moveEntrySched(0)

  #Lindsay: Clear fields when adding a new record
  def schedClearFields(self):
    self.schedNameEntry.delete(0, 'end')
    self.schedAirlineIDEntry.delete(0, 'end')
    self.schedDepFieldIDEntry.delete(0, 'end')
    self.schedArrFieldIDEntry.delete(0, 'end')
    self.schedFlightTypeEntry.set("")
    self.schedDistanceEntry.delete(0, 'end')
    self.schedLaunchEntry.delete(0, 'end')
    self.schedLandEntry.delete(0, 'end')
    self.schedAircraftIDEntry.delete(0, 'end')
    self.schedCrewIDEntry.delete(0, 'end')
    self.schedFFPointsEntry.delete(0, 'end')
    self.schedIDDisplay["text"] = ""

  #Lindsay: Combines the schedInsert(), leaveNewScheduledInterface(), goToEndSched() methods when clicking the commit button
  def schedAddCommit(self):
    self.schedInsert()
    self.leaveNewScheduledInterface()
    self.goToEndSched()
    
  #Michelle: Insert into Scheduled Flights
  def schedInsert(self):
    #os.system("clear")
    if (self.connected == False):
      print("Please connect to the database.")
    else:
      name = str(self.schedNameEntry.get())
      airlineID = str(self.schedAirlineIDEntry.get())
      depFieldID = str(self.schedDepFieldIDEntry.get())
      arrFieldID = str(self.schedArrFieldIDEntry.get())
      flightType = str(self.schedFlightTypeEntry.get())
      distance = str(self.schedDistanceEntry.get())
      launch = str(self.schedLaunchEntry.get())
      land = str(self.schedLandEntry.get())
      aircraftID = str(self.schedAircraftIDEntry.get())
      crewID = str(self.schedCrewIDEntry.get())
      ffPoints = str(self.schedFFPointsEntry.get())
      #try:
      schedGuiInsert = self.db.insertScheduledFlight(name, airlineID, depFieldID, arrFieldID, flightType, distance, launch, land, aircraftID, crewID, ffPoints) #Lindsay
      self.schedIDDisplay["text"] = (schedGuiInsert[0]) #Lindsay
      #except:
        #print("Failed to add record to Scheduled Flights Table.")
    #self.leaveNewScheduledInterface()

  # Lindsay: Update in Scheduled Flights
  def schedUpdate(self):
    if (self.connected == False):
      print("Please connect to the database.")
    else:
      givenId = self.db.getSchedId()
      flight_name = str(self.schedNameEntry.get())
      airline_id = str(self.schedAirlineIDEntry.get())
      dep_field_id = str(self.schedDepFieldIDEntry.get())
      #Michelle added in arr_field_id [missing before]
      arr_field_id = str(self.schedArrFieldIDEntry.get())
      flight_type = str(self.schedFlightTypeEntry.get())
      distance = str(self.schedDistanceEntry.get())
      scheduled_launch = str(self.schedLaunchEntry.get())
      scheduled_land = str(self.schedLandEntry.get())
      aircraft_id = str(self.schedAircraftIDEntry.get())
      crew_id = str(self.schedCrewIDEntry.get())
      ff_points = str(self.schedFFPointsEntry.get())
      try:
        self.db.updateScheduledFlight(flight_name, airline_id, dep_field_id, arr_field_id, flight_type, distance, scheduled_launch, scheduled_land, aircraft_id, crew_id, ff_points, givenId)
        print("Update successful in Scheduled Flights table.")
      except:
        print("Failed to update record in Scheduled Flights table.")

  #Erin: Delete from Scheduled Flights
  def schedDelete(self):
    if (self.connected == False):
      print("Please connect to the database.")
    else:
      userResponse = askyesno(title = "Delete", message = "Are you sure you want \n to delete this entry?")
      if (userResponse == True):
        self.db.deleteScheduledFlight(self.currentSchedFlights[0])
        self.moveEntrySched(0)
  
  ### Lindsay Road Work Begins ###
  
  #Scheduled Flights Menu
  def schedMenu(self):
    self.schedMenubar = Menu(self.root)
    self.root.config(menu = self.schedMenubar)
    #Menu: File
    self.schedFileMenu = Menu(self.schedMenubar, tearoff = 0)   
    self.schedFileMenu.add_command(label = "Connect", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.connectDB)
    self.schedFileMenu.add_command(label = "Disconnect", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.disconnectDB)    
    self.schedFileMenu.add_command(label = "Exit", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.root.destroy)
    self.schedMenubar.add_cascade(label = "File", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.schedFileMenu)

    #Menu: Update
    self.schedEditMenu = Menu(self.schedMenubar, tearoff = 0)  
    self.schedEditMenu.add_command(label = "Add", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.schedEditMenu.add_command(label = "Update", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.schedEditMenu.add_command(label = "Delete", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.schedMenubar.add_cascade(label = "Edit", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.schedEditMenu)
    
    #Menu: Navigate
    self.schedNavMenu = Menu(self.schedMenubar, tearoff = 0)    
    self.schedNavMenu.add_command(label = "First", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.goToStartSched) #Moses added all commands to navigation buttons
    self.schedNavMenu.add_command(label = "3rd Previous", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveEntrySched(-3))
    self.schedNavMenu.add_command(label = "Previous", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveEntrySched(-1))
    self.schedNavMenu.add_command(label = "Next", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveEntrySched(1))
    self.schedNavMenu.add_command(label = "3rd Next", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = lambda: self.moveEntrySched(3))
    self.schedNavMenu.add_command(label = "Last", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.goToEndSched)
    self.schedMenubar.add_cascade(label = "Navigate", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.schedNavMenu)
    
    #Menu: Help
    self.schedHelpMenu = Menu(self.schedMenubar, tearoff = 0)
    self.schedHelpMenu.add_command(label = "About", font = ("Times New Roman", 12), foreground = ("royalblue4"))#, command = self.aboutPopup)
    self.schedMenubar.add_cascade(label = "Help", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.schedHelpMenu)
    
  #Scheduled Flights Window
  def schedWindow(self):
    #Window
    self.root = tk.Tk()
    self.root.title("Scheduled Flights")
    self.root.geometry("800x475")
    
    #os.system("clear")
    self.schedMenu()
    #self.clearScreen()
    #Frames: Left
    self.schedLeftFrame = tk.Frame(master = self.root, width = 320, height = 235)
    self.schedLeftFrame.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
  
    #Frames: Left -> Connect/Disconnect Buttons
    self.schedBtnFrame = tk.Frame(self.schedLeftFrame)
    self.schedBtnFrame.place(x = 20, y = 20)

    self.schedExitBtn = tk.Button(self.schedBtnFrame, text = "Exit", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 8, command = self.root.destroy)
    self.schedConnectBtn = tk.Button(self.schedBtnFrame, text = "Connect", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 9, command = self.connectDB) #Make sure when adding the changing button, you change the connect/disconnect methods to have if/else so they connect or disconnect based on the current status
    self.schedDisconnectBtn = tk.Button(self.schedBtnFrame, text = "Disconnect", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 9, command = self.disconnectDB) 
    
    self.schedExitBtn.grid(row = 0, column = 1, padx = 15)
    self.schedConnectBtn.grid(row = 0, column = 2)

    #Frames: Right -> Middle-Right -> Data
    self.schedDataFrame1 = tk.Frame(self.schedLeftFrame, width = 300, height = 410)
    self.schedDataFrame1.place(x = 5, y = 80)

    self.schedIDLbl = tk.Label(self.schedDataFrame1, text = "ID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedNameLbl = tk.Label(self.schedDataFrame1, text = "Name", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedAirlineIDLbl = tk.Label(self.schedDataFrame1, text = "Airline ID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedDepFieldIDLbl = tk.Label(self.schedDataFrame1, text = "Dep. Field ID ", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedArrFieldIDLbl = tk.Label(self.schedDataFrame1, text = "Arr. Field ID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedFlightTypeLbl = tk.Label(self.schedDataFrame1, text = "Flight Type", font = ("Times New Roman", 12), fg = ("royalblue4"))
    
    self.schedIDDisplay = tk.Label(self.schedDataFrame1, text = "", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedNameEntry = tk.Entry(self.schedDataFrame1, font = ("Times New Roman", 12), width = 20)
    self.schedAirlineIDEntry = tk.Entry(self.schedDataFrame1, font = ("Times New Roman", 12), width = 20)
    self.schedDepFieldIDEntry = tk.Entry(self.schedDataFrame1, font = ("Times New Roman", 12), width = 20)
    self.schedArrFieldIDEntry = tk.Entry(self.schedDataFrame1, font = ("Times New Roman", 12), width = 20)
    self.schedFlightTypeEntry = ttk.Combobox(self.schedDataFrame1, state = 'readonly', background = ("white"), font = ("Times New Roman", 12), width = 19, values = ["COMMERCIAL", "NON-COMMERCIAL"])

    self.schedIDLbl.grid(row = 0, sticky = "W", pady = 10)
    self.schedIDDisplay.grid(row = 0, column = 1, sticky = "W", pady = 10)
    self.schedNameLbl.grid(row = 1, sticky = "W", pady = 10)
    self.schedNameEntry.grid(row = 1, column = 1, sticky = "W", pady = 10)
    self.schedAirlineIDLbl.grid(row = 2, sticky = "W", pady = 10)
    self.schedAirlineIDEntry.grid(row = 2, column = 1, sticky = "W", pady = 10)
    self.schedDepFieldIDLbl.grid(row = 3, sticky = "W", pady = 10)
    self.schedDepFieldIDEntry.grid(row = 3, column = 1, sticky = "W", pady = 10)
    self.schedArrFieldIDLbl.grid(row = 4, sticky = "W", pady = 10)
    self.schedArrFieldIDEntry.grid(row = 4, column = 1, sticky = "W", pady = 10)
    self.schedFlightTypeLbl.grid(row = 5, sticky = "W", pady = 10)
    self.schedFlightTypeEntry.grid(row = 5, column = 1, sticky = "W", pady = 10)
    
    #Frames: Right
    self.schedRightFrame = tk.Frame(self.root, width = 450, height = 310)
    self.schedRightFrame.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
  
    #Frames: Right -> Welcome Frame
    self.schedWelcomeLabel = tk.Label(self.root, text = "Scheduled Flights", font = ("Times New Roman", 16), fg = ("royalblue4"))
    self.schedWelcomeLabel.place(x = 360, y = 25)
  
    #Frames: Right -> Middle-Right
    self.schedRMiddleFrame = tk.Frame(self.schedRightFrame, width = 450, height = 330)
    self.schedRMiddleFrame.place(x = 0, y = 10)
  
    #Frames: Right -> Middle-Right -> Data
    self.schedDataFrame2 = tk.Frame(self.schedRMiddleFrame, width = 280, height = 510)
    self.schedDataFrame2.place(x = 8, y = 68)
  
    self.schedDistanceLbl = tk.Label(self.schedDataFrame2, text = "Distance", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedLaunchLbl = tk.Label(self.schedDataFrame2, text = "Launch Time", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedLandLbl = tk.Label(self.schedDataFrame2, text = "Land Time", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedAircraftIDLbl = tk.Label(self.schedDataFrame2, text = "Aircraft ID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedCrewIDLbl = tk.Label(self.schedDataFrame2, text = "Crew ID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.schedFFPointsLbl = tk.Label(self.schedDataFrame2, text = "Freq. Flyer Pts  ", font = ("Times New Roman", 12), fg = ("royalblue4"))

    self.schedDistanceEntry = tk.Entry(self.schedDataFrame2, font = ("Times New Roman", 12), width = 19)
    self.schedLaunchEntry = tk.Entry(self.schedDataFrame2, font = ("Times New Roman", 12), width = 19)
    self.schedLandEntry = tk.Entry(self.schedDataFrame2, font = ("Times New Roman", 12), width = 19)
    self.schedAircraftIDEntry = tk.Entry(self.schedDataFrame2, font = ("Times New Roman", 12), width = 19)
    self.schedCrewIDEntry = tk.Entry(self.schedDataFrame2, font = ("Times New Roman", 12), width = 19)
    self.schedFFPointsEntry = tk.Entry(self.schedDataFrame2, font = ("Times New Roman", 12), width = 19)
  
    self.schedDistanceLbl.grid(row = 0, sticky = "W", pady = 10)
    self.schedDistanceEntry.grid(row = 0, column = 1, sticky = "W", pady = 10)
    self.schedLaunchLbl.grid(row = 1, sticky = "W", pady = 10)
    self.schedLaunchEntry.grid(row = 1, column = 1, sticky = "W", pady = 10)
    self.schedLandLbl.grid(row = 2, sticky = "W", pady = 10)
    self.schedLandEntry.grid(row = 2, column = 1, sticky = "W", pady = 10)
    self.schedAircraftIDLbl.grid(row = 3, sticky = "W", pady = 10)
    self.schedAircraftIDEntry.grid(row = 3, column = 1, sticky = "W", pady = 10)
    self.schedCrewIDLbl.grid(row = 4, sticky = "W", pady = 10)
    self.schedCrewIDEntry.grid(row = 4, column = 1, sticky = "W", pady = 10)
    self.schedFFPointsLbl.grid(row = 5, sticky = "W", pady = 10)
    self.schedFFPointsEntry.grid(row = 5, column = 1, sticky = "W", pady = 10)
      
    #Frames: Right -> Middle-Right -> Clear/Add/Update/Delete Buttons
    self.schedAUDBtnFrame = tk.Frame(self.schedRMiddleFrame, width = 200, height = 240)
    self.schedAUDBtnFrame.place(x = 360, y = 95)
  
    self.schedAddBtn = tk.Button(self.schedAUDBtnFrame, text = "Add", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.prepareNewScheduledFlight)
    self.schedUpdateBtn = tk.Button(self.schedAUDBtnFrame, text = "Update", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.schedUpdate)
    self.schedDeleteBtn = tk.Button(self.schedAUDBtnFrame, text = "Delete", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.schedDelete)
    self.schedCommitAddBtn = tk.Button(self.schedAUDBtnFrame, text = "Commit", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.schedAddCommit)
    self.schedCancelCommitBtn = tk.Button(self.schedAUDBtnFrame, text = "Cancel", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.leaveNewScheduledInterface)
    
    self.schedAddBtn.grid(row = 1, column = 0, pady = 10)
    self.schedUpdateBtn.grid(row = 3, column = 0, pady = 10)
    self.schedDeleteBtn.grid(row = 5, column = 0, pady = 10)
  
    #Frames: Right -> Bottom (First, Prev, Next, Last Buttons)
    self.schedRBottomFrame = tk.Frame(self.root, width = 700, height = 80)
    self.schedRBottomFrame.place(x = 130, y = 385)
  
    self.schedFirstBtn = tk.Button(self.schedRBottomFrame, text = "First", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.goToStartSched) #Moses added commands to all navigation buttons
    self.schedPrevious3Btn = tk.Button(self.schedRBottomFrame, text = "<<", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveEntrySched(-3))
    self.schedPreviousBtn = tk.Button(self.schedRBottomFrame, text = "<", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveEntrySched(-1))
    self.schedNextBtn = tk.Button(self.schedRBottomFrame, text = ">", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveEntrySched(1))
    self.schedNext3Btn = tk.Button(self.schedRBottomFrame, text = ">>", font = ("Times New Roman", 14), fg = ("royalblue4"), command = lambda: self.moveEntrySched(3))
    self.schedLastBtn = tk.Button(self.schedRBottomFrame, text = "Last", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.goToEndSched)
  
    self.schedFirstBtn.grid(row = 0, column = 0, padx = 15)
    self.schedPrevious3Btn.grid(row = 0, column = 2, padx = 13)
    self.schedPreviousBtn.grid(row = 0, column = 4, padx = 11)
    self.schedNextBtn.grid(row = 0, column = 6, padx = 13)
    self.schedNext3Btn.grid(row = 0, column = 8, padx = 15)
    self.schedLastBtn.grid(row = 0, column = 10)

### Lindsay Road Work Ends ###
