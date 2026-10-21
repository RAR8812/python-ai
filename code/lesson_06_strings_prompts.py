"""Lesson 1.6: Prompt Cleaner. Clean, measure and size a user's question."""

name = input("Your name: ")
question = input("Your question: ")

# strip() removes extra spaces, so messy input becomes clean text
name = name.strip().title()
question = question.strip().capitalize()

characters = len(question)
# Rough rule: 1 token is about 4 characters, so divide by 4
tokens = round(characters / 4)

# lower() makes the check work for Python, PYTHON, python and so on
mentions_python = "python" in question.lower()

print("=" * 40)
print(f"Cleaned question: {question}")
print(f"Characters: {characters}, about {tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print("=" * 40)

# [:150] slicing keeps the prompt from getting too long
prompt = f"""You are a friendly Python tutor.
Greet {name} by name and answer in 3 short lines.
Question: {question[:150]}"""

print(prompt)