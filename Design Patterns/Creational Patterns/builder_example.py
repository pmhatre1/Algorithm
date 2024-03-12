from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import Any


"""
The ABC is an abbreviation for Abstract Base Class, and it is a module in Python's standard library 
(abc stands for Abstract Base Classes). Abstract base classes are used for defining abstract 
interfaces in Python.

The abstract method is a decorator provided by the abc module. It is used to declare 
abstract methods within an abstract class. Abstract methods are meant to be overridden by 
concrete (non-abstract) subclasses.

"""

"""
      ------------------------- Client ---------------------------
     |                                                            |
     |                                                            |
     |                                                         Director
     |                                                       - builder : Builder
     |              Builder      <---------------------------+ Director(builder)
     |                                                       + changeBuilder(builder)
     |              +  reset()                                 + make(type)
     |               + buildStepA()
     |               + buildStepB()
     |              + buildStepZ()                       
     |                      |
Concrete                Concrete
Builder 1               Builder 2
-result: Product1       -result: Product2
+ reset()               + reset()
+ buildStepA()          + buildStepA()
+ buildStepB()          + buildStepB()
+ buildStepZ()          + buildStepZ()
+ getResult():          + getResult():
    Product1                Product1

    """ 
class Builder(ABC):

    def reset(self) -> None:
        pass

    def setSeats(self,number) -> None:
        pass
    
    def setEngine(self,engine) -> None:
        pass

    def setTripComputer(self) -> None:
        pass

    def setGPS(self) -> None:
        pass


class ConcreteCarBuilder(Builder):

    def __init__(self)-> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()
    
    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product
    
    def setEngine(self, engine) -> None:
        self._product.add(engine)
    
    def setGPS(self) -> None:
        self._product.add("CarGPS")
    
    def setSeats(self, number) -> None:
        self._product.add("CarSeats")

    def setTripComputer(self) -> None:
        self._product.add("TripComputer")

class ConcreteCarManualBuilder(Builder):

    def __init__(self)-> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()
    
    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product
    
    def setEngine(self, engine) -> None:
        self._product.add(engine)
    
    def setGPS(self) -> None:
        self._product.add("CarManualGPS")
    
    def setSeats(self, number) -> None:
        self._product.add("CarManualSeats")

    def setTripComputer(self) -> None:
        self._product.add("TripManualComputer")

class Product1():

    def __init__(self)-> None:
        self.parts = []

    def add(self,part:Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Product parts: {','.join(self.parts)}",end = "")


class Director:

    def __init__(self)-> None:
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self,builder:Builder) -> None:
        self._builder = builder
    
    def build_car(self) -> None:
        self.builder.reset()
        self.builder.setEngine("Engine")
        self.builder.setGPS()
        self.builder.setSeats(6)
        self.builder.setTripComputer()

     
    def build_car_manual(self) -> None:
        self.builder.reset()
        self.builder.setEngine("ManualEngine")
        self.builder.setGPS()
        self.builder.setSeats(5)
        self.builder.setTripComputer()



if __name__ == "__main__":
    
    director = Director()
    builder =  ConcreteCarBuilder()
    director.builder = builder
    

    print("Car builder reqs are:")
    director.build_car()
    builder.product.list_parts()

    print("\n")

    print("Car builder manual reqs are:")
    builder = ConcreteCarManualBuilder()
    director.builder = builder
    director.build_car_manual()
    builder.product.list_parts()





