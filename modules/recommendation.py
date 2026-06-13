import pandas as pd

def recommend_products(category=None):

    df = pd.read_csv("data/products.csv")

    if category:
        products = df[
            df["category"].str.lower() == category.lower()
        ]
    else:
        products = df

    return products[[
        "name",
        "brand",
        "price",
        "rating"
    ]]