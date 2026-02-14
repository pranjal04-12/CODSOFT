print("🤖 CodSoft Chatbot (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")
    elif "name" in user:
        print("Bot: I am CodSoft AI Bot.")
    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")
    elif "help" in user:
        print("Bot: I can answer basic questions. Try asking something!")
    elif user == "bye":
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
