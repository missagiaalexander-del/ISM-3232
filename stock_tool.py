class StockLookup:
    """Look up products and their available quantities."""

    def __init__(self, stock):
        self.stock = stock

    def find_product(self, text):
        """Return a known product name found in the message."""
        for product in self.stock:
            if product.lower() in text.lower():
                return product
        return None

    def find_quantity(self, product):
        """Return the quantity, or None for an unknown product."""
        return self.stock.get(product)
