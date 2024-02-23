# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
"""
Pranavi Kuravi
6th period
APCS50
SQL Database Connection POCO
"""

# Preprocessor Directives
import os
import sys
import mysql.connector


from airport import Airport

#The database connection
class Database:
    
    def __init__(self):

        # instance variables
        
        # Holds the Db connection to SQL
        """
        self.conn = mysql.connector.connect(user='vader', password='jchs',
                              host='192.168.0.116',
                              database='airline_aircraft')
        """
        self.conn = mysql.connector.connect(user='traveluser', password='password',
                              host='127.0.0.1',
                              database='example')

        # #Debugging by Moses
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
        

        print("Connection details:  ", self.conn)
    
    # This method closes the DB connection
    def closeDbConnection(self):
        self.conn.close()

    
    def getAllAirports(self):

        cursor = self.conn.cursor()
        cursor.execute("SELECT id_airport, ICAO, country, city FROM airports")

        airportList = []

        for (id_airport, ICAO, country, city) in cursor:
            airports = Airport(id=id_airport, icaoName=ICAO,
                                country=country, city=city
                                )
            airportList.append(airports)

        cursor.close()

        return airportList

    #update 
    def updateAirport(self, airports):
        print("updating - ", airports.getAirportDetails())

        cursor = self.conn.cursor()
        data_airport = (airports.getIcaoName(), airports.getCountry(), airports.getCity(), airports.getId())
        cursor.execute(("UPDATE airports SET ICAO = %s, country = %s, city = %s WHERE id_airport = %s"), data_airport)
        self.conn.commit()



    def addAirport(self, airports):
        print("adding airports ", airports.getAirportDetails())
        cursor = self.conn.cursor()

        addAirport = ("INSERT INTO airports "
               "(ICAO, country, city) "
               "VALUES (%s, %s, %s)")
        
        data_airport = (airports.getIcaoName(), airports.getCountry(), airports.getCity())
        cursor.execute(addAirport, data_airport)

        self.conn.commit()
        cursor.close()

        

   
    def deleteAirport(self, id):
        print("deleting ", id)

        cursor = self.conn.cursor()
        data = (id,)
        cursor.execute("DELETE FROM airports WHERE id_airport = %s", data)

        self.conn.commit()
     
