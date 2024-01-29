from __future__ import annotations
from abc import ABC,abstractmethod

"""
The ABC is an abbreviation for Abstract Base Class, and it is a module in Python's standard library 
(abc stands for Abstract Base Classes). Abstract base classes are used for defining abstract 
interfaces in Python.

The abstract method is a decorator provided by the abc module. It is used to declare 
abstract methods within an abstract class. Abstract methods are meant to be overridden by 
concrete (non-abstract) subclasses.

"""

"""
                Product p = createProduct()
                p.doStuff()
                    |
                    |-----------------------           Creator
                                                + someOperation()          ---------------->  Product(interface)
                                                + createProduct():Product                     + doStuff()
                                                        |                                            |
                                                        |                                            |
                                        ----------------|----------------                            |
                                        |                               |                    ---------------------
                                        |                               |                    |                   |
                                        |                               |               ConcreteProductA     ConcreteProductB
                                ConcreateCreatorA               ConcreateCreatorB
                                + createProduct():Product       + createProduct(): Product
                                        
                                        
                                        
    """ 

class Creator(ABC):

    def factory_method(self):

        pass

    def some_operation(self)->str:
        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result
    

class ConcreteCreator1(Creator):

    def factory_method(self)-> Product:
        return ConcreteProduct1()
    
class ConcreteCreator2(Creator):

    def factory_method(self)-> Product:
        return ConcreteProduct2()


class Product(ABC):

    def operation(self)->str:
        pass

class ConcreteProduct1(Product):
    def operation(self)->str:
        return "{Result of the ConcreteProduct1}"
    
class ConcreteProduct2(Product):
    def operation(self)->str:
        return "{Result of the ConcreteProduct2}"
    
def client_code(creator:Creator)->None:

    print(f"Client: I'm not aware of the client class, but it still works.\n"
           f"{creator.some_operation()}",end="")
    
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App:Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
    

