
# Restaurant Menu & Order Management System


import copy
from collections import Counter



menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}



# TASK 1 — Explore Menu


print("\n====== MENU ======")

categories = set(item["category"] for item in menu.values())

for category in categories:
    print(f"\n===== {category} =====")

    for item, info in menu.items():
        if info["category"] == category:
            status = "Available" if info["available"] else "Unavailable"
            print(f"{item}  ₹{info['price']:.2f}  [{status}]")

# statistics
print("\nMENU STATISTICS")

total_items = len(menu)

available_items = sum(1 for i in menu.values() if i["available"])

most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

under_150 = [item for item, info in menu.items() if info["price"] < 150]

print("Total items:", total_items)
print("Available items:", available_items)
print("Most expensive:", most_expensive[0], most_expensive[1]["price"])
print("Items under ₹150:", under_150)


# TASK 2 — Cart Operations

cart = []


def add_item(item_name, qty):

    if item_name not in menu:
        print("Item not on menu")
        return

    if not menu[item_name]["available"]:
        print("Item unavailable")
        return

    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += qty
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return

    cart.append({
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]
    })


def remove_item(item_name):

    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name}")
            return

    print("Item not in cart")


def update_quantity(item_name, qty):

    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = qty
            return

    print("Item not found")


# simulate actions
print("\nCART OPERATIONS")

add_item("Paneer Tikka",2)
print(cart)

add_item("Gulab Jamun",1)
print(cart)

add_item("Paneer Tikka",1)
print(cart)

add_item("Mystery Burger",1)

add_item("Chicken Wings",1)

remove_item("Gulab Jamun")
print(cart)

# order summary
print("\n========== ORDER SUMMARY ==========")

subtotal = 0

for item in cart:
    total = item["quantity"] * item["price"]
    subtotal += total
    print(f"{item['item']}  x{item['quantity']}  ₹{total:.2f}")

gst = subtotal * 0.05
total = subtotal + gst

print("--------------------------------")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total:.2f}")


# TASK 3 — Inventory Tracker

print("\nINVENTORY CHECK")

inventory_backup = copy.deepcopy(inventory)

# modify inventory to demonstrate deep copy
inventory["Paneer Tikka"]["stock"] -= 5

print("Inventory:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

# restore inventory
inventory = copy.deepcopy(inventory_backup)

# deduct stock from cart
for item in cart:

    name = item["item"]
    qty = item["quantity"]

    if inventory[name]["stock"] < qty:
        print("Low stock for", name)
        qty = inventory[name]["stock"]

    inventory[name]["stock"] -= qty

# reorder alerts
print("\nREORDER ALERTS")

for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print("Reorder needed:", item)


# TASK 4 — Sales Log Analysis


print("\nSALES ANALYSIS")

revenue_per_day = {}

for day, orders in sales_log.items():

    revenue = sum(o["total"] for o in orders)
    revenue_per_day[day] = revenue

    print(day, "Revenue:", revenue)

best_day = max(revenue_per_day, key=revenue_per_day.get)

print("\nBest selling day:", best_day)

# most ordered item
items = []

for orders in sales_log.values():
    for order in orders:
        items.extend(order["items"])

most_common = Counter(items).most_common(1)[0]

print("Most ordered item:", most_common[0])


# add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken","Gulab Jamun","Garlic Naan"], "total": 450},
    {"order_id": 12, "items": ["Paneer Tikka","Rasgulla"], "total": 260}
]

print("\nALL ORDERS")

count = 1

for date, orders in sales_log.items():

    for order in orders:

        print(
            f"{count}. [{date}] Order #{order['order_id']} "
            f"- ₹{order['total']} - Items: {', '.join(order['items'])}"
        )

        count += 1