"""Lesson 1.5: AI Model Profile Card with a cost estimate."""

# Model profile: one value of each of the 4 types
model_name = "llama3.2"      # str
context_window = 128000      # int
price_per_1k = 0.5           # float, example price in PKR (not a real price)
runs_locally = True          # bool

# int() because input() always returns text, and we need a number for maths
tokens_per_chat = int(input("Tokens per chat: "))

cost = tokens_per_chat / 1000 * price_per_1k

# round() because floats are not exact and money should show 2 decimals
estimated_cost = round(cost, 2)

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k} PKR {type(price_per_1k)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")
print(f"Tokens per chat: {tokens_per_chat}")
print(f"Estimated cost: {estimated_cost} PKR")