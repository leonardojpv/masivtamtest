import mysql.connector, json
from classes.person import Person
from classes.MySQLConnector import MySQLConnector

class User(Person):

    connector = MySQLConnector()

    def __init__(self, name = "", age  = "", username  = "", email  = ""):
        self.name, self.age, self.username, self.email = name, age, username, email

    def saveToDB(self):
        return(self.connector.addDBEntry("users", self.toJson()))

    def updateDB(self, id):
        dictId = json.loads('{"id":"'+id+'"}')
        dictData = json.loads(self.toJson())
        data = {**dictId,**dictData}
        data = json.dumps(data)
        return(self.connector.updateDBEntry("users", data))

    def deleteFromDB(self, id):
        return(self.connector.deleteDBEntry("users", id))

    def getAll(self):
        return(self.connector.getDBEntity("users"))
        
    def toJson(self):
        return(json.dumps(self.__dict__))
