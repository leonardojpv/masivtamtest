from abc import ABC, abstractmethod

class DataConnector(ABC):

    @abstractmethod
    def cursor(self):
        pass

    @abstractmethod
    def getDBEntity(self):
        pass

    @abstractmethod
    def cursor():
        pass

    @abstractmethod
    def getDBEntity():
        pass

    @abstractmethod
    def addDBEntry():
        pass

    @abstractmethod
    def deleteDBEntry():
        pass
    
    @abstractmethod
    def updateDBEntry():
        pass