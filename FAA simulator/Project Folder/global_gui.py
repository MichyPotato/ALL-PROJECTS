# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, C       

"""
Everyone
23 March 2023
AP Computer Science Principles
Period 6
Sprint 2 Main GUI File
"""

# All TK windows should be 800 by 475 and nonresizable
# Start Moses Work
import tkinter as tk
from tkinter import ttk
from sched_flight_interface import ScheduledGUI
from exec_flight_interface import ExecutedGUI
from aircraftgui import AirCraftGUI
from crew_gui import CrewGUI
from airport_gui import AirTravelGUI
from airline_gui import AirlineGUI
from passengerslistsGui import PassengersListsGUI
from passengersGui import PassengersGUI
from pilot_fa_gui import PilotGUI
from pilot_fa_gui import FAttGUI

import PIL
from PIL import ImageTk, Image

class GlobalGUI():
  #Initiate
  def __init__(self):
    self.mainWindow()
    self.mainMenu()
    self.mainFrame() 
    self.root.mainloop()
    self.currentWindow = 0
  
  #About popup window
  def aboutPopup(self):
    tk.messagebox.showinfo(title = "About", message = "Home GUI")

  #Moses Work Ends
  
  ### Lindsay's Work Begins ###
  
  #Clear Main Screen
  def clearScreen(self):
    self.wLeftFrame.destroy()
    self.wRightFrame.destroy()
      
  ##### GUI Windows #####
  
  # Start Moses Work
  #Check Main Screen's Dropdown and Open Up New Windows
  def checkDropdown(self):
    checkDone = False
    while checkDone == False:
      if (self.tblDropdown.get() == "Scheduled Flights"):
        self.currentWindow = ScheduledGUI()
        checkDone = True
      elif (self.tblDropdown.get() == "Executed Flights"):
        self.currentWindow = ExecutedGUI()
        checkDone = True
      elif (self.tblDropdown.get() == "Aircrafts"):
        self.currentWindow = AirCraftGUI()
        self.currentWindow.buildWindow()
        checkDone = True
      elif (self.tblDropdown.get() == "Airports"):
        self.currentWindow = AirTravelGUI()
        self.currentWindow.buildWindow()
        checkDone = True
      elif (self.tblDropdown.get() == "Airlines"):
        self.currentWindow = AirlineGUI()
        checkDone = True
      elif (self.tblDropdown.get() == "Crews"):
        self.currentWindow = CrewGUI()
        checkDone = True
      elif (self.tblDropdown.get() == "Pilots"):
        self.currentWindow = PilotGUI()
        checkDone = True
      elif (self.tblDropdown.get() == "Flight Attendants"):#Done but not in the right way
        self.currentWindow = FAttGUI()
        checkDone = True
      elif (self.tblDropdown.get() == "Passengers"):
        self.currentWindow = PassengersGUI()
        checkDone = True
      elif (self.tblDropdown.get() == "Passenger Groups"):
        self.currentWindow = PassengersListsGUI()
        checkDone = True
   
  #Main Window  
  def mainWindow(self):
    #Window
    self.root = tk.Tk()
    self.root.title("Flight Tracking System")
    self.root.geometry("800x475")
    self.root.resizable(False, False)
  
  # End Moses Work
    
  #Main tk.Menu  
  def mainMenu(self):  
    #tk.Menu
    self.menubar = tk.Menu(self.root)
    self.root.config(menu = self.menubar)    
    #tk.Menu: File
    self.fileMenu = tk.Menu(self.menubar, tearoff = 0)
    self.fileMenu.add_command(label = "Exit", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.root.destroy)
    self.menubar.add_cascade(label = "File", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.fileMenu)
    
    #tk.Menu: Tables
    # self.mMenu = tk.Menu(self.menubar, tearoff = 0)
    # self.mMenu.add_command(label = "Scheduled", font = ("Times New Roman", 12), foreground = ("royalblue4"))#, command = self.schedWindow)
    # self.mMenu.add_command(label = "Executed", font = ("Times New Roman", 12), foreground = ("royalblue4"))#, command = self.execWindow)
    # self.menubar.add_cascade(label = "Flights", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.mMenu)
    
    #tk.Menu: Help
    self.helpMenu = tk.Menu(self.menubar, tearoff = 0)
    self.helpMenu.add_command(label = "About", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.aboutPopup)
    self.menubar.add_cascade(label = "Help", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.helpMenu)

  #Main Frame
  def mainFrame(self):
    #Welcome Frames: Left
    self.wLeftFrame = tk.Frame(master = self.root, width = 420, height = 380)
    self.wLeftFrame.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
    
    #Welcome Frames: Right
    self.wRightFrame = tk.Frame(self.root, width = 385, height = 380)
    self.wRightFrame.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
    
    #Welcome Frames: Right -> Welcome Frame/Label
    self.wWelcomeFrame = tk.Frame(self.wRightFrame, width = 385, height = 130) 
    self.wWelcomeFrame.place(x = 0, y = 75)
    
    #Welcome Frames: Right -> Choose Frame
    self.wChooseFrame = tk.Frame(self.wRightFrame, height = 400)
    self.wChooseFrame.place(x = 20, y = 195)

    #Welcome Frames: Left -> Picture - fixed by Kingsley
    self.plane_pic = Image.open("Project Folder/planepic.png")
    self.plane_pic = self.plane_pic.resize((300, 300), Image.LANCZOS)
    self.wPic = ImageTk.PhotoImage(self.plane_pic)
    self.wMyPic = tk.Label(self.wLeftFrame, image=self.wPic)
    self.wMyPic.place(x = 50, y = 150)
  
    #Welcome Label
    self.wWelcomeLabel = tk.Label(self.wWelcomeFrame, text = "Welcome to Your\nFlight Tracking System", font = ("Times New Roman", 18), fg = ("royalblue4"))
    self.wWelcomeLabel.place(x = 2, y = 32)

    #Choosing Label
    self.chooseLabel = tk.Label(self.wChooseFrame, text = "Please choose which table\nyou would like to connect to.", font = ("Times New Roman", 13), fg = ("royalblue4"))
    self.chooseLabel.grid(row = 0, column = 0)

    #Pick Table
    self.tblDropdown = ttk.Combobox(self.root, state = 'readonly', foreground = "royalblue4", font = ("Times New Roman", 14), width = 15
    , values = ["Scheduled Flights", "Executed Flights", "Aircrafts", "Airports", "Airlines", "Crews", "Pilots", "Flight Attendants", "Passenger Groups", "Passengers"])
    self.tblDropdown.current(0)
    self.tblDropdown.place(x = 450, y = 265)
    self.goBtn = tk.Button(self.root, text = "Go", font = ("Times New Roman", 12), fg = ("royalblue4"), command = self.checkDropdown)
    self.goBtn.place(x = 620, y = 260)
      
