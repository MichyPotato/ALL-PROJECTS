# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C       
# DO NOT delete this file

"""
Everyone
23 March 2023
AP Computer Science Principles
Period 6
Sprint 2 Global Database File
"""

# Everyone Should Mark Their Own Work

# Instructions #

# All Groups Need To Put Their Database Code Here 
# Replace all cursor names with self.cursor
# Replace all connection names with self.connection
# Remove all connect/disconnect methods from your group's code

#
#
# MAKE SURE TO CHECK DISCORD
#
#

import os,sys
import mysql.connector
from airport import Airport 
from aircraft import Aircraft
#Michelle fixed all class indenting problems hopefully. changed 10 problems :D
class GlobalDb():
  # For those working inside of __init__ , make sure that your names do not conflict with other tables
  def __init__(self):
    self.connect = False #Lindsay
    self.schedId = 0 #Lindsay
    self.execId = 0 #Lindsay

    # Database
    self.p_records = []
    self.p_record = []
    self.plist_records = []
    self.plist_record = []
    self.p_insertRec=["","",0,"","",""]
    self.p_updateRec=[0,"","",0,"","",""]
    self.plist_insertRec = [0,"",0,"",0,"",0,"",0,""]
    self.plist_updateRec = [0,0,"",0,"",0,"",0,"",0,""]

    # Airline
    self.recNum = 0 #for airline
    
    #Flight Attendants
    self.attendants = []
    self.insert_fa = ["","",0,"",]
    self.update_fa = [0,"","",0,""]

    # Pilots
    self.pilots = []
    self.insert_pi = ["","","","","",""]
    self.update_pi = [0, "", "", "", "","",""]

  # Moses: Create Connection With The Database
  def createConnection(self):
    # Deploy: At School Only
    # try:
    #   self.connection = mysql.connector.connect(
    #     host = "192.168.0.116",
    #     port = 3306,
    #     user = "vader",
    #     password = "jchs",
    #     database = "Airline_Period_6"
    #   )
    #   self.cursor = self.connection.cursor()
    # except:
    #   print("Create Connection Error")
    #   return 1
    
    # Testing: At Home Only 
    # If anybody needs to use this, make sure that you put in proper information for YOUR local device
    if (self.getConnect() == False): #Lindsay
      try:
        self.connection = mysql.connector.connect(
          host = "localhost",
          port = 3306, #(the default port is 3306)
          user = "root",
          password = "!@#seojean_and_sam90",
          database = "airlines"
        )
        # Establish the cursor used to execute later queries based on the connection above.
        self.cursor = self.connection.cursor()
        self.setConnect(True)	
        #Lindsay's Work Begins
        self.cursor.execute("SELECT * FROM scheduled_flights ORDER BY id_sched_flight ASC;")
        schedResult = self.cursor.fetchone()
        self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM executed_flights ORDER BY id_exec_flight ASC;")
        execResult = self.cursor.fetchone()
        self.cursor.fetchall()
        if schedResult is not None:
            self.setSchedId(schedResult[0])
        if execResult is not None:
            self.setExecId(execResult[0])
      #If connection fails, return error
        #return schedResult
        #Lindsay's Work Ends
      # If connection fails, return error
      except:
        print("Create Connection Error")
        return 1  
      # Return 0 if no errors occur
      return 0
    
  # Moses: Break Connection With The Database
  def breakConnection(self):
    #try to break the connection and the cursor off
    if (self.getConnect() == True): #Lindsay
      try:
        self.cursor.close()
        self.connection.close()
        self.setConnect(False)
      #if disconnection fails, return error
      except:
        print("Break Connection Error")
        return 1
      #if everything runs normally, return 0
      return 0

  # Moses: Commit changes
  def saveChanges(self):
    #Commit changes to database
    self.connection.commit()

  # Lindsay: Get the connection status
  def getConnect(self):
    try:
      return self.connect
    except AttributeError:
       return False

  # Lindsay: Set the connection status
  def setConnect(self, connectToSet):
    self.connect = connectToSet
	
  #######
  # Scheduled Flights CRUD 
  #######

  # Moses: Read Scheduled Flight
  def selectAllScheduledFlights(self):
    #try to select rows from table scheduled_flights
    try:
      self.cursor.execute("SELECT * FROM scheduled_flights;")
      return self.cursor.fetchall()
    #if the selection does not work, return an empty list
    except:
      print("ScheduledFlight Select All Query Has Failed")
      return []

  def selectAllJoinedScheduledFlights(self):
    #try to select rows from table scheduled_flights
    try:
      self.cursor.execute(""""SELECT flight.idFlight, flight.Airline, flight.Departure, flight.Arrival, flight.DepartureAirport, flight.ArrivalAirport, flight.Distance, flight.Time, flight.Points, 
      passengers.idPassengers, passengers.Name, passengers.FFN
      FROM scheduled_flight
      INNER JOIN passengers ON passengers.idPassengers = flight.Passenger1 OR passengers.idPassengers = flight.Passenger2 OR passengers.idPassengers = flight.Passenger3 OR passengers.idPassengers = flight.Passenger4 OR passengers.idPassengers = flight.Passenger5""")
      return self.cursor.fetchall()
    #if the selection does not work, return an empty list
    except:
      print("ScheduledFlight Select All Query Has Failed")
      return []

  #Lindsay: Get the record ID
  def getSchedId(self):
    return self.schedId

  #Lindsay: Set the record ID
  def setSchedId(self, idToSet):
    self.schedId = idToSet

  # Michelle: Insert into Scheduled Flights
  # Sprint 2 Michelle: updated Insert function so it works with new sprint 2
  def insertScheduledFlight(self, flight_name, airline_id, dep_field_id, arr_field_id, flight_type, distance, scheduled_launch, scheduled_land, aircraft_id, crew_id, ff_points):
    #try to insert a new row into scheduled flights, then commit changes
    #try:
    SQL_CREATE = "INSERT INTO scheduled_flights (flight_name, airline_id, dep_field_id, arr_field_id, flight_type, distance, scheduled_launch, scheduled_land, aircraft_id, crew_id, ff_points) VALUES ('{}', {}, {}, {}, '{}', {}, '{}', '{}', {}, {}, {});".format(flight_name, airline_id, dep_field_id, arr_field_id, flight_type, distance, scheduled_launch, scheduled_land, aircraft_id, crew_id, ff_points)
    self.cursor.execute(SQL_CREATE)
    #Lindsay's Work Begins
    self.connection.commit()
    self.cursor.execute("SELECT * FROM scheduled_flights ORDER BY id_sched_flight DESC;")
    result = self.cursor.fetchone()
    self.cursor.fetchall()
    if result is not None:
        self.setSchedId(result[0])
        return result
    else:
        return None
    #Lindsay's Work Ends
    #if the query run fails, return null value
    #except:
      #print("Problem arose with insertion into the Scheduled Flights table.")
      #return []
    
  # Lindsay: Update a record in Scheduled Flights
  def updateScheduledFlight(self, flight_name, airline_id, dep_field_id, arr_field_id, flight_type, distance, scheduled_launch, scheduled_land, aircraft_id, crew_id, ff_points, givenId):
    #try to update the scheduled_flights table, then select that row and return it, the commit the changes
    
    try:
      SQL_UPDATE = f"UPDATE scheduled_flights SET flight_name = '{flight_name}', airline_id = {airline_id}, dep_field_id = {dep_field_id}, arr_field_id = {arr_field_id}, flight_type = '{flight_type}', distance = {distance}, scheduled_launch = '{scheduled_launch}', scheduled_land = '{scheduled_land}', aircraft_id = {aircraft_id}, crew_id = {crew_id}, ff_points = {ff_points} WHERE id_sched_flight = {givenId};"
      self.cursor.execute(SQL_UPDATE)
      self.connection.commit()
      self.cursor.fetchall()
    #if the above does not run, return a null value
    except:
      print("Problem has occurred with Update Query in Scheduled Flights Table.")
      return []

  # Erin: Delete a record from Scheduled Flights
  def deleteScheduledFlight(self, flightID):
    #run delete query to delete row from scheduled flights table
    #Michelle fixed concatenation of flightID to the string and calling of 'ID' for where clause
    deleteQuery = "DELETE FROM scheduled_flights WHERE id_sched_flight = " + str(flightID)
    try:
      self.cursor.execute(deleteQuery)
    #if the ID is not found in any row, print the following message. else, commit.
      if self.cursor.rowcount == 0:
        print("No rows found with that ID")
      else:
        self.connection.commit() #Lindsay
  #except with errors, return nothing
    except:
      print("Problem has occurred with Delete Query in Scheduled Flights Table.")
      return []  
    
  #######
  # Executed Flights CRUD
  #######

  # Moses: Select All Executed Flights
  def selectAllJoinedExecutedFlights(self):
    #try to select rows of table executed_flights
    try:
      self.cursor.execute("""SELECT flight.idFlight, flight.Airline, flight.Departure, flight.Arrival, flight.DepartureAirport, flight.ArrivalAirport, flight.Distance, flight.Time, flight.Points, 
      passengers.idPassengers, passengers.Name, passengers.FFN
      FROM executed_flight
      INNER JOIN passengers ON passengers.idPassengers = flight.Passenger1 OR passengers.idPassengers = flight.Passenger2 OR passengers.idPassengers = flight.Passenger3 OR passengers.idPassengers = flight.Passenger4 OR passengers.idPassengers = flight.Passenger5""")
      return self.cursor.fetchall()
  #if it does not run, return the empty list below
    except:
      print("ExecutedFlight Select Query Has Failed")
      return []
      # Return Empty List if Failed

  # Moses: Flights joined with other tables
  def selectAllExecutedFlights(self):
    #try to select rows of table executed_flights
    try:
      self.cursor.execute("SELECT * FROM executed_flights;")
      return self.cursor.fetchall()
    #if it does not run, return the empty list below
    except:
      print("ExecutedFlight Select Query Has Failed")
      return []# Return Empty List if Failed
  
  #Lindsay: Get the record ID
  def getExecId(self):
    return self.execId

  #Lindsay: Set the record ID
  def setExecId(self, idToSet):
    self.execId = idToSet

  #CHANGES
  # Michelle: Insert into Executed Flights
  def insertExecutedFlight(self, flight_name, airline_id, dep_field_id, arr_field_id, flight_type, sched_flight_id, status, distance, launch_time, land_time, aircraft_id, crew_id, plist_id, ff_points):
    #try to insert a new row into executed flights
    try:    
      SQL_CREATE = "INSERT INTO executed_flights(flight_name, airline_id, dep_field_id, arr_field_id, flight_type, sched_flight_id, status, distance, launch_time, land_time, aircraft_id, crew_id, plist_id, ff_points) VALUES ('{}', {}, {}, {}, '{}', {}, '{}', {}, '{}', '{}', {}, {}, {}, {});".format(flight_name, airline_id, dep_field_id, arr_field_id, flight_type, sched_flight_id, status, distance, launch_time, land_time, aircraft_id, crew_id, plist_id, ff_points)
      self.cursor.execute(SQL_CREATE)
      #Lindsay's Work Begins
      self.connection.commit()
      self.cursor.execute("SELECT * FROM executed_flights ORDER BY id_exec_flight DESC;")
      result = self.cursor.fetchone()
      self.cursor.fetchall()
      if result is not None:
          self.setExecId(result[0])
          return result
      else:
          return None
      #Lindsay's Work Ends
    #If insert fails, then return null value
    except:
      print("Problem arose with insertion into the Executed Flights table.")
      return []

