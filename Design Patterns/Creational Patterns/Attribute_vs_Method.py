class MyClass:
    def __init__(self):
        self._product = None

    # Using methods
    def get_product(self):
        return self._product

    def set_product(self, value):
        self._product = value

    # Using properties
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value

# Creating an instance of MyClass
obj = MyClass()

# Using methods
obj.set_product("Product A")
print("Using methods - Get product:", obj.get_product())  # Output: Using methods - Get product: Product A

# Using properties
obj.product = "Product B"  # This calls the product setter method
print("Using properties - Product:", obj.product)  # Output: Using properties - Product: Product B
