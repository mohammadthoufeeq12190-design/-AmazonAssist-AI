from modules.router import route_query
from modules.recommendation import recommend_products
from modules.order_tracking import track_order
from modules.coupons import get_coupons

from modules.retrieval import search_documents
from modules.gemini_ai import generate_answer


def chatbot(query, last_product=None):

    intent = route_query(query)

    # Recommendation
    if intent == "recommendation":

        products = recommend_products("Electronics")

        laptop = products[
            products["name"].str.contains(
                "Laptop",
                case=False,
                na=False
            )
        ]

        if len(laptop) > 0:

            product = laptop.iloc[0]

            response = f"""
Recommended Product

Name: {product['name']}
Brand: {product['brand']}
Price: ₹{product['price']}
Rating: ⭐ {product['rating']}
"""

            return response, product.to_dict()

        return products.to_string(index=False), None

    # Memory
    if "price" in query.lower() and last_product:

        return (
            f"The price of {last_product['name']} is ₹{last_product['price']}.",
            last_product
        )

    # Tracking
    elif intent == "tracking":

        if "ord001" in query.lower():
            return track_order("ORD001"), None

        elif "ord002" in query.lower():
            return track_order("ORD002"), None

        elif "ord003" in query.lower():
            return track_order("ORD003"), None

        elif "ord004" in query.lower():
            return track_order("ORD004"), None

        elif "ord005" in query.lower():
            return track_order("ORD005"), None

        return "Please provide Order ID.", None

    # Coupons
    elif intent == "coupon":

        return get_coupons(), None

    # RAG + Gemini
    results = search_documents(query)

    context = ""

    for doc in results:
        context += doc.page_content + "\n"

    return generate_answer(context, query), None