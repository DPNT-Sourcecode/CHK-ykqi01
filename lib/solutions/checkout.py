# Our price table and offers: 
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+

from collections import Counter

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
}

offers = {
    "A": [(5, 50), (3, 20)],
    "B": [(2, 15)],
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    products = Counter(skus)
    total = 0

    if products.get("E") > 1:
        freebie = int(products["E"] / 2)
        b_count = products.get("B")
        if b_count:
            products["B"] -= freebie

    if products.get("F") > 2:
        freebie = int(products["F"] / 3)
        products["F"] -= freebie

    for product, count in products.iteritems():
        if product not in prices:
            return -1

        total += (prices[product] * count) 
        offer = offers.get(product)
        if offer:
            for each in offer:
                counter = int(count / each[0])
                discount = counter * each[1]
                total -= discount
                count -= counter * each[0]
    
    return total