# main.py
import json

def load_responses():
    try:
        with open('responses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def get_bot_response(user_message, knowledge_base):
    message = user_message.lower().strip()
    for keyword in knowledge_base:
        if keyword in message:
            return knowledge_base[keyword]
    return "I'm not sure I understand. Try asking about 'Python'."

def main():
    print("--- Simple Chatbot (Type 'quit' to exit) ---")
    knowledge = load_responses()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot: Bye!")
            break
        response = get_bot_response(user_input, knowledge)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
