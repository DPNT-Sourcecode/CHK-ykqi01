# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


# Notes: 
#  - For any illegal input return -1

# In order to complete the round you need to implement the following method:
#      checkout(String) -> Integer

# Where:
#  - param[0] = a String containing the SKUs of all the products in the basket
#  - @return = an Integer representing the total checkout value of the items 

from collections import Counter

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

offers = {
    "A": (3, 20),
    "B": (2, 15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    products = Counter(skus)
    total = 0

    for product, count in products.iteritems():
        if product not in prices:
            return -1

        total += (prices[product] * count) 
        offer = offers.get(product)
        if offer:
            discount = int(count / offers[product][0]) * offers[product][1]
            total -= discount 
    
    return total



