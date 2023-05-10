def apply_discount(price: int, discount: float = 0.0) -> int | str:
    """
    Apply Discount Percent and Calculate Final Price
    """
    final_price = int(price * (1 - discount))

    if 0 < final_price <= price:
        return final_price
    return "Error occurred"


print(apply_discount(1000,0.1))
print(apply_discount(-1000,0.1))
