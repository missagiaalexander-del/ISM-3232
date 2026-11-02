# business_rules.py
# Author: Alexander Missagia

APPROVAL_LIMIT = 1000


def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return True if amount is greater than APPROVAL_LIMIT."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Return approval tier based on amount."""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, pct: float) -> float:
    """Return price after applying discount percentage. pct is 0 to 100."""
    return price * (1 - pct / 100)
