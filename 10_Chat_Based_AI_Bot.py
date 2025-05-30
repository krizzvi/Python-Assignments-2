def respond(query):
    responses = {
        "hello": "Hi there!",
        "bye": "Goodbye!",
        "how are you": "I'm just code, but thanks!",
    }
    for key in responses:
        if key in query.lower():
            return responses[key]
    return "Sorry, I don't understand."

def main():
    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break
        print("Bot:", respond(q))

if __name__ == "__main__":
    main()