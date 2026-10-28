"""Task 2.4: Batch Service Writer. Writes one-sentence menu descriptions for every service and reports the cost."""
from langchain.chat_models import init_chat_model

# Services and prices in PKR; the 0-price item has no price yet, so it must be skipped
services = {
    "Consultation": 2000,
    "Checkup": 3500,
    "Blood test": 1500,
    "Ultrasound": 4000,
    "Old package": 0,
}

# Create the model ONCE before the loop, because loading it again for every item would waste time
llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0.5)

results = []        # a list of dictionaries: item, price, text
total_tokens = 0    # accumulators start at 0 BEFORE the loop and grow with each AI call
total_seconds = 0

for name, price in services.items():
    if price == 0:
        # continue jumps to the next item, so no AI call is made and no tokens are spent
        print(f"Skipping {name} (no price)")
        continue

    response = llm.invoke([
        {"role": "system", "content": "You write menu descriptions for City Care Clinic in Lahore. Reply with exactly one friendly sentence and no medical promises."},
        {"role": "user", "content": f"Describe this service: {name}."},
    ])

    results.append({"item": name, "price": price, "text": response.text.strip()})
    total_tokens += response.usage_metadata["total_tokens"]
    total_seconds += response.response_metadata["total_duration"] / 1_000_000_000

print("=" * 50)
# enumerate gives each row a number, and start=1 makes the menu begin at 1 instead of 0
for number, row in enumerate(results, start=1):
    print(f"{number}. {row['item']} ({row['price']} PKR)")
    print(f"   {row['text']}")
print("=" * 50)
print(f"{len(results)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds")