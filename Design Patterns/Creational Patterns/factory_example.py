from __future__ import annotations
from abc import ABC,abstractmethod


"""
                Product p = createProduct()
                p.doStuff()
                    |
                    |-----------------------           Transport
                                                + someOperation()          ---------------->  Product(interface)
                                                + createProduct():Product                     + doStuff()
                                                        |                                            |
                                                        |                                            |
                                        ----------------|----------------                            |
                                        |                               |                    ---------------------
                                        |                               |                    |                   |
                                        |                               |                    TruckProduct   ShipProduct
                                TruckTransport                     ShipTransport
                        + createProduct():TruckProduct       + createProduct():ShipProduct
                                        
                                        
                                        
    """                  

# Interface for the product creation
class Transport(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"{product.operation()}"
        return result

# Another interface for the product
class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass

# Concrete implementation of Transport for truck delivery
class TruckTransport(Transport):
    def factory_method(self) -> Product:
        return TruckProduct()

# Concrete implementation of Transport for ship delivery
class ShipTransport(Transport):
    def factory_method(self) -> Product:
        return ShipProduct()

# Concrete implementation of Product for truck delivery
class TruckProduct(Product):
    def operation(self) -> str:
        return 'Land'

# Concrete implementation of Product for ship delivery
class ShipProduct(Product):
    def operation(self) -> str:
        return 'Sea'

# Client code to demonstrate the use of the Factory Method pattern
def client_code(creator: Transport) -> None:
    print(f"Client: I am not sure but the food is transported by \n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with Truck Delivery")
    client_code(TruckTransport())
    print("\n")

    print("App: Launched with Ship Delivery")
    client_code(ShipTransport())
    print("\n")


