# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
"""
Pranavi Kuravi, Mariana Vega, Samantha Forero
TK AirCraftGUI POCO 
"""


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time

from database_aircraft import Database
from aircraft import Aircraft

# Air travel GUI POCO

#Pranavi
class AirCraftGUI:

    def __init__(self):
    

        # POCO Instance variables

        # create a main window which will have other widgets such as Labels etc
        self.rootWindow = Tk()

        # Holds the DB connection to DB - Database POCO
        self.dbConn = None

        # List container for holding aiport objects - aircraft POCO
        self.aircraftList = None

        # Holds the index reference to current aircraft poco from aircraftList
        self.currentIndex = -1

        # holds Canvas object for placing various GUI widgets
        self.winCanvas = None

        # Holds reference to background image and icon images
        self.bgImage = None
        self.iconImage = None

        # Textbox entry fields for id, aircraft type, BUNO
        # for capturing aircraft details. Initializing them to None for later instantiation
        self.idBox = None
        self.aircraftTypeBox = None
        self.bunoBox = None
        

        # Navigation button references for enabling and disabling depending on the total available records
        self.firstButton = None
        self.prevButton = None
        self.nextButton = None
        self.lastButton = None
        self.prevThreeButton = None
        self.nextThreeButton = None

        # Holds the reference to Status Text Id for updating the status messages for various user actions
        self.statusTextId = None

        # Holds references to Tags of various GUI widgets. This helps in hiding/displaying group of widgets
        self.aircraftFieldTags = "aircraftFields"
        self.aircraftInputFieldTags = "aircraftInputFields"
        self.navigationAndCrudFields = "navigationAndCrudFields"
        self.initialFieldTags = "initialFieldTags"
        self.submitCancelTags = "submitCancelTags"

    # build the root window and add buttons and labels inside the window

    #Pranavi
    def buildWindow(self):

        # set the window title
        self.rootWindow.title("Air Travel Reservation System")
        # set the size of the window and display it at (600, 200) location
        self.rootWindow.geometry("800x475")

        # Don't let user resize the window
        self.rootWindow.resizable(False, False)

        # Seting the application Icon.
        # *** This does not work in Mac OS but works in Windows OS ***
        #self.rootWindow.iconbitmap(".ico")

        # Build the various menu items as part of App menu
        self.buildAppMenu()

        # First build Canvas widget with background Image.
        # Other widets like text boxes, buttons are placed inside the Canvas
        self.buildCanvasWithBackgroundImage()

        # Build aircraft detail Text boxes and labels such as First Name, Last Name, Age etc
        self.buildAircraftDetailsFields()

        # Build navigation buttons for fetching first, prev, next and last records from the database
        self.buildNavigationButtons()

        # Build buttons for Editing, Deleting, Creating aircrafts
        self.buildCrudButtons()

        # show only load from DB button during initial load
        self.showInitialFieldsOnly()

        # This loop will keep the window from closing
        self.rootWindow.mainloop()

    #Mariana
    # This method builds the Menu items - File, Tools and Help and About Item under App menu
    def buildAppMenu(self):

        # Builds the About menu item under App menu
        menuBar = Menu(self.rootWindow)
        appMenu = Menu(menuBar, name='apple')
        menuBar.add_cascade(menu=appMenu)
        appMenu.add_command(label="About the Air Travel Reservation App",
                            command=self.showAboutTheAppDialog)
        self.rootWindow.config(menu=menuBar)

        # Builds the File Menu with Close App, quote of the day items in it
        fileMenu = Menu(menuBar, tearoff=False)
        fileMenu.add_command(label="Fun fact about airlines",
                             command=self.showFunFact)
        fileMenu.add_command(label="Close App", command=self.closeTheApp)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Builds the Tools menu with Connect and Disconnect from DB items in it
        dbMenu = Menu(menuBar, tearoff=False)
        dbMenu.add_command(label="Connect To Database",
                           command=self.connectToDatabase)
        dbMenu.add_command(label="Disconnect From Database",
                           command=self.disconnectFromDatabase)
        menuBar.add_cascade(label="Tools", menu=dbMenu)
        #dbMenu.entryconfigure(1, state=DISABLED)

        # Builds Help menu with Contact item in it
        helpMenu = Menu(menuBar, tearoff=False)
        helpMenu.add_command(label="Contact", command=self.showContactDialog)
        menuBar.add_cascade(label="Help", menu=helpMenu)

    #Mariana
    # This method builds the Canvas widget along with background Image
    # Other widgets such as text boxes, Labels, Buttons are placed inside this canvas.
    def buildCanvasWithBackgroundImage(self):

        # Create Canvas
        self.winCanvas = Canvas(self.rootWindow, width=640, height=480)
        self.winCanvas.pack(fill="both", expand=True)

        # Add background image
        self.bgImage = PhotoImage(file="Project Folder/airplane.png")
        # add Image to canvas
        self.winCanvas.create_image(20, 130, image=self.bgImage, anchor="nw")

    #Pranavi
    # This method builds aircraft Fields and adds it to Canvas
    def buildAircraftDetailsFields(self):

        # Title
        self.winCanvas.create_text(
            320, 30, text="Aircraft Details", fill="black", font="TkDefaultFont 25")

        # Add application icon image to the right of Title
        #self.iconImage = PhotoImage(file="cartoon-airplane.png")
        #self.winCanvas.create_image(30, 5, image=self.iconImage, anchor="nw")

        # Adding Id, Aircraft type, BUNO Labels to Canvas at specified locations with Tags.
        # Tags are useful for hiding and displaying these fields as a group
        self.winCanvas.create_text(400, 100, text="Id", fill="Black",
                                   font="TkDefaultFont 15", tags=self.aircraftFieldTags)
        self.winCanvas.create_text(400, 175, text="Aircraft type", fill="Black",
                                   font="TkDefaultFont 15", tags=self.aircraftFieldTags)
        self.winCanvas.create_text(400, 250, text="BUNO", fill="Black",
                                   font="TkDefaultFont 15", tags=self.aircraftFieldTags)

        # creating Text boxes for the the above labels
        self.idBox = Entry(self.rootWindow, width=5, borderwidth=2)
        self.aircraftTypeBox = Entry(self.rootWindow, width=15, borderwidth=2)
        self.bunoBox = Entry(self.rootWindow, width=15, borderwidth=2)

        # Adding Id, Aircraft type, BUNO Text entry boxes to Canvas at specified locations with Tags
        self.winCanvas.create_window(400, 130, window=self.idBox, tags=[
                                     self.aircraftFieldTags, self.aircraftInputFieldTags])
        self.winCanvas.create_window(400, 200, window=self.aircraftTypeBox, tags=[
                                     self.aircraftFieldTags, self.aircraftInputFieldTags])
        self.winCanvas.create_window(400, 285, window=self.bunoBox, tags=[
                                     self.aircraftFieldTags, self.aircraftInputFieldTags])

        # submit and cancel buttons are displayed when adding/editing a record
        # command action calls the mentioned method in response to button click event
        submitButton = Button(self.rootWindow, text="Submit",
                              width=5, command=self.saveAircraftInfoToDB)
        cancelButton = Button(self.rootWindow, text="Cancel",
                              width=5, command=self.cancelChanges)

        # Hide the submit/cancel buttons initially. These buttons will be shown only during Adding/Editing records
        self.winCanvas.create_window(
            700, 175, window=submitButton, state=HIDDEN, tags=self.submitCancelTags)
        self.winCanvas.create_window(
            700, 250, window=cancelButton, state=HIDDEN, tags=self.submitCancelTags)

    #Samantha
    # This method builds Navigation buttons first, prev, next and last buttons
    def buildNavigationButtons(self):

        # Adding Navigation label at specified location
        self.winCanvas.create_text(350, 350, text="Navigation", fill="Black", font="TkDefaultFont 15", tags=[
                                   self.aircraftFieldTags, self.navigationAndCrudFields])

        # creating four buttons - first, prev, next and last
        self.firstButton = Button(
            self.rootWindow, text="|<", width=2, command=self.loadFirstRecord)
        self.prevButton = Button(
            self.rootWindow, text="<", width=2, command=self.loadPrevRecord)
        self.nextButton = Button(
            self.rootWindow, text=">", width=2, command=self.loadNextRecord)
        self.prevThreeButton = Button(
            self.rootWindow, text="<<", width=2, command=self.loadThreeLastRecord)
        self.nextThreeButton = Button(
            self.rootWindow, text=">>", width=2, command=self.loadThreeNextRecord)
        self.lastButton = Button(
            self.rootWindow, text=">|", width=2, command=self.loadLastRecord)

        # Adding the first, prev, next and last buttons to Canvas at specified locations
        self.winCanvas.create_window(325, 390, window=self.firstButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
        self.winCanvas.create_window(475, 390, window=self.prevButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
        self.winCanvas.create_window(550, 390, window=self.nextButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
        self.winCanvas.create_window(700, 390, window=self.lastButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
        self.winCanvas.create_window(400, 390, window=self.prevThreeButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
        self.winCanvas.create_window(625, 390, window=self.nextThreeButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
    
    #Samantha
    # This method builds Edit, Delete and Create Buttons
    def buildCrudButtons(self):

        # creating three buttons - edit, delete and add buttons for create, update and delete operations on aircraft POCO objects
        editButton = Button(self.rootWindow, text="Edit Aircraft",
                            width=10, command=self.editAircraftFields)
        deleteButton = Button(self.rootWindow, text="Delete Aircraft",
                              width=10, command=self.deleteAircraft)
        addButton = Button(self.rootWindow, text="Add Aircraft",
                           width=10, command=self.addAircraftRecord)

        # Adding edit, delete, add buttons to Canvas at specified locations
        self.winCanvas.create_window(700, 100, window=editButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
        self.winCanvas.create_window(700, 175, window=deleteButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])
        self.winCanvas.create_window(700, 250, window=addButton, tags=[
                                     self.aircraftFieldTags, self.navigationAndCrudFields])

        # Button for loading records from database. This button shows during inital load of the screen
        loadFromDbButton = Button(
            self.rootWindow, text="Load From DB", width=10, command=self.connectToDatabase)
        self.winCanvas.create_window(
            300, 80, window=loadFromDbButton, tags=self.initialFieldTags)

        # Adding Status label at specified location
        self.statusTextId = self.winCanvas.create_text(
            320, 420, text="", fill="Black", font="TkDefaultFont 15")

    #Pranavi
    # This method hides and displays relevant UI fields during initial load of the app as well as when disconnected from DB
    def showInitialFieldsOnly(self):
        self.winCanvas.itemconfigure(
            self.aircraftFieldTags, state="hidden")
        self.winCanvas.itemconfigure(self.initialFieldTags, state="normal")
        self.winCanvas.itemconfigure(
            self.statusTextId, text="Disconnected from Database")

    # This method hides and displays relevant UI fields when records are loaded from DB
    def showAircraftFieldsOnly(self):
        self.winCanvas.itemconfigure(
            self.aircraftFieldTags, state="normal")
        self.winCanvas.itemconfigure(self.initialFieldTags, state="hidden")

    # This method sets the state of the navigation and crud buttons
    # desiredState parameter can be hidden or normal
    def changeStateOfNavigationAndCrudFields(self, desiredState):
        self.winCanvas.itemconfigure(
            self.navigationAndCrudFields, state=desiredState)

    #Samantha
    # This method loads the data from DB
    def connectToDatabase(self):

        # Connecting to airline.db
        self.dbConn = Database()
        print("Connected to Database")
        self.showStatusMessage("Connected to Database")

        # delay loading again from DB by 200 milli seconds so status message can be seen by user
        self.rootWindow.after(200, self.loadAircraftsFromDb)

        self.showAircraftFieldsOnly()

    # This method helps in disconnecting from DB and restoring the window state to initial stage
    def disconnectFromDatabase(self):

        if self.dbConn is not None:
            self.dbConn.closeDbConnection()

        print("disconnected from Database")
        self.resetInstanceFieldsToInitalState()
        self.showInitialFieldsOnly()
        self.showStatusMessage("Disconnected from Database")

    # This method displays status message for various user actions
    def showStatusMessage(self, message, fill="black"):
        self.winCanvas.itemconfigure(
            self.statusTextId, text=message, fill=fill)

    # This method fetches aircraft from sqlite DB and populates UI with details
    def loadAircraftsFromDb(self):

        self.aircraftList = self.dbConn.getAllAircrafts()

        for record in self.aircraftList:
            print(record.getAircraftDetails())

        if len(self.aircraftList) > 0:
            self.currentIndex = 0
        else:
            self.currentIndex = -1

        self.populateGuiWithAircraftDetails()

    #Pranavi
    # This method loads the previous record and gets called when prev button is clicked
    def loadPrevRecord(self):

        self.currentIndex = self.currentIndex - 1
        self.populateGuiWithAircraftDetails()

    # This method loads the first record and gets called when first button is clicked
    def loadFirstRecord(self):

        self.currentIndex = 0
        self.populateGuiWithAircraftDetails()

    # This method loads the next record and gets called when next button is clicked
    def loadNextRecord(self):

        self.currentIndex = self.currentIndex + 1
        self.populateGuiWithAircraftDetails()

    # This method loads the last record and gets called when last button is clicked
    def loadLastRecord(self):

        self.currentIndex = len(self.aircraftList) - 1
        self.populateGuiWithAircraftDetails()
    
    def loadThreeNextRecord(self):

        self.currentIndex = self.currentIndex + 3
        self.populateGuiWithAircraftDetails()

    # This method loads the last record and gets called when last button is clicked
    def loadThreeLastRecord(self):

        self.currentIndex = len(self.aircraftList) - 3
        self.populateGuiWithAircraftDetails()

    # This method populates the UI fields with Aircraft details
    # And also sets the state of text boxes to readonly state. This is for allowing to just read and not edit
    # Updates the status message to reflect the record totals and current item
    def populateGuiWithAircraftDetails(self):

        self.changeStateOfAircraftInputFields("normal")
        self.resetGuiTextFields()

        if self.currentIndex >= 0:
            aircraft = self.aircraftList[self.currentIndex]
            self.idBox.insert(0, aircraft.getId())
            self.aircraftTypeBox.insert(0, aircraft.getAircraftType())
            self.bunoBox.insert(0, aircraft.getBuno())


        self.changeStateOfAircraftInputFields("readonly")

        statusMessage = "Record {0} of {1}".format(
            (self.currentIndex+1), len(self.aircraftList))
        self.showStatusMessage(statusMessage)
        self.enableDisableNavigationButtons()

    # This method resets the UI fields to initial state
    def resetInstanceFieldsToInitalState(self):
        self.currentIndex = -1
        self.resetGuiTextFields()

    # This method clears the data from the input text boxes
    def resetGuiTextFields(self):

        self.idBox.delete(0, END)
        self.aircraftTypeBox.delete(0, END)
        self.bunoBox.delete(0, END)

    # This method would let the user edit the details
    # It changes the text boxes to be editable state except Id field since it is primary key
    def editAircraftFields(self):

        self.changeStateOfAircraftInputFields("normal")
        self.idBox.configure(state="disabled")
        self.changeSubmitCancelButtonState("normal")
        self.changeStateOfNavigationAndCrudFields("hidden")

    # This method allows for adding new record into DB.
    # Id field editing not allowed as it is auto incremented primary key
    def addAircraftRecord(self):

        self.changeStateOfAircraftInputFields("normal")
        self.resetGuiTextFields()
        self.idBox.configure(state="disabled")
        self.changeSubmitCancelButtonState("normal")
        self.changeStateOfNavigationAndCrudFields("hidden")
        self.showStatusMessage(message="")

    # This method allows for deleting a record. First it asks for confirmation before deleting
    def deleteAircraft(self):

        shouldDelete = messagebox.askyesno(title="confirm delete",
                                           message="Are you sure you want to delete?",
                                           )
        # Don't delete if usedr says no
        if shouldDelete is not True:
            return

        id = int(self.idBox.get())
        self.dbConn.deleteAircraft(id)

        self.showStatusMessage("Deleted succesfully from database")

        # delay by 1000 milli seconds
        self.rootWindow.after(1000, self.loadAircraftsFromDb)

    # This method sets the text box states and useful when editing/adding/reading
    # desired states are normal and readonly
    def changeStateOfAircraftInputFields(self, desiredState):

        self.idBox.configure(state=desiredState)
        self.aircraftTypeBox.configure(state=desiredState)
        self.bunoBox.configure(state=desiredState)

    # This method first validates the data before saving it to DB
    def saveAircraftInfoToDB(self):

        # Do not save if validation fails
        if self.validateFieldsBeforeSaving() is not True:
            return

        aircraft = self.createAircraftObjectFromInput()

        if aircraft.id == None:
            self.dbConn.addAircraft(aircraft)
        else:
            self.dbConn.updateAircraft(aircraft)

        self.showStatusMessage("saved succesfully to database")

        # delay by 1000 milli seconds
        self.rootWindow.after(1000, self.loadAircraftsFromDb)
        self.changeStateOfAircraftInputFields("readonly")
        self.changeSubmitCancelButtonState("hidden")
        self.changeStateOfNavigationAndCrudFields("normal")

    # This method allows for canceling and returning back to reading records
    def cancelChanges(self):

        self.loadAircraftsFromDb()
        self.changeStateOfAircraftInputFields("readonly")
        self.changeSubmitCancelButtonState("hidden")
        self.changeStateOfNavigationAndCrudFields("normal")

    # This method changes the state of Submit/Cancel buttons
    # desiredState can be normal/hidden
    def changeSubmitCancelButtonState(self, desiredState):
        self.winCanvas.itemconfigure(self.submitCancelTags, state=desiredState)

    # This method creates Aircraft poco object from input text boxes
    def createAircraftObjectFromInput(self):

        id = None
        if self.idBox.get() != "":
            id = int(self.idBox.get())

        aircraftType = self.aircraftTypeBox.get()
        buno = self.bunoBox.get()

        aircraft = Aircraft(aircraftType=aircraftType, buno=buno, id=id)

        return aircraft

    # This method enables/disables navigation buttons based on index position pointer to aircraftList records
    def enableDisableNavigationButtons(self):

        if self.currentIndex <= 0:
            self.prevButton.configure(state=DISABLED)
            self.firstButton.configure(state=DISABLED)
        else:
            self.prevButton.configure(state=NORMAL)
            self.firstButton.configure(state=NORMAL)

        if self.currentIndex >= len(self.aircraftList) - 1:
            self.nextButton.configure(state=DISABLED)
            self.lastButton.configure(state=DISABLED)
        else:
            self.nextButton.configure(state=NORMAL)
            self.lastButton.configure(state=NORMAL)

        if self.currentIndex >= len(self.aircraftList) - 3:
            self.nextThreeButton.configure(state=DISABLED)
            self.prevThreeButton.configure(state=NORMAL)
        else:
            self.nextThreeButton.configure(state=NORMAL)
            self.prevThreeButton.configure(state=DISABLED)

        

    # This method displays the About popup window to display general info reg. the app
    # Called when about menu item is clicked
    def showAboutTheAppDialog(self):

        messagebox.showinfo(title="About Airline Reservation app",
                            message="Aircraft Listing",
                            detail="This app allows you to save aircraft details",
                            icon=messagebox.INFO)

    # This method displays the contact details popup window.
    # Called when clicking on contact details from menu
    def showContactDialog(self):

        messagebox.showinfo(title="Contact Details",
                            message="Pranavi Kuravi",
                            detail="Please contact me at JCHS during school hours for help",
                            icon=messagebox.INFO)

    # This method first closes the database connections and then exit the app
    def closeTheApp(self):

        if self.dbConn is not None:
            self.dbConn.closeDbConnection()

        self.rootWindow.quit()

    def showFunFact(self):
        self.showStatusMessage(
            "The plane’s bathroom can be unlocked from the outside")
            

    # This method validates various input fields and returns True if all fields are entered and are valid else False
    def validateFieldsBeforeSaving(self):

        if self.checkIfInputIsEmpty(self.aircraftTypeBox.get(), "Aircraft type"):
            return False
        elif self.checkIfInputIsEmpty(self.bunoBox.get(), "BUNO"):
            return False

        return True

    # This method checks if entered input is empty. If so, returns True
    def checkIfInputIsEmpty(self, value, fieldName):

        if value != "":
            return False

        self.showStatusMessage("Please enter " + fieldName, fill="cyan")

        return True
