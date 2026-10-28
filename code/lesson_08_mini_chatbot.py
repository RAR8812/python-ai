"""Lesson 1.8: City Care Bot. A rule-based chatbot with a loop and memory."""

print("City Care Bot: Hi! Ask about timings, fees, location or appointments. Type 'bye' to exit.")

# Ask the name once, before the loop, so we do not ask on every message
name = input("City Care Bot: What is your name? ").strip().title()

total_messages = 0
unanswered = 0

while True:
    # strip() and lower() so " TIMINGS " matches the keyword "timing"
    message = input(f"{name}: ").strip().lower()

    if message == "":
        print("City Care Bot: Please type a question.")
        continue

    total_messages += 1

    if message == "bye":
        print(f"City Care Bot: Take care, {name}!")
        break
    # Complaint rule comes first so an angry message is never answered by a keyword rule
    elif "late" in message or "problem" in message or "complaint" in message or "wrong" in message:
        print("City Care Bot: Sorry about that. The clinic manager will call you today.")
    # "hi" is checked with == and startswith, because "hi" inside "which" would fire by mistake
    elif message == "hi" or message == "hello" or message.startswith("hi ") or message.startswith("hello "):        print(f"City Care Bot: Hello {name}! How can I help you?")
    elif "timing" in message or "hours" in message or "open" in message:
        print("City Care Bot: We are open 10 am to 8 pm, Monday to Saturday.")
    elif "fee" in message or "price" in message or "cost" in message:
        print("City Care Bot: Consultation fee is 2,000 PKR.")
    elif "where" in message or "location" in message or "address" in message:
        print("City Care Bot: We are on Main Boulevard, Lahore.")
    elif "appointment" in message or "book" in message:
        print("City Care Bot: Call 0300-0000000 to book an appointment.")
    else:
        # Every fallback is a gap in our rules, which an LLM will fill in Module 2
        unanswered += 1
        prompt = f"You are the friendly assistant of City Care Clinic. Answer in 2 lines: {message}"
        print(f"City Care Bot: I am not sure yet. In Module 2, an AI will answer: {prompt}")

print("=" * 40)
print(f"Chat summary: {total_messages} messages, {unanswered} unanswered.")