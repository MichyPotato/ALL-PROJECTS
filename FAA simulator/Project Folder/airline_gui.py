# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
from tkinter import *
import tkinter as tk
from tkinter import Menu
from PIL import ImageTk, Image
from global_database import GlobalDb

class AirlineGUI:
  #init
  def __init__(self):
    self.db = GlobalDb()
    self.conn = False  
    self.eNumber = 1  
    self.aNumber = [] 
    self.Window()
    self.Menu()
    self.root.mainloop()

  #Connect
  def connect(self):
    if (self.conn == False):
      connectionResult = self.db.createConnection()
      if (connectionResult == 1):
        self.conn = False
      else:
        print("Connected")
        self.conn = True

  #Disconnect
  def disconnect(self):
    if (self.conn == True):
      connectionResult = self.db.breakConnection()
      if (connectionResult == 1):
        self.conn = True
      else:
        print("Disconnected")
        self.conn = False

  # Navigation Methods
  def fetch_first(self):
    self.selected_airline = self.db.fetch_first(1)
    self.populate_airlineSpecs(self.selected_airline)
  def fetch_last(self):
    self.eNumber = 5
    self.selected_airline = self.db.fetch_last(self.eNumber)
    self.populate_airlineSpecs(self.selected_airline)
  def next(self):
    self.eNumber += 1
    self.selected_airline = self.db.next(self.eNumber)
    self.populate_airlineSpecs(self.selected_airline)
  def next2(self):
    self.eNumber += 2
    self.selected_airline = self.db.next2(self.eNumber)
    self.populate_airlineSpecs(self.selected_airline)
  def prev(self):
    self.eNumber -= 1
    self.selected_airline = self.db.prev(self.eNumber)
    self.populate_airlineSpecs(self.selected_airline)
  def prev2(self):
    self.eNumber -= 2
    self.selected_airline = self.db.prev2(self.eNumber)
    self.populate_airlineSpecs(self.selected_airline)


  def populate_airlineSpecs(self, selected_airline):
    print("selected airline", self.selected_airline)
    self.idEntry.delete(0, END)
    self.idEntry.insert(END, self.selected_airline[0])
    self.nameEntry.delete(0, END)
    self.nameEntry.insert(END, self.selected_airline[1])
    self.einEntry.delete(0, END)
    self.einEntry.insert(END, self.selected_airline[2])



  
  #Clear fields 
  def clearFields(self):
    self.idEntry.delete(0, 'end')
    self.nameEntry.delete(0, 'end')
    self.einEntry.delete(0, 'end')
    
  #Insert
  def insert(self):
    if (self.conn == False):
      print("Connect to the database.")
    else:
      id = self.idEntry.get()
      name = self.nameEntry.get()
      ein = self.einEntry.get()
      
      self.db.insert(id, ein, name)

  #Delete
  def delete(self):
    if (self.conn == False):
      print("Connect to the database.")
    else:
      self.db.delete(self.idEntry.get())
    
  def update(self):
    if (self.conn == False):
      print("Connect to the database.")
    else:
      id = self.idEntry.get()
      name = self.nameEntry.get()
      ein = self.einEntry.get()
      self.db.update(ein, name, id)


  
  #Menu
  def Menu(self):
    self.Menubar = Menu(self.root)
    self.root.config(menu = self.Menubar)
    #File
    self.FileMenu = Menu(self.Menubar, tearoff = 0)   
    self.FileMenu.add_command(label = "Connect", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.connect)
    self.FileMenu.add_command(label = "Disconnect", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.disconnect)    
    self.FileMenu.add_command(label = "Exit", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.root.destroy)
    self.Menubar.add_cascade(label = "File", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.FileMenu)

    #Update
    self.EditMenu = Menu(self.Menubar, tearoff = 0)  
    self.EditMenu.add_command(label = "Insert", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.EditMenu.add_command(label = "Update", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.EditMenu.add_command(label = "Delete", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.Menubar.add_cascade(label = "Edit", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.EditMenu)
    
    #Navigate
    self.NavMenu = Menu(self.Menubar, tearoff = 0)    
    self.NavMenu.add_command(label = "First", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.fetch_first) 
    self.NavMenu.add_command(label = "2nd Previous", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.prev2)
    self.NavMenu.add_command(label = "Previous", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.prev)
    self.NavMenu.add_command(label = "Next", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.next)
    self.NavMenu.add_command(label = "2nd Next", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.next2)
    self.NavMenu.add_command(label = "Last", font = ("Times New Roman", 12), foreground = ("royalblue4"), command = self.fetch_last)
    self.Menubar.add_cascade(label = "Navigate", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.NavMenu)
    
    #Help
    self.HelpMenu = Menu(self.Menubar, tearoff = 0)
    self.HelpMenu.add_command(label = "About", font = ("Times New Roman", 12), foreground = ("royalblue4"))
    self.Menubar.add_cascade(label = "Help", font = ("Times New Roman", 12), foreground = ("royalblue4"), menu = self.HelpMenu)
    
  #Window
  def Window(self):
    self.root = tk.Tk()
    self.root.title("Airlines")
    self.root.geometry("800x475")
  
    self.Menu()
    #Left
    self.lFrame = tk.Frame(master = self.root, width = 320, height = 235)
    self.lFrame.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
  
    self.btnFrame = tk.Frame(self.lFrame)
    self.btnFrame.place(x = 20, y = 20)

    self.exitBtn = tk.Button(self.btnFrame, text = "Exit", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 8, command = self.root.destroy)
    self.connectBtn = tk.Button(self.btnFrame, text = "Connect", font = ("Times New Roman", 12), fg = ("royalblue4"), width = 9, command = self.connect) 
    
    self.exitBtn.grid(row = 0, column = 1, padx = 15)
    self.connectBtn.grid(row = 0, column = 2)

    #Right
    self.rFrame = tk.Frame(self.root, width = 450, height = 310)
    self.rFrame.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
  
    #Name
    self.nameLabel = tk.Label(self.root, text = "Airlines", font = ("Times New Roman", 16), fg = ("royalblue4"))
    self.nameLabel.place(x = 360, y = 25)
  
    self.rrFrame = tk.Frame(self.rFrame, width = 450, height = 330)
    self.rrFrame.place(x = 0, y = 10)

    self.dFrame = tk.Frame(self.rrFrame, width = 280, height = 510)
    self.dFrame.place(x = 8, y = 68)
  
    self.idLBL = tk.Label(self.dFrame, text = "ID", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.nameLBL = tk.Label(self.dFrame, text = "Airline Name", font = ("Times New Roman", 12), fg = ("royalblue4"))
    self.einLBL = tk.Label(self.dFrame, text = "EIN", font = ("Times New Roman", 12), fg = ("royalblue4"))
  
    self.idEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    self.nameEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    self.einEntry = tk.Entry(self.dFrame, font = ("Times New Roman", 12), width = 19)
    
    self.idLBL.grid(row = 0, sticky = "W", pady = 10)
    self.idEntry.grid(row = 0, column = 1, sticky = "W", pady = 10)
    self.nameLBL.grid(row = 1, sticky = "W", pady = 10)
    self.nameEntry.grid(row = 1, column = 1, sticky = "W", pady = 10)
    self.einLBL.grid(row = 2, sticky = "W", pady = 10)
    self.einEntry.grid(row = 2, column = 1, sticky = "W", pady = 10)
  
      
    #CRUD buttons
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
  
    #NAV buttons
    self.navFrame = tk.Frame(self.root, width = 700, height = 80)
    self.navFrame.place(x = 130, y = 385)
  
    self.firstBtn = tk.Button(self.navFrame, text = "<<|", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.fetch_first) 
    self.prev2Btn = tk.Button(self.navFrame, text = "<<", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.prev2)
    self.prevBtn = tk.Button(self.navFrame, text = "<", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.prev)
    self.nextBtn = tk.Button(self.navFrame, text = ">", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.next)
    self.next2Btn = tk.Button(self.navFrame, text = ">>", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.next2)
    self.lastBtn = tk.Button(self.navFrame, text = "|>>", font = ("Times New Roman", 14), fg = ("royalblue4"), command = self.fetch_last)
  
    self.firstBtn.grid(row = 0, column = 0, padx = 15)
    self.prev2Btn.grid(row = 0, column = 2, padx = 13)
    self.prevBtn.grid(row = 0, column = 4, padx = 11)
    self.nextBtn.grid(row = 0, column = 6, padx = 13)
    self.next2Btn.grid(row = 0, column = 8, padx = 15)
    self.lastBtn.grid(row = 0, column = 10)