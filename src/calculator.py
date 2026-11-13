"""Calculate order totals without making network requests."""

from decimal import Decimal, ROUND_HALF_UP


def order_total(unit_price: str, quantity: int, tax_rate: str = "0") -> Decimal:
    """Return a total rounded to cents; tax_rate is a fraction such as 0.08."""
    price = Decimal(unit_price)
    tax = Decimal(tax_rate)
    if not price.is_finite() or not tax.is_finite():
        raise ValueError("Price and tax rate must be finite")
    if price < 0 or tax < 0:
        raise ValueError("Price and tax rate must be nonnegative")
    if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a nonnegative integer")
    return (price * quantity * (1 + tax)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
