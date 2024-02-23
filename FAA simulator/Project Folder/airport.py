# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
"""
Pranavi Kuravi
6th period
APCS50
Airport POCO. 
Useful for holding details for airports
"""


class Airport:

    def __init__(self, icaoName, country, city, id=-1):

        # instance variables
        self.id = id
        self.icaoName = icaoName
        self.country = country
        self.city = city

    # getter and setter methods for instance variables
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getIcaoName(self):
        return self.icaoName

    def setIcaoName(self, icaoName):
        self.icaoName = icaoName

    def getCountry(self):
        return self.country

    def setCountry(self, country):
        self.country = country

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city


    # This method formats the instance details and returns the details as string
    def getAirportDetails(self):

        details = "Id: {0}, ICAO: {1}, Country: {2}, City: {3}".format(
            self.getId(), self.getIcaoName(), self.getCountry(),
            self.getCity()
        )

        return details
