from nltk.chat.util import Chat, reflections

# List of possible conversations
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! 😊", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I'm CodTech Chatbot 🤖", "You can call me CodBot!"]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but I'm doing great! 😄"]
    ],
    [
        r"bye|quit",
        ["Goodbye! 👋", "See you later!", "Have a nice day!"]
    ],
]

# Create chatbot object
chatbot = Chat(pairs, reflections)

# Start conversation
chatbot.converse()
