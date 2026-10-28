"""Task 2.3: Persona Bot with Real Facts. Chats with memory, switchable style, and no invented prices."""
from langchain.chat_models import init_chat_model

# One dictionary for the real facts: the AI may only use what is written here
facts = {
    "name": "City Care Clinic",
    "city": "Lahore",
    "hours": "10 am to 8 pm, Monday to Saturday",
    "phone": "0300-0000000",
    "address": "Main Boulevard, Lahore",
    "prices": {"consultation": 2000, "checkup": 3500, "blood test": 1500},
}

# Each persona is just a style sentence we drop into the system message
personas = {
    "friendly": "warm and cheerful, uses simple words",
    "formal": "polite and professional, no slang",
    "brief": "very short, one line per answer",
}

# One config dictionary, so we change the model or memory size in one place
config = {"model": "llama3.2", "temperature": 0.2, "memory_size": 8}

llm = init_chat_model(config["model"], model_provider="ollama", temperature=config["temperature"])

# Build the prices text with a loop over the nested dictionary
price_text = ""
for item, price in facts["prices"].items():
    price_text += f"{item}: {price} PKR. "

# The rules tell the AI to ONLY use these facts, so it admits what it does not know
rules = (
    f"You are the assistant of {facts['name']} in {facts['city']}. "
    f"Opening hours: {facts['hours']}. Address: {facts['address']}. Phone: {facts['phone']}. "
    f"Prices: {price_text}"
    f"Only use these facts. If something is not listed, say you do not know "
    f"and suggest calling {facts['phone']}."
)

style = personas["friendly"]
messages = [{"role": "system", "content": f"Style: {style}. {rules}"}]

print("Bot ready. Commands: /persona friendly|formal|brief, /price <item>, bye")

while True:
    user_text = input("You: ").strip()

    if user_text == "":
        continue
    if user_text.lower() == "bye":
        print("Bot: Goodbye!")
        break

    if user_text.startswith("/persona"):
        name = user_text[len("/persona"):].strip().lower()
        # .get() with a default, so a wrong name never crashes with a KeyError
        style = personas.get(name, personas["friendly"])
        # Replace only the system message, so the chat memory stays
        messages[0]["content"] = f"Style: {style}. {rules}"
        print(f"Bot: Style changed to: {style}")
        continue

    if user_text.startswith("/price"):
        item = user_text[len("/price"):].strip().lower()
        # Answered from the dictionary, so no AI call and no invented price
        price = facts["prices"].get(item)
        if price is None:
            print(f"Bot: Sorry, {item} is not on our menu.")
        else:
            print(f"Bot: {item.title()} costs {price} PKR.")
        continue

    messages.append({"role": "user", "content": user_text})
    response = llm.invoke(messages)
    messages.append({"role": "assistant", "content": response.text})

    # Keep the system message plus the last N messages, so the cost does not grow forever
    messages = [messages[0]] + messages[1:][-config["memory_size"]:]

    print(f"Bot: {response.text}")