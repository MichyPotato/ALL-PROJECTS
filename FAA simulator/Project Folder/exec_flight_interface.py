# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, C       

"""
Moses Dong, Michelle Luo, Lindsay Wang, Erin Li, Thomas Lucas
23 March 2023
AP Computer Science Principles
Period 6
Sprint 2 Executed Flights GUI
"""

import os, sys
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
from tkinter.messagebox import askyesno
from global_database import GlobalDb


class ExecutedGUI:
  # Work Done by Moses
  #Initiate
  def __init__(self):
    self.db = GlobalDb()
    self.connected = False  # Boolean determing whether database is connected or not
    self.currentEntryNumber = 1  # Keeps track of current entry index (not database id)
    self.currentEntry = []  # Keeps track of current database entry and all of its values
    self.execWindow()
    self.execMenu()
    self.disableEverything()
    self.root.resizable(False, False)
    self.root.mainloop()

  #Connect to Database from Main Window
  def connectDB(self):
    if (self.connected == False):
      connectionResult = self.db.createConnection()
      if (connectionResult == 1):  # Error
        self.connected = False
      else:  # Success
        self.enableEverything()
        self.execConnectBtn.grid_forget()
        self.execDisconnectBtn.grid(row = 0, column = 2)
        self.connected = True
        print("Database Connection Successful")

    # Temporary Solution For Screens
    self.moveEntryExec(0)

  def disableEverything(self):
    for element in self.execAUDBtnFrame.winfo_children():
      element.configure(state='disable')
    
    for element in self.execDataFrame1.winfo_children():
      element.configure(state='disable')

    for element in self.execDataFrame2.winfo_children():
      element.configure(state='disable')
  
    for element in self.execRBottomFrame.winfo_children():
      element.configure(state='disable')

  def enableEverything(self):
    for element in self.execAUDBtnFrame.winfo_children():
      element.configure(state='normal')
    
    for element in self.execDataFrame1.winfo_children():
      element.configure(state='normal')

    for element in self.execDataFrame2.winfo_children():
      element.configure(state='normal')

    for element in self.execRBottomFrame.winfo_children():
      element.configure(state='normal')

  #Disconnect database from Main window
  def disconnectDB(self):
    if (self.connected == True):
      connectionResult = self.db.breakConnection(
      )  #Possibly add error detection later
      if (connectionResult == 1):  #Error Code
        self.connected = True
      else:
        self.disableEverything
        self.connected = False
        self.execDisconnectBtn.grid_forget()
        self.execConnectBtn.grid(row = 0, column = 2)
        print("Database Disconnect Successful")

  # Moses Work Ends

  #Clear Executed Flights Screen
  def execClearScreen(self):
    self.execLeftFrame.destroy()
    self.execRightFrame.destroy()

  # Navigation Methods for Executed Flights - All by Moses
  # Go To First Entry
  def goToStartExec(self):
    self.currentEntryNumber = 1
    self.readExecutedFlight()
    self.moveEntryExec(0)
    self.execIDDisplay["text"] = self.currentEntryNumber #Lindsay
    self.db.setExecId(self.currentEntryNumber) #Lindsay

  # Go To Last Entry
  def goToEndExec(self):
    self.currentEntryNumber = len(self.allExecFlights)
    self.readExecutedFlight()
    self.moveEntryExec(0)
    self.execIDDisplay["text"] = self.currentEntryNumber #Lindsay
    self.db.setExecId(self.currentEntryNumber) #Lindsay

  # Go To Certain Increment
  def moveEntryExec(self, increment):
    self.allExecFlights = self.db.selectAllExecutedFlights()
    self.currentEntryNumber += increment
    if (self.currentEntryNumber > len(self.allExecFlights)):
      self.currentEntryNumber = len(self.allExecFlights)
    elif (self.currentEntryNumber < 1):
      self.currentEntryNumber = 1
    print(self.allExecFlights)
    self.currentExecFlight = self.allExecFlights[self.currentEntryNumber-1]
    self.execClearFields()
    self.execIDDisplay.config(text = str(self.currentExecFlight[0]))
    #Show All Entries
    try:
      self.execClearFields()
      self.execIDDisplay["text"] = self.currentExecFlight[0] #Lindsay
      self.db.setExecId(self.currentEntryNumber) #Lindsay
      self.execSchedFlightIDEntry.insert(0, str(self.currentExecFlight[6]))
      self.execNameEntry.insert(0, str(self.currentExecFlight[1]))
      self.execAirlineIDEntry.insert(0, str(self.currentExecFlight[2]))
      self.execDepFieldIDEntry.insert(0, str(self.currentExecFlight[3]))
      self.execArrFieldIDEntry.insert(0, str(self.currentExecFlight[4]))
      self.execFlightTypeEntry.set(self.currentExecFlight[5])
      self.execUpDownStatEntry.set(self.currentExecFlight[7])
      self.execDistanceEntry.insert(0, str(self.currentExecFlight[8]))  
      self.execLaunchEntry.insert(0, str(self.currentExecFlight[9]))
      self.execLandEntry.insert(0, str(self.currentExecFlight[10]))
      self.execAircraftIDEntry.insert(0, str(self.currentExecFlight[11]))
      self.execCrewIDEntry.insert(0, str(self.currentExecFlight[12]))
      self.execPassListIDEntry.insert(0, str(self.currentExecFlight[13]))
      self.execFFPointsEntry.insert(0, str(self.currentExecFlight[14]))
    except:
      pass

  # Read Executed Flight - Moses
  def readExecutedFlight(self):
    self.executedFlights = self.db.selectAllExecutedFlights()
    self.moveEntryExec(0)

  # Add's Cancel/Commit Interface - Moses
  def prepareNewExecutedFlight(self):
    self.execClearFields()
    self.execAddBtn.grid_forget()
    self.execUpdateBtn.grid_forget()
    self.execDeleteBtn.grid_forget()
    self.execFirstBtn.grid_forget()
    self.execPrevious3Btn.grid_forget()
    self.execPreviousBtn.grid_forget()
    self.execNextBtn.grid_forget()
    self.execNext3Btn.grid_forget()
    self.execLastBtn.grid_forget()
    self.execConnectBtn.grid_forget()
    self.execCommitAddBtn.grid(row=2, column=0)
    self.execCancelCommitBtn.grid(row=4, column=0)

  # Leaving Add's Cancel/Commit Interface - Moses
  def leaveNewExecutedInterface(self):
    self.execAddBtn.grid(row=1, column=0, pady=10)
    self.execUpdateBtn.grid(row=3, column=0, pady=10)
    self.execDeleteBtn.grid(row=5, column=0, pady=10)
    self.execTriggerBtn.grid(row=7, column=0, pady=10)
    self.execFirstBtn.grid(row=0, column=0, padx=15)
    self.execPrevious3Btn.grid(row=0, column=2, padx=13)
    self.execPreviousBtn.grid(row=0, column=4, padx=11)
    self.execNextBtn.grid(row=0, column=6, padx=13)
    self.execNext3Btn.grid(row=0, column=8, padx=15)
    self.execLastBtn.grid(row=0, column=10)
    self.execCommitAddBtn.grid_forget()
    self.execCancelCommitBtn.grid_forget()
    self.execAddBtn.grid(row=1, column=0)
    self.execUpdateBtn.grid(row=3, column=0)
    self.execDeleteBtn.grid(row=5, column=0)
    self.moveEntryExec(0)

  #Lindsay: Clear fields when adding a new record
  def execClearFields(self):
    self.execSchedFlightIDEntry.delete(0, 'end')
    self.execNameEntry.delete(0, 'end')
    self.execAirlineIDEntry.delete(0, 'end')
    self.execDepFieldIDEntry.delete(0, 'end')
    self.execArrFieldIDEntry.delete(0, 'end')
    self.execFlightTypeEntry.set("")
    self.execUpDownStatEntry.set("")
    self.execDistanceEntry.delete(0, 'end')
    self.execLaunchEntry.delete(0, 'end')
    self.execLandEntry.delete(0, 'end')
    self.execAircraftIDEntry.delete(0, 'end')
    self.execCrewIDEntry.delete(0, 'end')
    self.execPassListIDEntry.delete(0, 'end')
    self.execFFPointsEntry.delete(0, 'end')
    self.execIDDisplay["text"] = ""

  #Michelle's executed Trigger to flood fill things from Scheduled Flights
  def execTrigger(self):
    #gets the desired schedued flight ID
    self.schedFlightID = self.execSchedFlightIDEntry.get()
    #empty list
    self.schedFlightLoad=[]
    #clears the rest of the fields
    self.execClearFields()
    #calls upon the executedFlightTrigger function in global_database
    self.schedFlightLoad=self.db.executedFlightTrigger(self.schedFlightID)
    #inserted loaded scheduled flight values into executed GUI
    self.execSchedFlightIDEntry.insert(0, self.schedFlightID)
    self.execNameEntry.insert(0, str(self.schedFlightLoad[0]))
    self.execAirlineIDEntry.insert(0, str(self.schedFlightLoad[1]))
    self.execDepFieldIDEntry.insert(0, str(self.schedFlightLoad[2]))
    self.execArrFieldIDEntry.insert(0, str(self.schedFlightLoad[3]))
    self.execFlightTypeEntry.set(self.schedFlightLoad[4])
    #self.execUpDownStatEntry.set(self.schedFlightLoad[7])
    self.execDistanceEntry.insert(0, str(self.schedFlightLoad[5]))  
    self.execLaunchEntry.insert(0, str(self.schedFlightLoad[6]))
    self.execLandEntry.insert(0, str(self.schedFlightLoad[7]))
    self.execAircraftIDEntry.insert(0, str(self.schedFlightLoad[8]))
    self.execCrewIDEntry.insert(0, str(self.schedFlightLoad[9]))
    #self.execPassListIDEntry.insert(0, str(self.schedFlightLoad[13]))
    self.execFFPointsEntry.insert(0, str(self.schedFlightLoad[10]))
    
  #Lindsay: Combines the schedInsert(), leaveNewScheduledInterface(), goToEndSched() methods when clicking the commit button
  def execAddCommit(self):
    self.execInsert()
    self.leaveNewExecutedInterface()
    self.goToEndExec()

  #Insert into Executed Flights
  def execInsert(self):
    if (self.connected == False):
      print("Please connect to the database.")
    else:
      #execFlightID = str(self.execSchedFlightIDEntry.get())
      name = str(self.execNameEntry.get())
      airlineID = str(self.execAirlineIDEntry.get())
      depFieldID = str(self.execDepFieldIDEntry.get())
      arrFieldID = str(self.execArrFieldIDEntry.get())
      flightType = str(self.execFlightTypeEntry.get())
      sched_flight_id = str(self.execSchedFlightIDEntry.get())
      upDownStatus = str(self.execUpDownStatEntry.get())
      distance = str(self.execDistanceEntry.get())
      launch = str(self.execLaunchEntry.get())
      land = str(self.execLandEntry.get())
      aircraftID = str(self.execAircraftIDEntry.get())
      crewID = str(self.execCrewIDEntry.get())
      passListID = str(self.execPassListIDEntry.get())
      ffPoints = str(self.execFFPointsEntry.get())
      try:
        execGuiInsert = self.db.insertExecutedFlight(name, airlineID, depFieldID, arrFieldID, flightType, sched_flight_id, upDownStatus, distance, launch, land,aircraftID, crewID, passListID, ffPoints) #Lindsay
        self.execIDDisplay["text"] = (execGuiInsert[0]) #Lindsay
      except:
        print("Failed to add record.")

  #Delete from Executed Flights
  def execDelete(self):
    #os.system("clear")
    if (self.connected == False):
      print("Please connect to the database.")
    else:
      userResponse = askyesno(title = "Delete", message = "Are you sure you want \n to delete this entry?")
      if (userResponse == True):
        self.db.deleteExecutedFlight(self.currentExecFlight[0])
        self.moveEntryExec(0)

  # Lindsay: Update in Executed Flights
  def execUpdate(self):
    #os.system("clear")
    if (self.connected == False):
      print("Please connect to the database.")
    else:
      givenId = self.db.getExecId()
      sched_flight_id = str(self.execSchedFlightIDEntry.get())
      name = str(self.execNameEntry.get())
      airlineID = str(self.execAirlineIDEntry.get())
      depFieldID = str(self.execDepFieldIDEntry.get())
      arrFieldID = str(self.execArrFieldIDEntry.get())
      flightType = str(self.execFlightTypeEntry.get())
      upDownStatus = str(self.execUpDownStatEntry.get())
      distance = str(self.execDistanceEntry.get())
      launch = str(self.execLaunchEntry.get())
      land = str(self.execLandEntry.get())
      aircraftID = str(self.execAircraftIDEntry.get())
      crewID = str(self.execCrewIDEntry.get())
      passListID = str(self.execPassListIDEntry.get())
      ffPoints = str(self.execFFPointsEntry.get())
      try:
        self.db.updateExecutedFlight(name, airlineID, depFieldID, arrFieldID, flightType, sched_flight_id, upDownStatus, distance, launch, land, aircraftID, crewID, passListID, ffPoints, givenId)
        print("Update successful in Executed Flights table.")
      except:
        print("Failed to update record in Executed Flights table.")

  #Executed Flights Menu
  def execMenu(self):
    self.execMenubar = Menu(self.root)
    self.root.config(menu=self.execMenubar)
    #Menu: File
    self.execFileMenu = Menu(self.execMenubar, tearoff=0)
    self.execFileMenu.add_command(label="Connect",
                                  font=("Times New Roman", 12),
                                  foreground=("royalblue4"),
                                  command=self.connectDB)
    self.execFileMenu.add_command(label="Disconnect",
                                  font=("Times New Roman", 12),
                                  foreground=("royalblue4"),
                                  command=self.disconnectDB)
    self.execFileMenu.add_command(label="Exit",
                                  font=("Times New Roman", 12),
                                  foreground=("royalblue4"),
                                  command=self.root.destroy)
    self.execMenubar.add_cascade(label="File",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 menu=self.execFileMenu)

    #Menu: Update
    self.execEditMenu = Menu(self.execMenubar, tearoff=0)
    self.execEditMenu.add_command(
      label="Create", font=("Times New Roman", 12),
      foreground=("royalblue4"))  #, command = self.execCreateTable)
    self.execEditMenu.add_command(
      label="Drop", font=("Times New Roman", 12),
      foreground=("royalblue4"))  #, command = self.execDropTable)
    self.execEditMenu.add_command(
      label="Add", font=("Times New Roman", 12),
      foreground=("royalblue4"))  #, command = self.yesNoCInsertMsgbox)
    self.execEditMenu.add_command(
      label="Update", font=("Times New Roman", 12),
      foreground=("royalblue4"))  #, command = self.yesNoCUpdateMsgbox)
    self.execEditMenu.add_command(
      label="Delete", font=("Times New Roman", 12),
      foreground=("royalblue4"))  #, command = self.yesNoCDeleteMsgbox)
    self.execMenubar.add_cascade(label="Edit",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 menu=self.execEditMenu)

    #Menu: Navigate
    self.execNavMenu = Menu(self.execMenubar, tearoff=0)
    self.execNavMenu.add_command(label="First",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 command=self.goToStartExec) # Moses added commands to all navigation buttons
    self.execNavMenu.add_command(label="3rd Previous",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 command=lambda:self.moveEntryExec(-3))
    self.execNavMenu.add_command(label="Previous",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 command=lambda:self.moveEntryExec(-1))
    self.execNavMenu.add_command(label="Next",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 command=lambda:self.moveEntryExec(1))
    self.execNavMenu.add_command(label="3rd Next",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 command=lambda:self.moveEntryExec(3))
    self.execNavMenu.add_command(label="Last",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 command=lambda:self.goToEndExec)
    self.execMenubar.add_cascade(label="Navigate",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 menu=lambda:self.execNavMenu)

    #Menu: Help
    self.execHelpMenu = Menu(self.execMenubar, tearoff=0)
    self.execHelpMenu.add_command(
      label="About", font=("Times New Roman", 12),
      foreground=("royalblue4"))  #, command = self.aboutPopup)
    self.execMenubar.add_cascade(label="Help",
                                 font=("Times New Roman", 12),
                                 foreground=("royalblue4"),
                                 menu=self.execHelpMenu)

  #Executed Flights Window
  def execWindow(self):
    #Window
    self.root = tk.Tk()
    self.root.title("Executed Flights")
    self.root.geometry("800x475")

    #os.system("clear")
    self.execMenu()
    #self.clearScreen()
    #Frames: Left
    self.execLeftFrame = tk.Frame(master=self.root, width=320, height=255)
    self.execLeftFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    #Frames: Left -> Connect/Disconnect Buttons
    self.execBtnFrame = tk.Frame(self.execLeftFrame)
    self.execBtnFrame.place(x=20, y=20)

    self.execExitBtn = tk.Button(
      self.execBtnFrame,
      text = "Exit",
      font = ("Times New Roman", 12),
      fg = ("royalblue4"),
      width = 8,
      command = self.root.destroy)
    
    self.execConnectBtn = tk.Button(
      self.execBtnFrame,
      text="Connect",
      font=("Times New Roman", 12),
      fg=("royalblue4"),
      width=9,
      command=self.connectDB)      
    self.execDisconnectBtn = tk.Button(self.execBtnFrame, text = "Disconnect", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 9, command = self.disconnectDB)

    self.execExitBtn.grid(row=0, column=1, padx=15)
    self.execConnectBtn.grid(row=0, column=2)

    #Frames: Right -> Middle-Right -> Data
    self.execDataFrame1 = tk.Frame(self.execLeftFrame, width=320, height=255)
    self.execDataFrame1.place(x=5, y=70)

    self.execIDLbl = tk.Label(self.execDataFrame1,
                              text="ID",
                              font=("Times New Roman", 12),
                              fg=("royalblue4"))
    self.execSchedFlightIDLbl = tk.Label(self.execDataFrame1,
                                         text="Sched. Flight ID  ",
                                         font=("Times New Roman", 12),
                                         fg=("royalblue4"))
    self.execNameLbl = tk.Label(self.execDataFrame1,
                                text="Name",
                                font=("Times New Roman", 12),
                                fg=("royalblue4"))
    self.execAirlineIDLbl = tk.Label(self.execDataFrame1,
                                     text="Airline ID",
                                     font=("Times New Roman", 12),
                                     fg=("royalblue4"))
    self.execDepFieldIDLbl = tk.Label(self.execDataFrame1,
                                      text="Dep. Field ID",
                                      font=("Times New Roman", 12),
                                      fg=("royalblue4"))
    self.execArrFieldIDLbl = tk.Label(self.execDataFrame1,
                                      text="Arr. Field ID",
                                      font=("Times New Roman", 12),
                                      fg=("royalblue4"))
    self.execFlightTypeLbl = tk.Label(self.execDataFrame1,
                                      text="Flight Type",
                                      font=("Times New Roman", 12),
                                      fg=("royalblue4"))
    self.execUpDownStatLbl = tk.Label(self.execDataFrame1,
                                      text="Up/Down",
                                      font=("Times New Roman", 12),
                                      fg=("royalblue4"))

    self.execIDDisplay = tk.Label(self.execDataFrame1,
                                  text="",
                                  font=("Times New Roman", 12),
                                  fg=("royalblue4"))
    self.execSchedFlightIDEntry = tk.Entry(self.execDataFrame1,
                                           font=("Times New Roman", 12),
                                           width=18)
    self.execNameEntry = tk.Entry(self.execDataFrame1,
                                  font=("Times New Roman", 12),
                                  width=18)
    self.execAirlineIDEntry = tk.Entry(self.execDataFrame1,
                                       font=("Times New Roman", 12),
                                       width=18)
    self.execDepFieldIDEntry = tk.Entry(self.execDataFrame1,
                                        font=("Times New Roman", 12),
                                        width=18)
    self.execArrFieldIDEntry = tk.Entry(self.execDataFrame1,
                                        font=("Times New Roman", 12),
                                        width=18)
    self.execFlightTypeEntry = ttk.Combobox(
      self.execDataFrame1,
      state='readonly',
      background=("white"),
      font=("Times New Roman", 12),
      width=17,
      values=["COMMERCIAL", "NON-COMMERCIAL"])
    self.execUpDownStatEntry = ttk.Combobox(self.execDataFrame1,
                                            state='readonly',
                                            background=("white"),
                                            font=("Times New Roman", 12),
                                            width=17,
                                            values=["Up", "Down"])

    self.execIDLbl.grid(row=0, sticky="W", pady=8)
    self.execIDDisplay.grid(row=0, column=1, sticky="W", pady=8)
    self.execSchedFlightIDLbl.grid(row=1, sticky="W", pady=8)
    self.execSchedFlightIDEntry.grid(row=1, column=1, sticky="W", pady=8)
    self.execNameLbl.grid(row=2, sticky="W", pady=8)
    self.execNameEntry.grid(row=2, column=1, sticky="W", pady=8)
    self.execAirlineIDLbl.grid(row=3, sticky="W", pady=8)
    self.execAirlineIDEntry.grid(row=3, column=1, sticky="W", pady=8)
    self.execDepFieldIDLbl.grid(row=4, sticky="W", pady=8)
    self.execDepFieldIDEntry.grid(row=4, column=1, sticky="W", pady=8)
    self.execArrFieldIDLbl.grid(row=5, sticky="W", pady=8)
    self.execArrFieldIDEntry.grid(row=5, column=1, sticky="W", pady=8)
    self.execFlightTypeLbl.grid(row=6, sticky="W", pady=8)
    self.execFlightTypeEntry.grid(row=6, column=1, sticky="W", pady=8)
    self.execUpDownStatLbl.grid(row=7, sticky="W", pady=8)
    self.execUpDownStatEntry.grid(row=7, column=1, sticky="W", pady=8)

    #Frames: Right
    self.execRightFrame = tk.Frame(self.root, width=440, height=340)
    self.execRightFrame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

    #Frames: Right -> Welcome
    self.execWelcomeLabel = tk.Label(self.root,
                                     text="Executed Flights",
                                     font=("Times New Roman", 16),
                                     fg=("royalblue4"))
    self.execWelcomeLabel.place(x=380, y=25)

    #Frames: Right -> Middle-Right
    self.execRMiddleFrame = tk.Frame(self.execRightFrame,
                                     width=450,
                                     height=380)
    self.execRMiddleFrame.place(x=0, y=10)

    #Frames: Right -> Middle-Right -> Data
    self.execDataFrame2 = tk.Frame(self.execRMiddleFrame,
                                   width=280,
                                   height=350)
    self.execDataFrame2.place(x=8, y=98)

    self.execDistanceLbl = tk.Label(self.execDataFrame2,
                                    text="Distance",
                                    font=("Times New Roman", 12),
                                    fg=("royalblue4"))
    self.execLaunchLbl = tk.Label(self.execDataFrame2,
                                  text="Launch Time",
                                  font=("Times New Roman", 12),
                                  fg=("royalblue4"))
    self.execLandLbl = tk.Label(self.execDataFrame2,
                                text="Land Time",
                                font=("Times New Roman", 12),
                                fg=("royalblue4"))
    self.execAircraftIDLbl = tk.Label(self.execDataFrame2,
                                      text="Aircraft ID",
                                      font=("Times New Roman", 12),
                                      fg=("royalblue4"))
    self.execCrewIDLbl = tk.Label(self.execDataFrame2,
                                  text="Crew ID",
                                  font=("Times New Roman", 12),
                                  fg=("royalblue4"))
    self.execPassListIDLbl = tk.Label(self.execDataFrame2,
                                      text="Pass. List ID",
                                      font=("Times New Roman", 12),
                                      fg=("royalblue4"))
    self.execFFPointsLbl = tk.Label(self.execDataFrame2,
                                    text="Freq. Flyer Pts ",
                                    font=("Times New Roman", 12),
                                    fg=("royalblue4"))

    self.execDistanceEntry = tk.Entry(self.execDataFrame2,
                                      font=("Times New Roman", 12),
                                      width=18)
    self.execLaunchEntry = tk.Entry(self.execDataFrame2,
                                    font=("Times New Roman", 12),
                                    width=18)
    self.execLandEntry = tk.Entry(self.execDataFrame2,
                                  font=("Times New Roman", 12),
                                  width=18)
    self.execPassListIDEntry = tk.Entry(self.execDataFrame2,
                                        font=("Times New Roman", 12),
                                        width=18)
    self.execAircraftIDEntry = tk.Entry(self.execDataFrame2,
                                        font=("Times New Roman", 12),
                                        width=18)
    self.execCrewIDEntry = tk.Entry(self.execDataFrame2,
                                    font=("Times New Roman", 12),
                                    width=18)
    self.execFFPointsEntry = tk.Entry(self.execDataFrame2,
                                      font=("Times New Roman", 12),
                                      width=18)

    self.execDistanceLbl.grid(row=0, sticky="W", pady=8)
    self.execDistanceEntry.grid(row=0, column=1, sticky="W", pady=8)
    self.execLaunchLbl.grid(row=1, sticky="W", pady=8)
    self.execLaunchEntry.grid(row=1, column=1, sticky="W", pady=8)
    self.execLandLbl.grid(row=2, sticky="W", pady=8)
    self.execLandEntry.grid(row=2, column=1, sticky="W", pady=8)
    self.execAircraftIDLbl.grid(row=3, sticky="W", pady=8)
    self.execAircraftIDEntry.grid(row=3, column=1, sticky="W", pady=8)
    self.execCrewIDLbl.grid(row=4, sticky="W", pady=8)
    self.execCrewIDEntry.grid(row=4, column=1, sticky="W", pady=8)
    self.execPassListIDLbl.grid(row=5, sticky="W", pady=8)
    self.execPassListIDEntry.grid(row=5, column=1, sticky="W", pady=8)
    self.execFFPointsLbl.grid(row=6, sticky="W", pady=8)
    self.execFFPointsEntry.grid(row=6, column=1, sticky="W", pady=8)

    #Frames: Right -> Middle-Right -> Clear/Add/Update/Delete Buttons
    self.execAUDBtnFrame = tk.Frame(self.execRMiddleFrame,
                                    width=200,
                                    height=240)
    self.execAUDBtnFrame.place(x=360, y=135)

    self.execAddBtn = tk.Button(self.execAUDBtnFrame,
                                text="Add",
                                font=("Times New Roman", 12),
                                fg=("royalblue4"),
                                width=5,
                                command=self.prepareNewExecutedFlight)
    self.execUpdateBtn = tk.Button(self.execAUDBtnFrame,
                                   text="Update",
                                   font=("Times New Roman", 12),
                                   fg=("royalblue4"),
                                   width=5,
                                   command=self.execUpdate)
    self.execDeleteBtn = tk.Button(self.execAUDBtnFrame,
                                   text="Delete",
                                   font=("Times New Roman", 12),
                                   fg=("royalblue4"),
                                   width=5,
                                   command=self.execDelete)
    self.execTriggerBtn = tk.Button(self.execAUDBtnFrame,
                                   text= "FF",
                                   font=("Times New Roman", 12),
                                   fg=("royalblue4"),
                                   width=5,
                                   command=self.execTrigger)
    self.execCommitAddBtn = tk.Button(self.execAUDBtnFrame, text = "Commit", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.execAddCommit)
    self.execCancelCommitBtn = tk.Button(self.execAUDBtnFrame, text = "Cancel", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 5, command = self.leaveNewExecutedInterface)
    self.execAddBtn.grid(row=1, column=0, pady=10)
    self.execUpdateBtn.grid(row=3, column=0, pady=10)
    self.execDeleteBtn.grid(row=5, column=0, pady=10)
    self.execTriggerBtn.grid(row=7, column=0, pady=10)

    #Frames: Right -> Bottom (First, Prev, Next, Last Buttons)
    self.execRBottomFrame = tk.Frame(self.root, width=700, height=80)
    self.execRBottomFrame.place(x=130, y=415)

    self.execFirstBtn = tk.Button(self.execRBottomFrame,
                                  text="First",
                                  font=("Times New Roman", 14),
                                  fg=("royalblue4"),
                                  command=self.goToStartExec) # Moses added commands to all navigation buttons
    self.execPrevious3Btn = tk.Button(self.execRBottomFrame,
                                      text="<<",
                                      font=("Times New Roman", 14),
                                      fg=("royalblue4"),
                                      command=lambda: self.moveEntryExec(-3))
    self.execPreviousBtn = tk.Button(self.execRBottomFrame,
                                     text="<",
                                     font=("Times New Roman", 14),
                                     fg=("royalblue4"),
                                     command=lambda: self.moveEntryExec(-1))
    self.execNextBtn = tk.Button(self.execRBottomFrame,
                                 text=">",
                                 font=("Times New Roman", 14),
                                 fg=("royalblue4"),
                                 command=lambda: self.moveEntryExec(1))
    self.execNext3Btn = tk.Button(self.execRBottomFrame,
                                  text=">>",
                                  font=("Times New Roman", 14),
                                  fg=("royalblue4"),
                                  command=lambda: self.moveEntryExec(3))
    self.execLastBtn = tk.Button(self.execRBottomFrame,
                                 text="Last",
                                 font=("Times New Roman", 14),
                                 fg=("royalblue4"),
                                 command=self.goToEndExec)

    self.execFirstBtn.grid(row=0, column=0, padx=15)
    self.execPrevious3Btn.grid(row=0, column=2, padx=13)
    self.execPreviousBtn.grid(row=0, column=4, padx=11)
    self.execNextBtn.grid(row=0, column=6, padx=13)
    self.execNext3Btn.grid(row=0, column=8, padx=15)
    self.execLastBtn.grid(row=0, column=10)

##### Lindsay Road Work Ends #####
