from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def saveToDB():
      pass

    @abstractmethod
    def updateDB():
      pass

    @abstractmethod
    def deleteFromDB():
      pass

    @abstractmethod
    def getAll():
      pass

    @abstractmethod
    def toJson():
        pass