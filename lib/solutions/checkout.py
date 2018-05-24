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
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+

from collections import Counter

offers = {
    "A": [(5, 50), (3, 20)],
    "B": [(2, 15)],
    "H": [(10, 20), (5, 5)],
    "K": [(2, 10)],
    "P": [(5, 50)],
    "Q": [(3, 10)],
    "V": [(3, 20), (2, 10)],
}

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

freebies = {
    "E": (2, "B"),
    "F": (2, "F"),
    "N": (3, "M"), 
    "R": (3, "Q"),
    "U": (3, "U"),
}

def apply_freebie(products):
    for sku, rule in freebies.iteritems():
        counter = products.get(sku)
        if counter:
            freebie = int(products[sku] / rule[0])
            freebie_count = products.get(rule[1])
            if freebie_count:
                products[rule[1]] -= freebie
                if products[rule[1]] < 0:
                    products[rule[1]] = 0
    return products


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    products = Counter(skus)
    total = 0

    products = apply_freebie(products)

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