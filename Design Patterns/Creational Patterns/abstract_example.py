from __future__ import annotations
from abc import ABC

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

###########################################################################################
"""
ABSTRACT CLASS FOR AbstractFactory
"""

class AbstractFactory(ABC):

    def CreateChair(self)->AbstractChair:
        pass

    def CreateCoffeeTable(self)->AbstractCoffeeTable:
        pass

    def CreateSofa(self)->AbstractSofa:
        pass

###########################################################################################

"""
Concrete CLASS FOR ConcreteFactory
"""

class VictorianFurnitureFactory(AbstractFactory):

    def CreateChair(self) -> AbstractChair:
        return VictorianChairProduct()
    
    def CreateCoffeeTable(self) -> AbstractCoffeeTable:
        return VictorianCoffeeProduct()
    
    def CreateSofa(self) -> AbstractSofa:
        return VictorianCreateSofa()
    
class ModernFurnitureFactory(AbstractFactory):
    def CreateChair(self) -> AbstractChair:
        return ModernChairProduct()
    
    def CreateCoffeeTable(self) -> AbstractCoffeeTable:
        return ModernCoffeeProduct()
    
    def CreateSofa(self) -> AbstractSofa:
        return ModernCreateSofa()

###########################################################################################
"""
ABSTRACT CLASS FOR AbstractChair
"""

class AbstractChair:

    def chair_function(self)->str:
        pass

###########################################################################################

class VictorianChairProduct(AbstractChair):

    def chair_function(self) -> str:
        return "Victorian Chair"

class ModernChairProduct(AbstractChair):

    def chair_function(self) -> str:
        return "Modern Chair"
    
###########################################################################################
"""
ABSTRACT CLASS FOR AbstractCoffeeTable
"""

class AbstractCoffeeTable:

    def coffeetable_function(self)->str:
        pass

    def another_coffee_table_function(self,collab:AbstractChair)->str:
        pass
        
###########################################################################################
class VictorianCoffeeProduct(AbstractCoffeeTable):

    def coffeetable_function(self) -> str:
        return "Victorian Coffee"
    
    def another_coffee_table_function(self, collab: AbstractChair) -> str:
        result = collab.chair_function()
        return f"Victorian Coffee table is to be bought with {result}"

class ModernCoffeeProduct(AbstractCoffeeTable):

    def coffeetable_function(self) -> str:
        return "Modern Coffee"
    
    def another_coffee_table_function(self, collab: AbstractChair) -> str:
        result = collab.chair_function()
        return f"Modern Coffee table is to be bought with {result}"

###########################################################################################
"""
ABSTRACT CLASS FOR AbstractSofa
"""

class AbstractSofa:

    def sofa_function(self)->str:
        pass

    def another_sofa_function(self,collab:AbstractCoffeeTable)->str:
        pass

        
###########################################################################################
    
class VictorianCreateSofa:

    def sofa_function(self)->str:
        return "Victorian Sofa"
    
    def another_sofa_function(self,collab:AbstractCoffeeTable)->str:
        result = collab.sofa_function()
        return f"Victorian sofa is to be bought with {result}"

class ModernCreateSofa:

    def sofa_function(self)->str:
        return "Modern Sofa"
    
    def another_sofa_function(self,collab:AbstractCoffeeTable)->str:
        result = collab.sofa_function()
        return f"Modern sofa is to be bought with {result}"

###########################################################################################
    
def client_code(factory: AbstractFactory) -> None:

    product_a = factory.CreateChair()
    product_b = factory.CreateCoffeeTable()
    product_c = factory.CreateSofa()

    print(product_a.chair_function())
    print(product_b.another_coffee_table_function(product_a))
    print(product_c.sofa_function())


print("Client: I want everything from VictoriaFurniture")
client_code(VictorianFurnitureFactory())
print("\n")

print("Client: I want everything from ModernFurniture")
client_code(ModernFurnitureFactory())



