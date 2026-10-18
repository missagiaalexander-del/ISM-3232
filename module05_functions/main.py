# main.py
from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_approval,
)

# add sample input
price, quantity = 450.00, 3
total = calculate_total(price, quantity)
review = requires_approval(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)

print(f"total: {total:.2f}")
print(f"requires approval: {requires_approval(total)}")
print(f"approval tier: {get_approval_tier(total)}")
print(f"discounted price: {apply_discount(price, 10):.2f}")
