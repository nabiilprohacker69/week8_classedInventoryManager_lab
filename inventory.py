
##responsible for add, search, displaying all data

import json
from product import Product


class Inventory:

    def __init__(self, inventory):
        self.__inventory = inventory

    def __display_all__(self):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            for product in inventory:
                Product(product).__display_product_info__() ##Product(product) converts initial product dictionary into a Product object

    def __add_product__(self, product_id, product_name, product_price, product_stock):
        print("Add New Product")
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        
            new_product = {
                "ID": product_id,
                "Name": product_name,
                "Price": product_price,
                "Stock": product_stock
            }
        
            inventory.append(new_product)
        
            with open("inventory.json", "w") as file:
                json.dump(inventory, file, indent=4)
        
            print("Product added successfully.\n")

    def __update_product__(self, new_stock_quantity,product_id):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        
            for product in inventory:
                if product["ID"] == product_id:
                    product["Stock"] = int(new_stock_quantity)

                    with open("inventory.json", "w") as file:
                     json.dump(inventory, file, indent=4)

                    print("Stock updated successfully!\n")
                    return True

    def __search_product__(self, product_id):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        for product in inventory:
            if product["ID"] == product_id:
                print("\nProduct Found")
                print("---------------------------------")
                print(f"ID: {product['ID']} | Name: {product['Name']} | Price: {product['Price']} | Stock: {product['Stock']}")
                print("---------------------------------\n")
            
                return product
        print("Product ID not found.\n")
        return None