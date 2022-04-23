food_item = {"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.00, "Milk": 2.50}

BTS_age = {"Jimin": 26, "Jungkook": 24, "Jin": 29, "J-hope": 28, "RM": 27, "V": 24, "Suga": 29}

Chicken_price = food_item["Chicken"]
Beef_price = food_item["Beef"]
Cheese_price = food_item["Cheese"]
Milk_price = food_item["Milk"]

print(Chicken_price, Beef_price, Cheese_price, Milk_price)

Jimin_age = BTS_age["Jimin"]
Jungkook_age = BTS_age["Jungkook"]
Jin_age = BTS_age["Jin"]
Jhope_age = BTS_age["J-hope"]
RM_age = BTS_age["RM"]
V_age = BTS_age["V"]
Suga_age = BTS_age["Suga"]

print(Jimin_age, Jungkook_age, Jin_age, Jhope_age, RM_age, V_age, Suga_age)

shoe_brand_stock = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

shoe_brand_stock["SB Dunk"] -= 2
shoe_brand_stock["Yeezy"] += 1
shoe_brand_stock["Jordan 13"] += 7
shoe_brand_stock["Yeezy"] += 7
shoe_brand_stock["Foamposite"] += 7
shoe_brand_stock["Air Max"] += 7
shoe_brand_stock["SB Dunk"] += 7

shoe_brand_stock["Jordan 13"] -= 3
shoe_brand_stock["Yeezy"] -= 3
shoe_brand_stock["Foamposite"] -= 3
shoe_brand_stock["Air Max"] -= 3
shoe_brand_stock["SB Dunk"] -= 3

print(shoe_brand_stock["Jordan 13"])
print(shoe_brand_stock["Yeezy"])
print(shoe_brand_stock["Foamposite"])
print(shoe_brand_stock["Air Max"])
print(shoe_brand_stock["SB Dunk"])

shoe_brand_stock["Nike"] = 5
shoe_brand_stock["Adidas"] = 3
shoe_brand_stock["Vans"] = 7

print(shoe_brand_stock["Nike"])
print(shoe_brand_stock["Adidas"])
print(shoe_brand_stock["Vans"])

del shoe_brand_stock["Nike"]
del shoe_brand_stock["Adidas"]

print(shoe_brand_stock["Jordan 13"])
print(shoe_brand_stock["Yeezy"])
print(shoe_brand_stock["Foamposite"])
print(shoe_brand_stock["Air Max"])
print(shoe_brand_stock["SB Dunk"])
print(shoe_brand_stock["Vans"])



