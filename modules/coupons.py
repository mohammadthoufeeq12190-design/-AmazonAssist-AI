import pandas as pd

def get_coupons():

    df = pd.read_csv("data/coupons.csv")

    response = "🎁 Available Coupons\n\n"

    for _, row in df.iterrows():

        response += (
            f"Coupon: {row['coupon_code']}\n"
            f"Discount: {row['discount']}\n"
            f"Minimum Order: ₹{row['minimum_order']}\n\n"
        )

    return response