# Lindsay: Update a record in Executed Flights 
  def updateExecutedFlight(self, flight_name, airline_id, dep_field_id, arr_field_id, flight_type, sched_flight_id, status, distance, launch_time, land_time, aircraft_id, crew_id, plist_id, ff_points, givenId):
    #Try to update a record and then select that row and return it to the GUI, then commit the changes
    try:      
      SQL_UPDATE = f"UPDATE executed_flights SET flight_name = '{flight_name}', airline_id = {airline_id}, dep_field_id = {dep_field_id}, arr_field_id = {arr_field_id}, flight_type = '{flight_type}', sched_flight_id = {sched_flight_id}, status = '{status}', distance = {distance}, launch_time = '{launch_time}', land_time = '{land_time}', aircraft_id = {aircraft_id}, plist_id = {plist_id}, crew_id = {crew_id}, ff_points = {ff_points} WHERE id_exec_flight = {givenId};"
      self.cursor.execute(SQL_UPDATE)
      self.connection.commit()
      self.cursor.fetchall()
  #if the update fails, return a value of null
    except:
      print("Problem has occurred with Update Query in Executed Flights Table.")
      return []

  # Erin: Delete a record from Executed Flights
  def deleteExecutedFlight(self, flightID):
    #try to delete row from executed flights table where specified
    #Michelle fixed concatenation of flightID to the string
    deleteQuery = "DELETE FROM executed_flights WHERE id_exec_flight = " + str(flightID)
    try:
      self.cursor.execute(deleteQuery)
    #if the ID is not found in any row, print the following message. else, commit.
      if self.cursor.rowcount == 0:
        print("No rows found with that ID")
      else:
        self.connection.commit() #Lindsay
    #if query execution fails, return null value
    except:
      print("Problem has occurred with Delete Query in Executed Flights Table.")
      return []
      
  #Michelle: TRIGGER FROM Scheduled to Executed.
  #Michelle updated function.
  def executedFlightTrigger(self, id_sched_flight):
    #try run a query that selects specific rows from scheduled flights table to floodfill in the executedflights GUi
    try:
      sql_select_sched="SELECT flight_name, airline_id, dep_field_id, arr_field_id, flight_type, distance, scheduled_launch, scheduled_land, aircraft_id, crew_id, ff_points FROM scheduled_flights WHERE id_sched_flight={}".format(id_sched_flight)
      self.cursor.execute(sql_select_sched)
      initialList=self.cursor.fetchall()
      return initialList[0]
    #if the query run fails, return a null value
    except:
      return []
  
  # END Scheduled Flights/Executed Flights

  #######
  # Aircrafts CRUD
  #######
  
  #Erin added 'self' since self.cursor is now a global variable, and 'self.connection.commit()'
  def getAllAircrafts(self):
      
    self.cursor.execute("SELECT aircrafts_id, aircraft_type, buno FROM aircraft")

    aircraftList = []
    # Michelle added self to cursor below
    for (aircrafts_id, aircraft_type, buno) in self.cursor:
        aircraft = Aircraft(id=aircrafts_id, aircraftType=aircraft_type,
                            buno=buno
                            )
        aircraftList.append(aircraft)

    self.connection.commit()
    
    return aircraftList

  #UPDATE
  #Erin added 'self' since self.cursor is now a global variable, and 'self.connection.commit()'
  def updateAircraft(self, aircraft):
      
    print("updating - ", aircraft.getAircraftDetails())

    data_aircraft = (aircraft.getAircraftType(), aircraft.getBuno(), aircraft.getId())
    self.cursor.execute(("UPDATE aircraft SET aircraft_type = %s, buno = %s WHERE aircrafts_id = %s"), data_aircraft)
    self.connection.commit()

  #Erin added 'self' since self.cursor is now a global variable, and 'self.connection.commit()'
  def addAircraft(self, aircraft):

    print("adding aircraft ", aircraft.getAircraftDetails())

    addAircraft = ("INSERT INTO aircraft "
            "(aircraft_type, buno) "
            "VALUES (%s, %s)")
    
    data_aircraft = (aircraft.getAircraftType(), aircraft.getBuno())
    self.cursor.execute(addAircraft, data_aircraft)
    self.connection.commit()

  # Michelle changed variable name because 'id' is built in python function
  #Erin added 'self' since self.cursor is now a global variable, and 'self.connection.commit()'
  def deleteAircraft(self, ID):

    print("deleting ", ID)

    data = (ID,)
    self.cursor.execute("DELETE FROM aircraft WHERE aircrafts_id = %s", data)

    self.connection.commit()
    
  #######
  # Airports CRUD
  #######

  def getAllAirports(self):

    #Lindsay added 'self' to 'cursor.execute' since self.cursor is now a global variable, and 'self.connection.commit()'

    self.cursor.execute("SELECT airport_id, ICAO_name, country, city FROM airport")

    airportList = []
    # Not Functional
	  # Michelle added self in front of cursor
    for (airport_id, ICAO_name, country, city) in self.cursor:
        airport = Airport(id=airport_id, icaoName=ICAO_name,
                            country=country, city=city
                            )
        airportList.append(airport)

    self.connection.commit()

    return airportList
    
  #UPDATE 
  def updateAirport(self, airport):
    #Lindsay added 'self' to 'cursor.execute' since self.cursor is now a global variable, and 'self.connection.commit()'

    print("updating - ", airport.getAirportDetails())

    data_airport = (airport.getIcaoName(), airport.getCountry(), airport.getCity(), airport.getId())
    self.cursor.execute(("UPDATE airport SET ICAO_name = %s, country = %s, city = %s WHERE airport_id = %s"), data_airport)
    self.connection.commit()

  def addAirport(self, airport):
    
    #Lindsay added 'self' to 'cursor.execute' since self.cursor is now a global variable, and 'self.connection.commit()'
    print("adding airport ", airport.getAirportDetails())

    addAirport = ("INSERT INTO airport "
            "(ICAO_name, country, city) "
            "VALUES (%s, %s, %s)")
    
    data_airport = (airport.getIcaoName(), airport.getCountry(), airport.getCity())
    self.cursor.execute(addAirport, data_airport)
    self.connection.commit()
  
  def deleteAirport(self, id):
    #Lindsay added 'self' to 'cursor.execute' since self.cursor is now a global variable, and 'self.connection.commit()'
    
    print("deleting ", id)

    data = (id,)
    self.cursor.execute("DELETE FROM airport WHERE airport_id = %s", data)

    self.connection.commit()
    
  #######
  # Passengers CRUD
  #######

  #Query the Database for all records and load records
  # into self.records which is the list used to hold 
  # all records for GUI/Controller
   
  #READ BY ARSHAN
  #Erin: consistent function name changes
  def setPassengerRecord(self, pos):
    # Ryan Kennedy
    self.p_record = self.p_records[pos]

  def loadPassengers(self):
    #Arshan Rahman
    try:
      #Gets all values of passengers on the flight and orders them by last name.
      query = "SELECT * FROM passengers;"
      self.cursor.execute(query)
      #Store retrieved values.
      self.p_records = self.cursor.fetchall()
      return "Load Successfull"
    except:
      return "Error Loading Records"
        
          
  #DELETION BY CHRIS
  #Erin: consistent function name changes
  def deletePassengers(self):
    try:
      self.p_deleteID = self.p_record[0]
      query = "DELETE FROM passengers WHERE idPassenger=" + str(self.p_deleteID) + ";"
      self.cursor.execute(query)
      return "Record Deleted."
    except:
          return "Error Deleting Record"
          
  #INSERTION BY RYAN
  #Erin: consistent function name changes
  def insertPassengers(self, p_info):
    try:
      self.p_insertRec = p_info
      query = "INSERT INTO passengers (firstName, lastName, licenseNum, gender, nationality, noFlyStatus) VALUES (\"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(self.p_insertRec[0],
                                                                                                                                                                       self.p_insertRec[1],
                                                                                                                                                                       self.p_insertRec[2],
                                                                                                                                                                       self.p_insertRec[3],
                                                                                                                                                                       self.p_insertRec[4],
                                                                                                                                                                       self.p_insertRec[5])
      self.cursor.execute(query)
      return "Insertion Completed"
    except:
      return "Error Inserting Record"
            
        
  #UPDATE SECTION (crUd)
  #Erin: consistent function name changes
  #michelle added minor changes to align sql to correct syntax
  def updatePassengers(self, p_info):
    #Arshan Rahman
    try:
      self.p_updateRec = [self.p_record[0], p_info[0], p_info[1], p_info[2], p_info[3], p_info[4], p_info[5]]
      #self.p_updateRec[0] = self.p_record[0]
      #self.p_updateRec[1] = p_info[0]
      #self.p_updateRec[2] = p_info[1]
      #self.p_updateRec[3] = p_info[2]
      #self.p_updateRec[4] = p_info[3]
      #self.p_updateRec[5] = p_info[4]
      #self.p_updateRec[6] = p_info[5]
      query = "UPDATE passengers SET firstName = \'{}\', lastName = \'{}\', licenseNum = {}, gender = \'{}\', nationality = \'{}\', noFlyStatus = \'{}\' WHERE idPassenger = {};".format(self.p_updateRec[1],
                                                                                                                                                                                         self.p_updateRec[2],
                                                                                                                                                                                         self.p_updateRec[3],
                                                                                                                                                                                         self.p_updateRec[4],
                                                                                                                                                                                         self.p_updateRec[5],
                                                                                                                                                                                         self.p_updateRec[6],
                                                                                                                                                                                         self.p_updateRec[0])
      #Simple check to make sure update statement works as needed.
      self.cursor.execute(query)
      return "Update Successful"
    except:
      return "Error Updating Record"
    
  # Ryan Kennedy
  #Erin: consistent function name changes
  def selectPassengers(self, columnList, condition):
    try:
      query = "SELECT "    # Creates, formats, and runs a query to select certain fields where certain conditions are true from passengers
      for x in columnList:
          query += x 
          query += ", "
          query[:-2]
      if(condition == []):
          query += "FROM passengers WHERE {};".format(condition)
          self.cursor.execute(query)
          self.p_records = self.cursor.fetchall()
      else:
          query += "FROM passengers;"
          self.cursor.execute(query)
          self.p_records = self.cursor.fetchall()
      return "Loaded"
    except:
      return "Error Selecting Record"
    
  #######
  # Passengers Lists CRUD
  #######

  #CRUD FOR 2nd TABLE (Passengers Lists) Made by Matheww and Ben
  #READ
  #Ben Barrett: Reading records from passengerlist in the order of Id.
  #Erin: consistent function name changes

  def setPassengersListsRecord(self, pos):
    # Ryan Kennedy
    self.plist_record = self.plist_records[pos]


  def loadPassengersLists(self):
    #Ryan Kennedy
    try:
      #Gets all values of passengers on the flight and orders them by last name.
      query = "SELECT * FROM passengerlists;"
      self.cursor.execute(query)
      #Store retrieved values.
      self.plist_records = self.cursor.fetchall()
      return "Load Successfull"

    except:
        return "Error Loading Records"

  def selectPassengersLists(self, columnList, condition):
    try:
      query = "SELECT "    # Creates, formats, and runs a query to select certain fields where certain conditions are true from passengers
      for x in columnList:
          query += x 
          query += ", "
          query[:-2]
      if(condition == []):
          query += "FROM passengerlists WHERE {};".format(condition)
          self.cursor.execute(query)
          self.p_records = self.cursor.fetchall()
      else:
          query += "FROM passengers;"
          self.cursor.execute(query)
          self.plist_records = self.cursor.fetchall()
      return "Loaded"
    except:
      return "Error Selecting Record"
    
  #DELETE
  #Ben Barrett: Deleting records from passengerslist where idPassenger = a certain Id.
  #Erin: consistent function name changes
  def deletePassengersLists(self):
    try:
      self.plist_deleteId = self.plist_record[0]
      query = "DELETE FROM passengerlists WHERE idPassList =" + str(self.plist_deleteId) + ";"
      self.cursor.execute(query)
      return "Deleted."
    except:
      return "Error Deleting Record"
      
  #UPDATE
  #Mathew Lam: Update for Passengers List. Updating Values such as PassList, pass1Id, pass1Presentm pass2Id, pass2Present, pass3Id, pass3Present.
  #Erin: consistent function name changes
  def updatePassengersLists(self, plist_info):
      try:
          self.plist_updateRec = [self.plist_record[0], plist_info[0], plist_info[1], plist_info[2], plist_info[3], plist_info[4], plist_info[5], plist_info[6], plist_info[7], plist_info[8], plist_info[9]]

          #self.plist_updateRec[0] = self.plist_record[0]
          #self.plist_updateRec[1] = plist_info[0]
          #self.plist_updateRec[2] = plist_info[1]
          #self.plist_updateRec[3] = plist_info[2]
          #self.plist_updateRec[4] = plist_info[3]
          #self.plist_updateRec[5] = plist_info[4]
          #self.plist_updateRec[6] = plist_info[5]
          #self.plist_updateRec[7] = plist_info[6]
          #self.plist_updateRec[8] = plist_info[7]
          #self.plist_updateRec[9] = plist_info[8]
          #self.plist_updateRec[10] = plist_info[9]
          query = "UPDATE passengerlists SET pass1Id = {}, pass1Present = \"{}\", pass2Id = {}, pass2Present = \"{}\", pass3Id = {}, pass3Present = \"{}\", pass4Id = {}, pass4Present = \"{}\", pass5Id = {}, pass5Present = \"{}\" WHERE idPassList = {}".format(self.plist_updateRec[1],
                                                                                                                                                                                                                                                                   self.plist_updateRec[2],
                                                                                                                                                                                                                                                                   self.plist_updateRec[3],
                                                                                                                                                                                                                                                                   self.plist_updateRec[4],
                                                                                                                                                                                                                                                                   self.plist_updateRec[5],
                                                                                                                                                                                                                                                                   self.plist_updateRec[6],
                                                                                                                                                                                                                                                                   self.plist_updateRec[7],
                                                                                                                                                                                                                                                                   self.plist_updateRec[8],
                                                                                                                                                                                                                                                                   self.plist_updateRec[9],
                                                                                                                                                                                                                                                                   self.plist_updateRec[10],
                                                                                                                                                                                                                                                                   self.plist_updateRec[0],
                                                                                                                                                                                                                                                                   ) #fixed by Chris :)
          self.cursor.execute(query)
          return "Updated"
      except:
          return "Error Updating Record"
        
  #CREATE
  #Mathew Lam: Create for PassengersList. Inserting Values such as PassList, pass1Id, pass1Presentm pass2Id, pass2Present, pass3Id, pass3Present.
  #Erin: consistent function name changes
  def insertPassengersLists(self, plist_info):
    try:
      self.plist_insertRec = plist_info
      #self.plist_insertRec[0] = plist_info[0]
      #self.plist_insertRec[1] = plist_info[1]
      #self.plist_insertRec[2] = plist_info[2]
      #self.plist_insertRec[3] = plist_info[3]
      #self.plist_insertRec[4] = plist_info[4]
      #self.plist_insertRec[5] = plist_info[5]
      #self.plist_insertRec[6] = plist_info[6]
      #self.plist_insertRec[7] = plist_info[7]
      #self.plist_insertRec[8] = plist_info[8]
      #self.plist_insertRec[9] = plist_info[9]
      query = "INSERT INTO passengerlists (pass1Id, pass1Present, pass2Id, pass2Present, pass3Id, pass3Present, pass4Id, pass4Present, pass5Id, pass5Present) VALUES ({},\"{}\",{},\"{}\",{},\"{}\",{},\"{}\",{},\"{}\");".format(self.plist_insertRec[0],
                                                                                                                                                                                                                                  self.plist_insertRec[1],
                                                                                                                                                                                                                                  self.plist_insertRec[2],
                                                                                                                                                                                                                                  self.plist_insertRec[3],
                                                                                                                                                                                                                                  self.plist_insertRec[4],
                                                                                                                                                                                                                                  self.plist_insertRec[5],
                                                                                                                                                                                                                                  self.plist_insertRec[6],
                                                                                                                                                                                                                                  self.plist_insertRec[7],
                                                                                                                                                                                                                                  self.plist_insertRec[8],
                                                                                                                                                                                                                                  self.plist_insertRec[9]
                                                                                                                                                                                                                                  )
      self.cursor.execute(query)
      return "Inserted."
    except:
      return "Error Inserting Record."

  
  #######
  # Pilots CRUD
  #######
 
  #Erin: consistent function name changes
  #Insert Pilot
  #CREATE
  #Andy: used to creating the informations for the pilots - being fixed by Kingsley
  def insertPilot(self):
    try:
      
      q= ("INSERT INTO pilot (first_name,last_name,position, aircraft_qualification_1, aircraft_qualification_2, aircraft_qualification_3) VALUES()")
      
      self.cursor.execute(q, [self.insert_pi[0], self.insert_pi[1], self.insert_pi[2], self.insert_pi[3], self.insert_pi[4], self.insert_pi[5]])
      self.connection.commit()
      self.loadPilots()
      print("Pilot inserted")

    except mysql.connector.Error as e:
      return 'Error:' + e

  #READ
  #reading and selecting the pilots
  def loadPilots(self):
    try:
      q = ('''SELECT * FROM pilots''')
      self.cursor.execute(q)
      self.pilots = self.cursor.fetchall()
      return ""
    except mysql.connector.Error as e:
     return 'Error:' + e 

  #UPDATE 
  #updating the pilots information if the wrong information is put or ohter information is needed
  def updatePilots(self, ID):
    try:
      q = ('UPDATE pilot SET first_name='+self.update_pi[1]+
          "', last_name='"+self.update_pi[2]+
          "', position='"+self.update_pi[3]+
          "',aircraft_qualification_1='"+self.update_pi[4]
          +"',aircraft_qualification_2='"+self.update_pi[5]+
          "',aircraft_qualification_3='"+self.update_pi[6]+
          "' WHERE id_pilot ="+str(self.update_pi[0]))
      self.cursor.execute(q)
      self.connection.commit()
      
    except mysql.connector.Error as e:
      return 'Error, {}' .format(e)

  #DELETE 
  #deleting the pilots information
  def deletePilots(self, id):
    try:
      q = ('DELETE FROM pilot WHERE id_pilot='+str(id)+';')
      self.cursor.execute(q)
      self.connection.commit()
      self.loadP()
    except mysql.connector.Error as e:
      return 'Error, {}'.format(e)

  #######
  # Flight Attendants CRUD
  #######
  
  #CREATE
  # - Kingsley(start): Inserting a flight attendant
  def createflight_attendants(self):
    try:
      q = ("INSERT INTO flightattendants (first_name, last_name, airline_id, position) VALUES (?,?,?,?)")
      self.cursor.execute(q, [self.insert_fa[0], self.insert_fa[1], self.insert_fa[2], self.insert_fa[3]])
      self.connection.commit()
      self.loadflight_attendants() # Not Functional
    except mysql.connector.Error as e:
      return "Error:" + e
   
  #READ
  # Selects all records from the flight_attendant table and loads it into the gui
  def loadflight_attendants(self):
      try:
        q = ("SELECT * FROM flight_attendants")
        self.cursor.execute(q)
        self.attendants = self.cursor.fetchall()
        return ""
      except mysql.connector.Error as e:
        return "Error:" + e
  # Kingsley(stop)

  #Andy: Update a flight attendant
  def update_flight_attendants(self, ID):
    try:
      q = ("UPDATE flight_attendants SET firstName='"+self.update_fa[1]+
          "', lastName='"+self.update_fa[2]+
          "', airline_id="+str(self.update_fa[3]))
      +", pos='" + self.update_fa[4]+"' WHERE id_flight_attendant="+str(self.update_fa[0])
      self.cursor.execute(q)
      self.connection.commit()
      
    except mysql.connector.Error as e:
      return "Error, {}" .format(e)

  #Andy and Leo: Deleting a flight attendant
  def deleteflight_attendants(self, id):
    try:
      q = ("DELETE FROM flight_attendants WHERE id_flight_attendant="+str(id)+";")
      self.cursor.execute(q)
      self.connection.commit()
      self.loadFA()
    except mysql.connector.Error as e:
      return "Error, {}".format(e)


  #######
  # Crew CRUD
  #######

  #Create 
  #Written by: Nameer Sadiq
  #michelle fixed query
  def createCrew(self, CaptainID, CoPilotID, SeniorFAID, FA2ID):
      query = "INSERT INTO crews (captain_id, copilot_id, senior_fa_id, fa2_id) VALUES (%s, %s, %s, %s)"
      values = (CaptainID, CoPilotID, SeniorFAID, FA2ID)
      with self.connection.cursor() as cursor:
          cursor.execute(query, values)
          self.connection.commit()

  #Read
  #Omar Jibreen
  def readCrew(self, CrewID):
      query = "SELECT * FROM crews WHERE id_crew = %s"
      values = (CrewID,)
      with self.connection.cursor() as cursor:
          cursor.execute(query, values)
          row = cursor.fetchone()
      return row
        
  #Update
  #Omar Jibreen
  #michelle added correct queries
  def updateCrew(self, CrewID, CaptainID, CoPilotID, SeniorFAID, FA2ID):
      query = "UPDATE crews SET captain_id = %s, copilot_id = %s, senior_fa_id=%s, fa2_id=%s WHERE id_crew = %s"
      values = (CrewID, CaptainID, CoPilotID, SeniorFAID, FA2ID)
      with self.connection.cursor() as cursor:
          cursor.execute(query, values)
          self.connection.commit()
            
  #Delete
  #Omar Jibreen
  #michelle fixed query name
  def deleteCrew(self, CrewID):
    query = "DELETE FROM crews WHERE id_crew = %s"
    values = (CrewID,)
    with self.connection.cursor() as cursor:
      cursor.execute(query, values)
      self.connection.commit()


  def fetchByCrewID(self, CrewID):
    self.cursor.execute(
        "SELECT * FROM crews WHERE id_crew = {}" .format(CrewID))
    row = self.cursor.fetchone()
    return row

  def fetch_1st(self, CrewID):
      self.cursor.execute(
          "SELECT * FROM crews WHERE id_crew = {} ORDER BY id_crew ASC" .format(CrewID))
      row = self.cursor.fetchone()
      return row

  def fetch_end(self, CrewID):
      self.cursor.execute(
          "SELECT * FROM crews WHERE id_crew = {} ORDER BY id_crew DESC" .format(CrewID))
      row = self.cursor.fetchone()
      return row

  def forward(self, CrewID):
      self.cursor.execute(
          "SELECT * FROM crews WHERE id_crew = {} ".format(CrewID))
      row = self.cursor.fetchone()
      if (row == None):
          return self.fetchByCrewID(CrewID)
      else:
          return row

  def forward2(self,CrewID):
      self.cursor.execute(
          "SELECT * FROM crews WHERE CrewID_crew = {} ".format(CrewID))
      row = self.cursor.fetchone()
      if (row == None):
          return self.fetchByCrewID(CrewID)
      else:
          return row

  def back(self, CrewID):
      self.cursor.execute(
          "SELECT * FROM crews WHERE CrewID_crew = {} ORDER BY CrewID_crew DESC" .format(CrewID))
      row = self.cursor.fetchone()
      if (row == None):
          return self.fetchByCrewID(CrewID)
      else:
          return row

   
  def back2(self, CrewID):
    self.cursor.execute(
          "SELECT * FROM crews WHERE CrewID_crew = {} ORDER BY CrewID_crew DESC" .format(CrewID))
    row = self.cursor.fetchone()
    if (row == None):
          return self.fetchByCrewID(CrewID)
    else:
        return row
      


  #######
  # Airline CRUD
  #######

  def selectAllAirlines(self):
    try:
      self.cursor.execute("SELECT * FROM airlines;")
      return self.cursor.fetchall()
    except:
      print("Select All Query Has Failed")
  #Jarrett
      #Inserting
  def insert(self, id, EIN, Name):
      self.cursor.execute("INSERT INTO airlines (id_airline, EIN, Name) VALUES ({}, '{}', '{}')".format(id, EIN, Name))
      self.connection.commit()
  #Matt
      #Deleting 
  def delete(self, id):
      self.cursor.execute("DELETE FROM airlines WHERE id_airline = {}" .format(id))
      self.connection.commit()
  #Jarrett
  #Updating
  def update(self, EIN, Name, id):
      self.cursor.execute("UPDATE airlines SET EIN = '{}', Name = '{}' WHERE id_airline = {}" .format(EIN, Name, id))
      self.connection.commit()

  def fetchById(self, id):
    self.cursor.execute(
        "SELECT * FROM airlines WHERE id_airline = {}" .format(id))
    row = self.cursor.fetchone()
    return row

  #######  Method to retrieve first record by ID ASC #########
  def fetch_first(self, id):
      self.cursor.execute(
          "SELECT * FROM airlines WHERE id_airline = {} ORDER BY id_airline ASC" .format(id))
      row = self.cursor.fetchone()
      return row

  #######  Method to retrieve last record by ID DESC #########
  def fetch_last(self, id):
      self.cursor.execute(
          "SELECT * FROM airlines WHERE id_airline = {} ORDER BY id_airline DESC" .format(id))
      row = self.cursor.fetchone()
      return row

  #######  Method to retrieve next record by ID ASC #########
  def next(self, id):
      self.cursor.execute(
          "SELECT * FROM airlines WHERE id_airline = {} ".format(id))
      row = self.cursor.fetchone()
      if (row == None):
          return self.fetchById(id)
      else:
          return row

  #######  Method to retrieve second next record by ID ASC #########
  def next2(self,id):
      self.cursor.execute(
          "SELECT * FROM airlines WHERE id_airline = {} ".format(id))
      row = self.cursor.fetchone()
      if (row == None):
          return self.fetchById(id)
      else:
          return row

  #######  Method to retrieve previous record by ID DESC #########
  def prev(self, id):
      self.cursor.execute(
          "SELECT * FROM airlines WHERE id_airline = {} ORDER BY id_airline DESC" .format(id))
      row = self.cursor.fetchone()
      if (row == None):
          return self.fetchById(id)
      else:
          return row

    #######  Method to retrieve previous record by ID DESC #########
  def prev2(self, id):
    self.cursor.execute(
          "SELECT * FROM airlines WHERE id_airline = {} ORDER BY id_airline DESC" .format(id))
    row = self.cursor.fetchone()
    if (row == None):
          return self.fetchById(id)
    else:
        return row
      

  ########
  #Passenger and Passsenger List CRUD
  ########





