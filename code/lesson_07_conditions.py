"""Lesson 1.7: Smart Model Router. Pick a model by task type and estimate cost."""

# strip() and lower() so " Code " and "CODE" still match "code"
task = input("Task (code / private / chat): ").strip().lower()
# int() because input() always returns text
tokens = int(input("Estimated tokens: "))

# Private data goes to the local model, code goes to a strong model,
# everything else goes to a cheap one
if task == "code":
    model = "claude (cloud, strong at code)"
    price_per_1k = 0.8      # example price in PKR, not a real price
elif task == "private":
    model = "llama3.2 (local, Ollama)"
    price_per_1k = 0        # local model is free to run
else:
    model = "gemini (cloud, cheap)"
    price_per_1k = 0.2      # example price in PKR, not a real price

cost = tokens / 1000 * price_per_1k

if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

print(f"Chosen model: {model}")
# :.2f always shows 2 decimals, so 0 prints as 0.00
print(f"Estimated cost: {cost:.2f} PKR")