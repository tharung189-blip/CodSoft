print("Simple AI Chatbot (type 'exit' to stop)")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hi there!")
    elif user == "how are you":
        print("Bot: I am fine. How can I assist you?")
    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")
    elif user == "what is your name":
        print("Bot: I am a simple AI chatbot.")
    elif user == "bye" or user == "exit":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I didn't understand.")