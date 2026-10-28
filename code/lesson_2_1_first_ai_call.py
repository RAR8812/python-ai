"""Task 2.1: AI Tutor. Explains a topic at the right level and reports the token cost."""
from langchain.chat_models import init_chat_model

topic = input("Topic:   ").strip()
level = input("Level (beginner or expert): ").strip()

# Low temperature (0.2) so explanations stay focused and repeatable
llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0.2)

# The system message sets the role AND the length, so every answer stays short and at the right level
system_message = f"You are a friendly tutor for a {level} student. Explain in 3 short lines."

response = llm.invoke([
    {"role": "system", "content": system_message},
    {"role": "user", "content": f"Explain {topic}."},
])

# total_duration is in nanoseconds, so divide to get seconds
seconds = response.response_metadata["total_duration"] / 1_000_000_000
total_tokens = response.usage_metadata["total_tokens"]

print("=" * 40)
print(response.text)
print("=" * 40)
print(f"{total_tokens} tokens in {seconds:.1f} seconds")