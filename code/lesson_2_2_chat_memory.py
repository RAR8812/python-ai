"""Task 2.2: Personal Tutor with Memory. Remembers the chat but trims old messages to control cost."""
from langchain.chat_models import init_chat_model

llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0.2)

# The system message sets the tutor's role and answer length; it always stays at messages[0]
system_message = {"role": "system", "content": "You are a friendly tutor. Answer in 2 short lines."}
messages = [system_message]

print("Tutor: Ask me anything. Commands: /reset, /count, bye")

while True:
    user_text = input("You: ").strip()

    if user_text == "":
        continue
    if user_text.lower() == "bye":
        print("Tutor: Goodbye!")
        break
    if user_text == "/reset":
        # Rebuild the list with only the system message, so the tutor forgets the chat but keeps its role
        messages = [system_message]
        print("Tutor: Memory cleared.")
        continue
    if user_text == "/count":
        print(f"Tutor: {len(messages)} messages in memory.")
        continue

    # The AI only knows what is in the list, so we append the user message AND the AI reply
    messages.append({"role": "user", "content": user_text})
    response = llm.invoke(messages)
    messages.append({"role": "assistant", "content": response.text})

    # Keep the system message plus the last 8 messages, so the cost does not grow forever
    messages = [messages[0]] + messages[1:][-8:]

    print(f"Tutor: {response.text}")
    print(f"       (tokens sent: {response.usage_metadata['input_tokens']})")