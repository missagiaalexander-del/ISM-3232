class SupportChatbot:
    """A support chatbot. Rules handle what must be right. A model handles the rest."""

    def __init__(self, name, instructions, order_tool, stock_tool, model):
        """Set up the chatbot's tools, model, and history."""
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.stock_tool = stock_tool
        self.model = model
        self.history = []

    def choose_reply(self, user_message):
        """Use a rule when one applies. Otherwise ask the model."""
        text = user_message.lower()

        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a human agent."
        if "order" in text:
            return self.order_reply(user_message)
        if "stock" in text:
            return self.stock_reply(user_message)

        return self.model_reply()

    def needs_human(self, text):
        """Return whether the message asks for a change that needs an agent."""
        return "change" in text and "address" in text

    def order_reply(self, user_message):
        """Look up an order mentioned in the message."""
        order_id = self.order_tool.find_order_id(user_message)
        if order_id is None:
            return "I couldn't find an order ID in your message."

        status = self.order_tool.find_status(order_id)
        if status is None:
            return f"I couldn't find order {order_id}."

        return f"Order {order_id} is {status}."

    def stock_reply(self, user_message):
        """Look up the quantity for a product mentioned in the message."""
        product = self.stock_tool.find_product(user_message)
        if product is None:
            return "I couldn't find a product in your message."

        quantity = self.stock_tool.find_quantity(product)
        if quantity == 0:
            return f"The {product} is out of stock."
        if quantity is None:
            return f"I couldn't find stock information for {product}."

        return f"We have {quantity} of the {product} in stock."

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."

        return reply

    def respond(self, user_message):
        """Record the message, choose a reply, and save that reply."""
        self.history.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        reply = self.choose_reply(user_message)

        self.history.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )

        return reply
