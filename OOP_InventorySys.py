# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def Area(self):
#         return round(math.pi * self.radius ** 2, 5)

#     def Circumference(self):
#         return round(2 * math.pi * self.radius, 5)

# radius = int(input("Enter value: "))

# c1 = Circle(radius)
# print("Area: ", c1.Area())
# print("Parameter: ", c1.Circumference())

## +++++++++++++++++++++++++++++++++++++++++++++++
# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def DisplayDetail(self):
#         print("\n", "="*5, "Employee Detail", "="*5)
#         print("Employee Job Type: ", self.role)
#         print("Employee Department: ", self.department)
#         print("Employee Salary: ", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__(Role, Department, Salary)


# Role = input("Enter job type: ").capitalize().strip()
# Department = input("Enter employee department: ").capitalize().strip()
# Salary = input("Enter employee salary: ").capitalize().strip()
# e1 = Employee(Role, Department, Salary)
# e2 = Engineer("Hamza", "19")
# e2.DisplayDetail()
# print(e2.name)


## +++++++++++++++++++++++++++++++++++++
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, odr2):
#         return self.price > odr2.price

# odr = input("Enter your order: ").capitalize().strip()
# cost= int(input("Enter your order price: ").strip())
# o1 = Order(odr, cost)
# odr = input("Enter your order: ").capitalize().strip()
# cost = int(input("Enter your order price: ").strip())
# o2 = Order(odr, cost)
# print(o1 > o2)

## ++++++++++++++++++++++++++++++++
# class InventorySystem:
#     def __init__(self):
#         self.stock = {"Water":[50, 10], "Chips":[30, 7], "Cola":[40, 4]}

#     def display_item(self):
#         print("Availble Items: ")
#         for item, (price, qty) in self.stock.items():
#             print(f"{item} - Rs. {price} ({qty} in stock)")


#     def buy_item(self, item_name, qty):
#         if item_name in self.stock:
#             price, availble_qty = self.stock[item_name]
#             if qty <= availble_qty:
#                 total_cost = price * qty
#                 self.stock[item_name][1] -= qty
#                 print(f"You bought {item_name}(s) in Rs. {total_cost}")

#             else:
#                 print(f"Sorry, onlt {availble_qty} {item_name}(s) in stock.")
#         else:
#             print(f"{item_name} is not availble today. in this machine")

# print("="*5, "Item List", "="*5)
# print("Water - Rs. 50 ")
# print("Chips - Rs. 30 ")
# print("Cola - Rs. 40 ")
# print("-"*20)
# inv = InventorySystem()
# print("")
# item_name = input("Enter an item to purchase: ").capitalize().strip()
# qty = int(input(f"Enter quantity of {item_name} : ").strip())
# inv.buy_item(item_name, qty)
# print("\nUpdated Inventory: ")
# inv.display_item()


## +++++++++++++++++++++++++++++++++++

# store = {
#     "Tomato": {"price": 40, "stock": 100, "category": "Vegetable", "discount": 5},
#     "Potato": {"price": 30, "stock": 80, "category": "Vegetable"},
#     "Apple": {"price": 120, "stock": 50, "category": "Fruit", "discount": 10},
#     "Banana": {"price": 20, "stock": 60, "category": "Fruit"},
# }


# print("-: Menu :-")
# for item_name, detail in store.items():
#     print(
#         f"{item_name} - Rs.{detail['price']} ({detail['stock']} in stock) | {detail['category']}"
#     )

# user_input = input("Enter your item name to buy: ").capitalize().strip()
# if user_input in store:
#     quantity = int(input(f"Enter quantity of '{user_input}': ").strip())
#     avaible_stock = store[user_input]["stock"]

#     if quantity <= avaible_stock:
#         total_cost = store[user_input]["price"] * quantity
#         store[user_input]["stock"] -= quantity

#         print(f"You bought {quantity} {user_input}(s) in Rs.{total_cost}")
#         print(f"Remaining only {user_input}: {store[user_input]['stock']} ")

#         if "discount" in store[user_input]:
#             discount = store[user_input]["discount"]
#             discount_amount = (total_cost * discount) / 100
#             final_cost = total_cost - discount_amount

#             print(f"Discount Amount: {discount_amount}")
#             print(f"Grand Total: {final_cost}")

#         else:
#             print("No discount. ")

#     else:
#         print(f"Sorry! only available {avaible_stock} in stock.")

# else:
#     print("Item not found.")

