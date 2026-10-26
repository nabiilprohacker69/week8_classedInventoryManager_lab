
##responsible for product data. ie. uppdating stock and displaying product information.

class Product:

    def __init__(self, product):
        self.__product_id = product["ID"]
        self.__product_name = product["Name"]
        self.__product_price = product["Price"]
        self.__product_stock = product["Stock"]

    def __display_product_info__(self):
        print(f"ID: {self.__product_id} | Name: {self.__product_name} | Price: {self.__product_price} | Stock: {self.__product_stock}")
