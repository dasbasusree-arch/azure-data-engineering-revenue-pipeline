import csv

total_order_value = {}

# Step 1: Read paid orders only
paid_orders = set()

with open("data/orders.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["status"] == "PAID":
            paid_orders.add(row["order_id"])

# Step 2: Calculate value for paid orders
with open("data/order_items.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        order_id = row["order_id"]

        if order_id in paid_orders:
            quantity = int(row["quantity"])
            unit_price = float(row["unit_price"])

            item_value = quantity * unit_price

            if order_id not in total_order_value:
                total_order_value[order_id] = 0

            total_order_value[order_id] += item_value

# Step 3: Print results
for order_id, amount in total_order_value.items():
    print(f"Order {order_id}: Rs. {amount:,.2f}")
