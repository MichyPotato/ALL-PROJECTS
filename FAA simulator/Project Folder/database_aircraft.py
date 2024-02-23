# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
"""
Pranavi Kuravi, Mariana Vega, Samantha Forero

"""

# Preprocessor Directives
import os
import sys
import mysql.connector


from aircraft import Aircraft

#The database connection
class Database:
    
    def __init__(self):

        # instance variables
        """
        # Holds the Db connection to sqlite
        self.conn = mysql.connector.connect(user='vader', password='jchs',
                              host='192.168.0.116',
                              database='airline_aircraft')
        """
        self.conn = mysql.connector.connect(user='traveluser', password='password',
                              host='127.0.0.1',
                              database='example')
        
        #Debugging by Moses
        # try:
        #     self.conn = mysql.connector.connect(
        #         host = "localhost",
        #         port = 3308, #(the default port is 3306)
        #         user = "root",
        #         password = "Lj9753@1",
        #         database = "airline_period_6"
        #     )
        #     # Establish the cursor used to execute later queries based on the connection above.
        #     self.cursor = self.conn.cursor()
        #     # If connection fails, return error
        # except:
        #     print("Create Connection Error")

        # sets the reference of DB connection's row factory to Row
        # This enables retreiving record data using column names than index numbers
        #self.conn.row_factory = sqlite3.Row

        print("Connection details:  ", self.conn)
    
    # This method closes the DB connection
    def closeDbConnection(self):
        self.conn.close()

    
    def getAllAircrafts(self):

        cursor = self.conn.cursor()
        cursor.execute("SELECT id_aircraft, aircraft_type, buno FROM aircrafts")

        aircraftList = []

        for (id_aircraft, aircraft_type, buno) in cursor:
            aircrafts = Aircraft(id=id_aircraft, aircraftType=aircraft_type,
                                buno=buno
                                )
            aircraftList.append(aircrafts)

        cursor.close()

        return aircraftList



    #update 
    def updateAircraft(self, aircrafts):
        print("updating - ", aircrafts.getAircraftDetails())

        cursor = self.conn.cursor()
        data_aircraft = (aircrafts.getAircraftType(), aircrafts.getBuno(), aircrafts.getId())
        cursor.execute(("UPDATE aircrafts SET aircraft_type = %s, buno = %s WHERE id_aircraft = %s"), data_aircraft)
        self.conn.commit()



    def addAircraft(self, aircrafts):
        print("adding aircrafts ", aircrafts.getAircraftDetails())
        cursor = self.conn.cursor()

        addAircraft = ("INSERT INTO aircrafts "
               "(aircraft_type, buno) "
               "VALUES (%s, %s)")
        
        data_aircraft = (aircrafts.getAircraftType(), aircrafts.getBuno())
        cursor.execute(addAircraft, data_aircraft)

        self.conn.commit()
        cursor.close()

        

   
    def deleteAircraft(self, id):
        print("deleting ", id)

        cursor = self.conn.cursor()
        data = (id,)
        cursor.execute("DELETE FROM aircrafts WHERE id_aircraft = %s", data)

        self.conn.commit()
     
