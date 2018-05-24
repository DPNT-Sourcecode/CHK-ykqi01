# Our price table and offers: 
# +------+-------+---------------------------------+
# | Item | Price | Special offers                  |
# +------+-------+---------------------------------+
# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | C    | 20    |                                 |
# | D    | 15    |                                 |
# | E    | 40    | 2E get one B free               |
# | F    | 10    | 2F get one F free               |
# | G    | 20    |                                 |
# | H    | 10    | 5H for 45, 10H for 80           |
# | I    | 35    |                                 |
# | J    | 60    |                                 |
# | K    | 70    | 2K for 120                      |
# | L    | 90    |                                 |
# | M    | 15    |                                 |
# | N    | 40    | 3N get one M free               |
# | O    | 10    |                                 |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | R    | 50    | 3R get one Q free               |
# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |
# | W    | 20    |                                 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
# +------+-------+---------------------------------+

from collections import Counter


prices = {
    "A": 50,    # 3A for 130, 5A for 200          |
    "B": 30,    # 2B for 45                       |
    "C": 20,    #                                 |
    "D": 15,    #                                 |
    "E": 40,    # 2E get one B free               |
    "F": 10,    # 2F get one F free               |
    "G": 20,    #                                 |
    "H": 10,    # 5H for 45, 10H for 80           |
    "I": 35,    #                                 |
    "J": 60,    #                                 |
    "K": 70,    # 2K for 120                      |
    "L": 90,    #                                 |
    "M": 15,    #                                 |
    "N": 40,    # 3N get one M free               |
    "O": 10,    #                                 |
    "P": 50,    # 5P for 200                      |
    "Q": 30,    # 3Q for 80                       |
    "R": 50,    # 3R get one Q free               |
    "S": 20,    # buy any 3 of (S,T,X,Y,Z) for 45 |
    "T": 20,    # buy any 3 of (S,T,X,Y,Z) for 45 |
    "U": 40,    # 3U get one U free               |
    "V": 50,    # 2V for 90, 3V for 130           |
    "W": 20,    #                                 |
    "X": 17,    # buy any 3 of (S,T,X,Y,Z) for 45 |
    "Y": 20,    # buy any 3 of (S,T,X,Y,Z) for 45 |
    "Z": 21,    # buy any 3 of (S,T,X,Y,Z) for 45 |
}


def apply_freebie(products):
    freebies = {
        "E": (2, "B"),
        "F": (3, "F"),
        "N": (3, "M"), 
        "R": (3, "Q"),
        "U": (4, "U"),
    }
    for sku, rule in freebies.items():
        counter = products.get(sku)
        if not counter:
            continue
        freebie = int(products[sku] / rule[0])
        freebie_count = products.get(rule[1])
        if freebie_count:
            products[rule[1]] -= freebie
            if products[rule[1]] < 0:
                products[rule[1]] = 0
    return products

def apply_bulk_discount(products):
    offers = {
        "A": [(5, 50), (3, 20)],
        "B": [(2, 15)],
        "H": [(10, 20), (5, 5)],
        "K": [(2, 20)],
        "P": [(5, 50)],
        "Q": [(3, 10)],
        "V": [(3, 20), (2, 10)],
    }
    mixed_offers = [
        ("Z", 6), 
        ("S", 5),
        ("T", 5),
        ("Y", 5),
        ("X", 2),
    ]
    total = 0
    for product, count in products.items():
        if product not in prices:
            raise ValueError("invalid product")
        total += (prices[product] * count) 
        offer = offers.get(product)
        if offer:
            for each in offer:
                counter = int(count / each[0])
                discount = counter * each[1]
                total -= discount
                count -= counter * each[0]
            products[product] = count

    mixed_offers_counter = sum([products[p] for (p, _) in mixed_offers])
    cutoff = mixed_offers_counter % 3
    if mixed_offers_counter > 2:
        for mixed_offer, mixed_offer_discount in mixed_offers:
            if products.get(mixed_offer) > 0:
                for _ in range(products[mixed_offer]):
                    mixed_offers_counter -= 1
                    if mixed_offers_counter < cutoff:
                        break
                    total -= mixed_offer_discount

    return products, total

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    products = Counter(skus)

    products = apply_freebie(products)
    products, total = apply_bulk_discount(products)
    print(products, total)


    return total

def run():
    for t in ["SSSZ", "ZZZS", "STXS", "STX"]:
        print(t, checkout(t))