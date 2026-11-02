class OrderLookup:
    """A tool that knows about orders. It knows nothing about chatting."""

    def __init__(self, orders):
        """Initialize the lookup with a mapping of order IDs to statuses."""
        self.orders = orders

    def find_order_id(self, text):
        """Find an order ID in text, ignoring letter case."""
        text = text.upper()
        for order_id in self.orders:
            if str(order_id).upper() in text:
                return order_id
        return None

    def find_status(self, order_id):
        """Return the status associated with an order ID, if it exists."""
        return self.orders.get(order_id)
