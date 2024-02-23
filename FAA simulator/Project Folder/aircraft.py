# pylint: disable=locally-disabled, bare-except, multiple-statements, mixed-indentation, bad-indentation, bad-continuation, attribute-defined-outside-init, pointless-string-statement, C  
"""
Pranavi Kuravi, Mariana Vega, Samantha Forero

"""


class Aircraft:

    def __init__(self, aircraftType, buno, id=-1):

        # instance variables
        self.id = id
        self.aircraftType = aircraftType
        self.buno = buno
        

    # getter and setter methods for instance variables
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getAircraftType(self):
        return self.aircraftType

    def setAircraftType(self, aircraftType):
        self.aircraftType = aircraftType

    def getBuno(self):
        return self.buno

    def setBuno(self, buno):
        self.buno = buno


    # This method formats the instance details and returns the details as string
    def getAircraftDetails(self):

        details = "Id: {0}, Aircraft Type: {1}, BUNO: {2}".format(
            self.getId(), self.getAircraftType(), self.getBuno()
        )

        return details
