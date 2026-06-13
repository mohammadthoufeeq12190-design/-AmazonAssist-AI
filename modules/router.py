def route_query(query):

    query = query.lower()

    if any(word in query for word in [
        "track",
        "order",
        "status"
    ]):
        return "tracking"

    elif any(word in query for word in [
        "recommend",
        "product",
        "buy",
        "laptop",
        "phone",
        "mobile",
        "electronics"
    ]):
        return "recommendation"

    elif any(word in query for word in [
        "coupon",
        "offer",
        "offers",
        "discount",
        "discounts"
    ]):
        return "coupon"

    elif any(word in query for word in [
        "return",
        "refund"
    ]):
        return "return"

    else:
        return "general"