# ++++++++++++++++++++++++
# Fruit = {
#     "Apple":{"price":40, "stock":20 , "discount": 10 },
#     "Banana":{"price":30, "stock":60 , "discount": 6 },
#     "Gava":{"price":50, "stock":50 , "discount": 8 },
#     "Date":{"price":40, "stock":80  }
# }

# Vegetable = {
#     "Carrot":{"price":40, "stock":20 , "discount": 10},
#     "Lady finger":{"price":30, "stock":60 , "discount": 4 },
#     "Chilli":{"price":50, "stock":50 , "discount": 8 },
#     "Lemon":{"price":40, "stock":80 , "discount": 6}
# }

# category_option = input("\nWhat would you like to buy? (Fruit/Vegetable): ").capitalize().strip()
# if category_option in ["Fruit", "Vegetable"]:
#     selected_category = Fruit if category_option == "Fruit" else Vegetable

#     for item_name, detail in selected_category.items():

#         print(f"{item_name} - Rs.{detail['price']} ({detail['stock']} in stocks)")

#     user_input = input("\nEnter item name from above list to buy: ").capitalize().strip()
#     if user_input in selected_category:
#         quantity = int(input(f"Enter quantity of '{user_input}': ").strip())
#         availble_stock = selected_category[user_input]['stock']

#         if quantity <= availble_stock:
#             total_cost = selected_category[item_name]['price'] * quantity
#             selected_category[user_input]['stock'] -= quantity

#             print(f"You bought {quantity} {user_input}(s) in Rs.{total_cost} ")
#             print(f"Remaining {selected_category[user_input]['stock']} {user_input}(s) in store.")


#             if "discount" in selected_category[user_input]:
#                 discount = selected_category[user_input]["discount"]

#                 discount_amount = (total_cost * discount)/100
#                 final_cost = total_cost - discount_amount

#                 print(f"\nDiscount Amount: {discount_amount}")
#                 print(f"Grand Total: {final_cost}")
#             else:
#                 print("No discount. ")

#         else:
#             print(f"Sorry! only {availble_stock} {item_name} in stock. ")
#     else:
#         print("Item not found. ")


# else:
#     print("Item not found.")


# +++++++++++++++++++++++++++++++++++++++++

class IventorySystem:
    def __init__(self):

        self.Fruit = {
            "Apple": {"price": 60, "stock": 90, "discount": 20},
            "Banana": {"price": 50, "stock": 60, "discount": 10},
            "Gava": {"price": 40, "stock": 50},
            "Peach": {"price": 90, "stock": 120, "discount": 15},
        }
        self.Vegetable = {
            "Carrot": {"price": 60, "stock": 90, "discount": 20},
            "Chilli": {"price": 50, "stock": 60, "discount": 10},
            "Lemon": {"price": 40, "stock": 50},
            "Cucumber": {"price": 90, "stock": 120, "discount": 15},
        }

    def display(self):
        while True:
            category_option = input("Enter category (Fruit/Vegetable): ").capitalize().strip()
            if category_option.lower().strip() == "exit":
                print("Exiting. Thank for shopping!")
                break
            category_option = category_option.title()
            if category_option in ["Fruit", "Vegetable"]:
                selected_category = self.Fruit if category_option == "Fruit" else self.Vegetable

                for item_name, detail in selected_category.items():
                    print(f"{item_name} - Rs. {detail['price']} ({detail['stock']} in stock.)")

                user_input = input("\nEnter item to buy from above list: ").capitalize().strip()
                if user_input in selected_category:

                    quantity = int(input(f"Enter quantity of '{user_input}': ").strip())
                    available_stock = selected_category[user_input]['stock']

                    if quantity <= available_stock:
                        total_cost = selected_category[user_input]['price'] * quantity
                        selected_category[user_input]['stock'] -= quantity

                        print(f"You bought {quantity} {user_input}(s) in Rs. {total_cost}")
                        print(f"Remining only {selected_category[user_input]['stock']} {user_input} in stock.")

                        if "discount" in selected_category[user_input]:
                            discount = selected_category[user_input]["discount"]

                            discount_amount = (total_cost * discount)/ 100
                            final_cost = total_cost - discount_amount

                            print(f"Discount Amount: {discount_amount}")
                            print(f"Grand Total: {final_cost}")
                        else:
                            print("Sorry! No discount.")

                    else:
                        print("Sorry! Quantity not availble. ")

                else:
                    print("Not found.")

            else:
                print("Select category not found in list. ")

m1 = IventorySystem()
m1.display()
