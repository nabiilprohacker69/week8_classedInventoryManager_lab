import json
import os
from product import Product


def data_representation():
    print("==================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==================================================\n")

    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            print("inventory.json found")
            print("Inventory loaded successfully.\n")

       # with open("inventory.json", "r") as file: #read the file and print the data
       #     data = json.load(file)
       #     print(data)
    else:
        print("inventory.json not found. Creating a new inventory file...")
        with open("inventory.json", "w") as file:
            json.dump([
    {
        "ID": "P001",
        "Name": "Laptop",
        "Price": "$1200",
        "Stock": 50
    },
    {
        "ID": "P002",
        "Name": "Mouse",
        "Price": "$25.50",
        "Stock": 30
    },
    {
        "ID": "P003",
        "Name": "Keyboard",
        "Price": "$45.00",
        "Stock": 20
    }], file)
            print("New inventory file created successfully.\n")

    print("--------------MENU---------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------\n")

def options():
    user_input = input("Enter Option: ")

    if user_input == "1":
        option_1()
    elif user_input == "2":
        option_2()
    elif user_input == "3":
        option_3()
    elif user_input == "4":
        option_4()
    elif user_input == "5":
        option_5()
    elif user_input == "6":
        print("Thank you for usingInventory Management System.\nProgram terminated.")

def option_1():
    with open("inventory.json", "r") as file:
            inventory = json.load(file)
            for product in inventory:
                Product(product).__display_product_info__() ##Product(product) converts initial product dictionary into a Product object

def option_2():
    pass
def option_3():
    pass
def option_4():
    pass
def option_5():
    pass

data_representation()
options()