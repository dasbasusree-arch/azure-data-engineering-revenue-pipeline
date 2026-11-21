import csv

total_order_value = {}

# Read order items
with open("data/order_items.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        order_id = row["order_id"]
        quantity = int(row["quantity"])
        unit_price = float(row["unit_price"])

        item_value = quantity * unit_price

        if order_id not in total_order_value:
            total_order_value[order_id] = 0

        total_order_value[order_id] += item_value

# Print order-wise totals
for order_id, amount in total_order_value.items():
    print(f"Order {order_id}: Rs. {amount:,.2f}")

