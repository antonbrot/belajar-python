import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "greetings", "what's up"]
    if any(word in user_input for word in greetings):
        return random.choice([
            "Hello! How can I assist you today?",
            "Hey there! What would you like to know?",
            "Hi! How's your day going?",
            "Greetings! How may I help you?"
        ])

    if "how are you" in user_input:
        return random.choice([
            "I'm just a program, but I'm doing great! How about you?",
            "I am just lines of code, but thank you for asking! How are you?",
            "I don’t have feelings, but if I did, I’d say I'm fantastic! How are you doing?",
            "I'm good, thank you for asking! How can I assist you today?"
        ])
    
    if "thank you" in user_input or "thanks" in user_input:
        return random.choice([
            "You're welcome!",
            "No problem at all!",
            "Glad I could help!",
            "Anytime! I'm here to assist."
        ])
    if "bye" in user_input or "goodbye" in user_input:
        return random.choice([
            "Goodbye! Have a great day!",
            "Take care! Hope to chat again soon.",
            "Bye! Feel free to return anytime.",
            "See you later!"
        ])
    return random.choice([
        "I'm not sure I understand. Could you rephrase that?",
        "I'm still learning, could you say that differently?",
        "Sorry, I'm not able to understand that. Can you ask something else?",
        "That's interesting, but I don't have an answer for that."
    ])

def chat():
    print("Chatbot: Hi! I am your simple AI chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: " + chatbot_response(user_input))
            break
        else:
            print("Chatbot: " + chatbot_response(user_input))

if __name__ == "__main__":
    chat()
