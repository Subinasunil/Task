def calculate_discount(quantity, total_quantity, total_amount):
    discount = 0
    discount_name = ""

    if total_amount > 200:
        discount = min(10, total_amount)
        discount_name = "flat_10_discount"
    elif quantity > 10:
        discount = min(0.05 * total_amount, total_amount)
        discount_name = "bulk_5_discount"
    elif total_quantity > 20:
        discount = min(0.1 * total_amount, total_amount)
        discount_name = "bulk_10_discount"
    elif total_quantity > 30 and quantity > 15:
        discount = min((quantity - 15) * 0.5 * total_amount, total_amount)
        discount_name = "tiered_50_discount"

    return discount, discount_name


def calculate_fees(quantity):
    gift_wrap_fee = quantity
    shipping_fee = (quantity // 10) * 5

    return gift_wrap_fee, shipping_fee


def calculate_total(products):
    subtotal = 0
    total_quantity = 0
    total_discount = 0
    gift_wrap_fee = 0
    shipping_fee = 0

    for product in products:
        name = product[0]
        quantity = product[1]
        price = product[2]
        is_gift_wrapped = product[3]

        total_quantity += quantity
        total_amount = price * quantity

        discount, discount_name = calculate_discount(quantity, total_quantity, total_amount)
        total_discount += discount

        gift_wrap, shipping = calculate_fees(quantity)
        if is_gift_wrapped:
            gift_wrap_fee += gift_wrap
        shipping_fee += shipping

        subtotal += total_amount

        print(f"Product: {name}\nQuantity: {quantity}\nTotal Amount: ${total_amount}\n")

    print(f"Subtotal: ${subtotal}\n")

    if total_discount > 0:
        print(f"Discount Applied: {discount_name}\nDiscount Amount: ${total_discount}\n")

    print(f"Gift Wrap Fee: ${gift_wrap_fee}\nShipping Fee: ${shipping_fee}\n")

    total = subtotal - total_discount + gift_wrap_fee + shipping_fee
    print(f"Total: ${total}")


# Example usage
products = [
    ("Product A", 2, 20, False),
    ("Product B", 12, 40, True),
    ("Product C", 8, 50, False)
]

calculate_total(products)