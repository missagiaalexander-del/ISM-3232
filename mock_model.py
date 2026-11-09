# MockModel
# Author: Alexander Missagia


class MockModel:
    """A stand-in for an AI model. It gives the same simple replies every time."""

    def reply(self, instructions, history):
        """Return a deterministic simulated reply for common support questions."""
        last_message = history[-1]["content"].lower()
        instruction_lines = instructions.splitlines()
        if "hello" in last_message:
            return "Hello! How can I help you today?"
        if "hour" in last_message:
            for line in instruction_lines:
                if "store hours" in line.lower():
                    return line.strip()
        if "shipping" in last_message or "delivery" in last_message:
            for line in instruction_lines:
                if (
                    line.strip()
                    .lower()
                    .startswith(("shipping takes ", "delivery takes "))
                ):
                    return line.strip()
        if "sale" in last_message and "return" in last_message:
            for line in instruction_lines:
                if "sale item" in line.lower() and "return" in line.lower():
                    return line.strip()
        if "price match" in last_message:
            return (
                "I do not know if we price match; please ask a human agent "
                "for clarification."
            )
        return (
            "I do not know; I can offer to pass you to a human agent for clarification."
        )
