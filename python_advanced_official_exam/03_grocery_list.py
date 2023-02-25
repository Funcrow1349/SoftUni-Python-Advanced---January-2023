def shop_from_grocery_list(budget, grocery_list, *products_and_prices):
    money_left = budget
    products_left = grocery_list

    for product, price in products_and_prices:
        if product in grocery_list:
            if price <= money_left:
                money_left -= price
                products_left.remove(product)
            else:
                break

    if not products_left:
        return f"Shopping is successful. Remaining budget: {money_left:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(products_left)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
