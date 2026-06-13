from modules.router import route_query

print("Track my order ->", route_query("Track my order"))

print("Track ORD001 ->", route_query("Track ORD001"))

print("Recommend a laptop ->", route_query("Recommend a laptop"))

print("Recommend products under ₹10,000 ->", route_query("Recommend products under ₹10,000"))

print("What is the refund policy? ->", route_query("What is the refund policy?"))