import pandas as pd

def track_order(order_id):

    df = pd.read_csv("data/orders.csv")

    result = df[df["order_id"] == order_id]

    if len(result) == 0:
        return "Order not found."

    order = result.iloc[0]

    return f"""
📦 Order Details

Order ID: {order['order_id']}
Customer: {order['customer_name']}
Product: {order['product_name']}
Status: {order['status']}
Payment Method: {order['payment_method']}
"""