Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import random
admin_keys = {"Saroj": "Saroj@2022"}

inven = {}


def add_new_item():
    itemname = input("Enter the Item name: ")
    itemid = random.randint(1,1000)
    price = int(input("Enter the price of the item: "))
    stock = int(input("Enter amount left in stock in the restaurant: "))
    quantity=int(input("Enter the quantity of the item:"))
    discount=float(input("enter the discout for this item:")
    inven[itemid] = {
        "ItemName": itemname,
        "ItemID": itemid,
        "Price": price,
        "Stock": stock,
        "Quantity":quantity
        "Discount":discount
    }
    print("The Item"+itemname+ "is successfully added")
    return inven


def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the price of item"))
    d = int(input("Enter the stock of the item"))
    e= quantity=int(input("Enter the quantity of the item:"))
    f=discount=float(input("enter the discout for this item:")
    inven[item]["ItemName"] = a
    inven[item]["Price"] = b
    inven[item]["Stock"] = d
    inven[item]["Quantity"]=e
    inven[item]["Discount"]=f
    print("*****Edited item successfully*****")
    return inven

def show_inven():
    print("*****HERE IS THE INVENTORY OF RAKSHAK MART*****")
    for i in inven:
        print("Item Name: ",inven[i]["ItemName"])
        print("Price: ",inven[i]["Price"],"INR")
        print("Item ID: ",inven[i]["ItemID"])
        print("Quantity:", inven[i]["Quantity"])
        print("discount:", inven[i]["Discount"])

def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    inven.pop(d)
    print("Remove item successfully ")
    return inven