import json
from pathlib import Path
from intents import detect_intents


def load_faq():

    try:
        file_path = Path(__file__).parent / "faq.json"

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("faqs", [])

    except (FileNotFoundError, json.JSONDecodeError):
        print("Warning: FAQ dataset could not be loaded.")
        return []


def search_faq(user_input, faqs):

    user_input = user_input.lower()

    for faq in faqs:

        question = faq["question"].lower()

        keywords = question.replace("?", "").split()

        if any(word in user_input for word in keywords if len(word) > 3):
            return faq["answer"]

    return None


def chatbot():

    print("\n" + "=" * 55)
    print("       DATHEON CUSTOMER SUPPORT CHATBOT")
    print("=" * 55)

    print("Hello! Welcome to our interactive assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")

    faqs = load_faq()

    while True:

        try:

            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Bot: Please enter a message.")
                continue

            if user_input.lower() in ["bye", "exit", "quit"]:
                print("Bot: Thank you for chatting with us. Goodbye!")
                break

            if user_input.lower() == "help":
                print("""
Bot: I can help you with:

1. Business hours
2. Product information
3. Product prices
4. Delivery information
5. Order FAQs
6. General greetings
""")
                continue

            detected = detect_intents(user_input)

            if detected:

                for intent in detected:
                    from intents import INTENTS
                    print("Bot:", INTENTS[intent]["response"])

            else:

                answer = search_faq(user_input, faqs)

                if answer:
                    print("Bot:", answer)

                else:
                    print("Bot: Sorry, I didn't understand that.")
                    print("Please ask about products, prices, delivery or business hours.")

        except KeyboardInterrupt:
            print("\nBot: Chat session ended. Goodbye!")
            break

        except Exception as error:
            print("Bot: Something went wrong. Please try again.")


if __name__ == "__main__":
    chatbot()