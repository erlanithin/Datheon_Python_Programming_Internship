import re

INTENTS = {
    "greeting": {
        "patterns": [
            r"\bhello\b",
            r"\bhi\b",
            r"\bhey\b",
            r"\bgood morning\b",
            r"\bgood evening\b"
        ],
        "response": "Hello! Welcome to our customer support assistant. How can I help you?"
    },

    "business_hours": {
        "patterns": [
            r"\bopening hours\b",
            r"\bbusiness hours\b",
            r"\bworking hours\b",
            r"\bwhen are you open\b",
            r"\btime\b"
        ],
        "response": "Our business hours are Monday to Saturday, 9:00 AM to 6:00 PM."
    },

    "product": {
        "patterns": [
            r"\bproducts\b",
            r"\bproduct details\b",
            r"\bavailable items\b",
            r"\bwhat do you sell\b"
        ],
        "response": "We offer electronics, clothing, accessories and lifestyle products."
    },

    "price": {
        "patterns": [
            r"\bprice\b",
            r"\bcost\b",
            r"\bhow much\b",
            r"\bpricing\b"
        ],
        "response": "Product prices depend on the selected item. Please check our product catalog."
    },

    "delivery": {
        "patterns": [
            r"\bdelivery\b",
            r"\bshipping\b",
            r"\bdeliver\b",
            r"\bshipment\b"
        ],
        "response": "Standard delivery usually takes 3-7 business days."
    },

    "thanks": {
        "patterns": [
            r"\bthanks\b",
            r"\bthank you\b",
            r"\bthankyou\b"
        ],
        "response": "You're welcome! Happy to help you."
    }
}


def detect_intents(user_input):

    detected = []

    text = user_input.lower().strip()

    for intent, details in INTENTS.items():

        for pattern in details["patterns"]:

            if re.search(pattern, text):

                detected.append(intent)
                break

    return detected