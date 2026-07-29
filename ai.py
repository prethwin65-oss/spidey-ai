import datetime
import random

def get_ai_response(message):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! I am Spidey-AI. How can I help you?"

    elif "how are you" in msg:
        return "I'm doing great! Thanks for asking."

    elif "time" in msg:
        return "Current time: " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in msg:
        return "Today's date: " + str(datetime.date.today())

    elif "who are you" in msg:
        return "I am Spidey-AI, your intelligent AI assistant."

    elif "bye" in msg:
        return "Goodbye! Have a nice day."

    else:
        replies = [
            "I'm still learning. Can you ask another question?",
            "Interesting question! I'll improve over time.",
            "I don't know the answer yet, but I can learn more features.",
            "Can you explain your question differently?"
        ]
        return random.choice(replies)