########
# Unused Code
########

# Former Passenger Connection Methods
# 
# class passengerDb():

 # def __init__(self):

      #ALL ERROR MESSAGES BY CHRIS (try and except lines)

      #Defining variables in class

      # Connection flag
#      self.connected = False

#      self.p_records = []
#      self.p_record = []
#      self.plist_records = []
#      self.plist_record = []

      #Holding variables for  records to be inserted / updated
#      self.p_insertRec=["","",0,"","",""]
#      self.p_updateRec=[0,"","",0,"","",""]
#      self.plist_insertRec = [0,0,0,0,0,0]
#      self.plist_updateRec = [0,0,0,0,0,0,0]


  #     self.connection = sql.connector.connect(
  #           host = "192.168.0.116",
  #           user = "vader",
  #           password = "jchs",
  #           database = "Period_6"
  #           )
            
  #     self.cursor = self.connection.cursor()
  #     #administrative utilty variables for debugging
  #     self.alertMessage= "No Message Yet."

  #     ################################
  #     #Connection to database Section#
  #     ################################

  #     #Connect method to database
  # #def connect(self):
  # #      #Ryan Kennedy, Arshan Rahman
  # #      try: 
  # #          
  # #          self.connection = sql.connector.connect(
  # #          host = "192.168.0.116",
  # #          user = "vader",
  # #          password = "jchs",
  # #          database = "Period_6"
  # #          )
  # #          
  # #          self.cursor = self.connection.cursor()
  # #      except:
  # #        print("Error while connecting to MySQL", )
  # #        return 
    
  #   #DISCONNECT METHOD
  # def disconnect(self):
  #     # Ryan Kennedy
  #     try:
  #         if(self.connection.is_connected()):
  #             self.connection.close()
  #             return "Connection Closed."
  #     except:
  #         return 

  
# Former Pilots Connection Code

# def connect(self, q):
#       #All database connections and queries should be try/excepted
#       try:
#           #Connection object to local database in mysql
#           self.connection = mysql.connector.connect(
#             host = "192.168.0.116",
#             port = 3306,
#             user = "yoda",
#             password = "jchs",
#             database =q
#           )

#           #Cursor object for this database
#           self.cursor = self.connection.cursor()

#           return "Connected Properly."
      
#       except:
#           return "Error Connecting: ",  

#   #Disconnecting from the database
# def disconnect(self):
#       if(self.connection):
#           self.connection.close()
#           return "Connection Closed"



# def placeholder(self):
#     pass



# Former Flight Attendant Connection Code

      
# def __init__(self):
    
#     self.table = ["Pilot"]
    


# def __init__(self, host, user, password, database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.connection = None
        
# 	#Connection to database
# 	#Written by: Nameer Sadiq
#     def connect(self):
#         self.connection = mysql.connector.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database
#        	 )

#     def disconnect(self):
#         if self.connection is not None:
#             self.connection.close()

#Flight Attendant Issues Again?
      
# def connect(self):
#         self.connection = mysql.connector.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database
#         )

#Matt: Disconnect from the database
# def disconnect(self):
#     self.connection.close()
