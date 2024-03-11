from __future__ import annotations
from abc import ABC, abstractclassmethod

"""
        ----------------------ConcreteFactory1
        |         |             + createProduct_A()
        |         |             + createProduct_B()
    Concrete   Concrete 
    ProductA1  ProductB1              |
        |         |                   |
        |         |                   |------------------------Client
     Abstract   Abstract              |                        +someOperation()
     ProductA   ProductB              |
                                AbstractFactory
                                 <<interface>>                   
"""  

class AbstractFactory(ABC):

    def CreateProduct_A(self) -> AbstractProductA:
        pass

    def CreateProduct_B(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):

    def CreateProduct_A(self)-> AbstractProductA:
        return ConcreteProduct_A1()
    
    def CreateProduct_B(self)-> AbstractProductB:
        return ConcreteProduct_B1()

class ConcreteFactory2(AbstractFactory):

    def CreateProduct_A(self)-> AbstractProductA:
        return ConcreteProduct_A2()
    
    def CreateProduct_B(self)-> AbstractProductB:
        return ConcreteProduct_B2()

class AbstractProductA(ABC):

    def useful_function_a(self) -> str:
        pass

class ConcreteProduct_A1(AbstractProductA):
    
    def useful_function_a(self)-> str:
        return "The result of the product A1."
    
class ConcreteProduct_A2(AbstractProductA):

    def useful_function_a(self)->str:
        return "The result of the product A2."
    
class AbstractProductB(ABC):

    def useful_function_b(self) -> str:
        pass

    def another_useful_function(self, collab: AbstractProductA) -> None:
        pass
    
class ConcreteProduct_B1(AbstractProductB):
    
    def useful_function_b(self)-> str:
        return "The result of the product B1"
    
    def another_useful_function(self,collab:AbstractProductA)->str:
        result = collab.useful_function_a()
        return f"The result of the B1 collaboratiing with the {result}"
    
class ConcreteProduct_B2(AbstractProductB):
    def useful_function_b(self)-> str:
        return "The reusltof the product B2"
    
    def another_useful_function(self,collab:AbstractProductA)->str:
        result = collab.useful_function_a()
        return f"The result of the B2 collaborating with the {result}"
    

def client_code(factory:AbstractFactory)->None:

    product_a = factory.CreateProduct_A()
    product_b = factory.CreateProduct_B()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function(product_a)}",end ="")

print("Client:Testing the client code with the first factory type:")
client_code(ConcreteFactory1())

print("\n")

print("Client:Testing the same client code with the second factory type:")
client_code(ConcreteFactory2())
