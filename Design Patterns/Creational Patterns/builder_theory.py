from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):

    def product(self) -> None:
        pass

    def product_part_a(self) -> None:
        pass

    def produce_part_a(self) -> None:
        pass

    def produce_part_b(self) -> None:
        pass

    def produce_part_c(self) -> None:
        pass

class ConcreteBuilder(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self,part:Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(f"Product parts: {','.join(self.parts)}",end = "")


class Director:

    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self,builder:Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__=="__main__":

    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("Standard Basic Product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured Product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom Product:")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()