import mysql.connector, json
from classes.DataConnector import DataConnector

class MySQLConnector(DataConnector):

    def __init__(self, h = "localhost", u = "root", p = "", db = "flask-crud"):
        self.connection = database = mysql.connector.connect(host = h, user = u, password = p, database = db)

    def cursor(self):
        return self.connection.cursor()

    def getDBEntity(self, entity):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM " + entity)
        response = cursor.fetchall()
        data = []
        columnNames = [column[0] for column in cursor.description]
        for entry in response:
            data.append(dict(zip(columnNames, entry)))
        cursor.close()
        return(data)

    
    def addDBEntry(self, entity, data):
        cursor = self.connection.cursor()
        keys = json.loads(data).keys()
        values = json.loads(data).values()
        sql = "INSERT INTO " + entity + " ("
        for key in keys:
            sql = sql + " "+ key +","
        sql = sql[:-1]
        sql = sql + ") VALUES ("
        for value in values:
            sql = sql + "'"+ value +"',"
        sql = sql[:-1]
        sql = sql + ");"
        cursor.execute(sql)
        self.connection.commit()
        id = cursor.lastrowid
        cursor.close()
        return(id)


    def deleteDBEntry(self, entity, id):
        cursor = self.connection.cursor()
        result = cursor.execute("DELETE FROM " + entity + " WHERE id=" + id)
        self.connection.commit()
        cursor.close()
        return(result)
    
    def updateDBEntry(self, entity, data):
        data = json.loads(data)
        cursor = self.connection.cursor()
        sql = "UPDATE " + entity + " SET "
        for key, value in data.items():
            sql = sql + key + " = '" + value + "', "
        sql = sql[:-2] + " "
        sql = sql + "WHERE id = " + data['id']
        result = cursor.execute(sql)
        self.connection.commit()
        cursor.close()
        return(result)