# Module 1 Quick Checks (Lessons 1.5 to 1.8)

**Course:** Python for AI · **Module 1:** Python Basics for GenAI and Agentic AI · **Updated:** Oct 2026

> **Student version.** Answer on your own first, without AI tools or notes. The goal is to find what you have not understood yet, not to get full marks.

**Format per lesson:** 5 MCQs + 1 "Predict the Output" · **Time:** 5 minutes · **Marks:** 6 per lesson

**How to answer:** add your answers to `docs/my-answers-module-1.md` like this:

```text
1.5: Q1 ?, Q2 ?, Q3 ?, Q4 ?, Q5 ?, Q6 (your predicted output)
```

**Predict the Output rule:** write your answer **before** running the code. Then run it with `uv run` and check yourself.

---

## Lesson 1.5: Variables and Data Types

**Q1.** What is the type of `temperature` after `temperature = 0.7`?
- a) int
- b) str
- c) float
- d) bool

**Q2.** What does `int(3.9)` return?
- a) 4
- b) 3
- c) 3.9
- d) ValueError

**Q3.** Which is a valid variable name?
- a) `2nd_model`
- b) `max-tokens`
- c) `max_tokens`
- d) `max tokens`

**Q4.** What does `bool("False")` return?
- a) False
- b) True
- c) None
- d) TypeError

**Q5.** The user types `1200` into `tokens = input("Tokens: ")`. Why does `tokens * 2` not give `2400`?
- a) Python cannot multiply numbers
- b) `input()` returns text, so `* 2` repeats it: `"12001200"`
- c) `tokens` is a float
- d) `*` only works with lists

**Q6. Predict the Output**
```python
tokens_used = 120
tokens_used = tokens_used + 80
print(tokens_used / 100)
```

---

## Lesson 1.6: Working with Text (Strings)

**Q1.** What does `"Python for AI"[0:6]` return?
- a) `"Pytho"`
- b) `"Python"`
- c) `"Python "`
- d) `"ython "`

**Q2.** `text = "Python"`. What is `text[-1]`?
- a) `"P"`
- b) `"n"`
- c) `"o"`
- d) IndexError

**Q3.** Which method removes spaces at both ends of a string?
- a) `.lower()`
- b) `.strip()`
- c) `.title()`
- d) `.capitalize()`

**Q4.** What does this print?
```python
name = "ali"
name.upper()
print(name)
```
- a) `ALI`
- b) `ali`
- c) `Ali`
- d) Error

**Q5.** `message = "I want a REFUND"`. Which check correctly finds "refund"?
- a) `"refund" in message`
- b) `"refund" in message.lower()`
- c) `message == "refund"`
- d) `message.startswith("refund")`

**Q6. Predict the Output**
```python
cost = 1234.5678
tokens = 1500000
print(f"{cost:.2f} PKR, {tokens:,} tokens")
```

---

## Lesson 1.7: Operators and Making Decisions

**Q1.** What does `17 // 5` give?
- a) 3.4
- b) 3
- c) 2
- d) 85

**Q2.** What does `17 % 5` give?
- a) 3
- b) 3.4
- c) 2
- d) 0

**Q3.** Which line **compares** `task` with `"code"`?
- a) `if task = "code":`
- b) `if task == "code":`
- c) `if task := "code":`
- d) `if "code" = task:`

**Q4.** Why is `if task == "code" or "chat":` **always** True, whatever `task` is?
- a) `"chat"` on its own is a non-empty string, so it counts as True
- b) `or` only works with numbers
- c) Strings cannot be compared with `==`
- d) It is not always True

**Q5.** What does this print?
```python
score = 85
if score > 50:
    print("Pass")
elif score > 80:
    print("Distinction")
```
- a) `Pass`
- b) `Distinction`
- c) `Pass` and `Distinction`
- d) Nothing

**Q6. Predict the Output**
```python
tokens = 3000
if tokens > 4000:
    print("Too long")
elif tokens > 2000:
    print("Costs more")
else:
    print("Good length")
```

---

## Lesson 1.8: Mini Project: Rule-Based Chatbot

**Q1.** What does `break` do inside `while True`?
- a) Closes the terminal
- b) Leaves the loop immediately
- c) Skips to the next round of the loop
- d) Restarts the program

**Q2.** Your bot never stops, even when you type `bye`. What should you do **first**?
- a) Reinstall Python
- b) Press `Ctrl + C`, then check that the message is cleaned with `.strip().lower()` and that `break` is inside the loop
- c) Delete the file
- d) Add more `elif` rules

**Q3.** Why is `if "hi" in message:` a bad greeting rule?
- a) `in` does not work with strings
- b) "hi" hides inside words like "which" and "this", so the greeting fires by mistake
- c) It is slower than `==`
- d) It only works with capital letters

**Q4.** "My order is late" goes to the order menu instead of the manager. Why?
- a) The order rule is above the complaint rule, and only the first True block runs
- b) The word "late" is not a string
- c) The bot needs more memory
- d) `elif` cannot check two words

**Q5.** Where should the bot ask for the user's name?
- a) Inside the loop, every round
- b) Once, **before** the loop
- c) After `break`
- d) Inside the `else` block

**Q6. Predict the Output**
The user types `hello`, then `  BYE  `.
```python
count = 0
while True:
    text = input("You: ").strip().lower()
    count += 1
    if text == "bye":
        break
print(f"{count} messages")
```
What is the last line printed?

---

## After the Check

- Answers are discussed in the **next class warm-up**.
- Got a question wrong? Re-read that lesson's section in `docs/` and redo its Code Task.
- Commit your answers file: `git commit -m "Module 1 quick checks part 2"`

**Self-score guide**

| Score (per lesson) | Meaning |
|---|---|
| 6 | Mastered, move on |
| 4 to 5 | Good, review what you missed |
| 0 to 3 | Re-read the lesson and ask in class |
