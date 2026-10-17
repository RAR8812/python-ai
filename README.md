<div align="center">

# Python for AI

### From your first `print()` to AI agents that do real work

A hands-on, project-driven course that teaches Python through the lens of Generative AI and Agentic AI.
Every lesson ends with something you can run, push to GitHub, and show to a client or employer.

<br>

![Python](https://img.shields.io/badge/Python-3.13-1f425f?style=for-the-badge&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-package%20manager-261230?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20apps-1c3c3c?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-local%20models-000000?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Module%202%20in%20progress-0a7d5a?style=for-the-badge)

<br>

[Overview](#overview) &nbsp;&middot;&nbsp;
[Learning Path](#the-learning-path) &nbsp;&middot;&nbsp;
[Curriculum](#curriculum) &nbsp;&middot;&nbsp;
[Assessments](#assessments-and-projects) &nbsp;&middot;&nbsp;
[Getting Started](#getting-started) &nbsp;&middot;&nbsp;
[Repository Layout](#repository-layout) &nbsp;&middot;&nbsp;
[Resources](#core-resources)

</div>

---

## Overview

Most Python courses teach the language first and leave AI for "later". This course does the opposite: **every concept is introduced through a real AI use case**. Variables become model configurations, strings become prompts, `if / elif / else` becomes a model router, and a `while` loop becomes a chatbot. By the start of Module 2, that chatbot is talking to a real language model.

The course is built around one idea from Lesson 1.1:

<div align="center">

### `Agent = LLM + Tools + Memory + Loop`

</div>

Each module adds one more piece of that formula, until you can build agents that plan, use tools, and finish tasks on their own.

### Who this course is for

| You are | You will leave with |
|---|---|
| A complete beginner to programming | A solid Python foundation, taught through problems you care about |
| A student aiming for an AI career | A public GitHub portfolio with one commit per lesson |
| A freelancer or aspiring freelancer | Client-style projects you can pitch to local businesses |
| A developer new to GenAI | A practical path from API calls to agents, without the ML theory detour |

### What makes it different

- **Applied AI first.** Industry demand is for engineers who *use* models well, not train them. ML and deep learning can come later, when you need them.
- **Local and private by default.** Lessons run on [Ollama](https://ollama.com), so you can learn for free and offline, then switch to Claude, OpenAI or Gemini with a one-line change.
- **Client-ready mindset.** Every lesson has a *Job & Client Angle* section that connects the skill to paid work.
- **Portfolio from day one.** Every task is pushed to GitHub, so your learning log becomes your proof of skill.

---

## The Learning Path

```mermaid
flowchart LR
    M1["<b>Module 1</b><br/>Python Basics for<br/>GenAI and Agentic AI"]
    M2["<b>Module 2</b><br/>Core Python for<br/>Your First LLM Apps"]
    M3["<b>Next</b><br/>RAG and Tools"]
    M4["<b>Next</b><br/>AI Agents"]
    J["<b>Outcome</b><br/>Jobs and<br/>Client Work"]

    M1 --> M2 --> M3 --> M4 --> J

    style M1 fill:#1f425f,stroke:#1f425f,color:#ffffff
    style M2 fill:#2c6e91,stroke:#2c6e91,color:#ffffff
    style M3 fill:#f4f6f8,stroke:#9aa5b1,color:#3e4c59
    style M4 fill:#f4f6f8,stroke:#9aa5b1,color:#3e4c59
    style J fill:#0a7d5a,stroke:#0a7d5a,color:#ffffff
```

### One project, growing with you

The course follows a single thread: a customer-support bot for an example business, *Sweet Crumbs bakery*. It starts as a prompt printer, becomes a rule-based chatbot, and then gets a real AI brain.

```mermaid
flowchart LR
    A["<b>Lesson 1.4</b><br/>Prompt builder<br/><i>input and f-strings</i>"]
    B["<b>Lesson 1.6</b><br/>Prompt cleaner<br/><i>string methods</i>"]
    C["<b>Lesson 1.7</b><br/>Model router<br/><i>if / elif / else</i>"]
    D["<b>Lesson 1.8</b><br/>Rule-based chatbot<br/><i>while loop and memory</i>"]
    E["<b>Lesson 2.1</b><br/>Hybrid AI chatbot<br/><i>rules plus a real LLM</i>"]

    A --> B --> C --> D --> E

    style E fill:#0a7d5a,stroke:#0a7d5a,color:#ffffff
```

---

## Curriculum

### Module 1: Python Basics for GenAI and Agentic AI

Build the foundation: tools, project setup, and the core Python that every AI application is made of. The module ends with a working chatbot for a real local business.

| # | Lesson | What you learn | What you build |
|:-:|---|---|---|
| 1.1 | [Welcome to GenAI and Agentic AI](docs/01-python-basics/1.1-welcome-genai-agentic-ai.md) | AI vs GenAI vs Agentic AI, tokens, hallucinations, why Python, jobs and gigs | Your AI career intro script |
| 1.2 | [Setting Up Your AI Dev Toolkit](docs/01-python-basics/1.2-setting-up-ai-dev-toolkit.md) | uv, Python 3.13, VS Code or Antigravity, Git and GitHub, Ollama, Claude Code | A fully verified dev environment |
| 1.3 | [Your First Python Project with uv](docs/01-python-basics/1.3-first-python-project-with-uv.md) | `pyproject.toml`, `.venv`, `uv.lock`, `uv run`, `uv add`, pushing to GitHub | A clean, reproducible `python-ai` repo |
| 1.4 | [Talking to Python: print, input and Comments](docs/01-python-basics/1.4-print-input-comments.md) | Input, process, output; f-strings; multi-line prompts; writing "why" comments | Prompt builder |
| 1.5 | [Variables and Data Types](docs/01-python-basics/1.5-variables-data-types.md) | `str`, `int`, `float`, `bool`, `None`; casting; naming rules; type hints | AI model config and cost estimator |
| 1.6 | [Working with Text (Strings)](docs/01-python-basics/1.6-working-with-text-strings.md) | Indexing, slicing, string methods, immutability, f-string formatting | Prompt cleaner with token estimate |
| 1.7 | [Operators and Making Decisions](docs/01-python-basics/1.7-operators-and-decisions.md) | Arithmetic, comparison and logical operators; truthiness; `if / elif / else` | Smart model router |
| 1.8 | [Mini Project: Rule-Based Chatbot](docs/01-python-basics/1.8-mini-project-rule-based-chatbot.md) | `while True`, `break`, counters, rule order, designing intents | Business helper bot (Module 1 final) |

### Module 2: Core Python for Your First LLM Apps

Connect Python to real language models, then learn the data structures and control flow that real LLM apps depend on.

| # | Lesson | What you learn | What you build |
|:-:|---|---|---|
| 2.1 | [Your First AI Call](docs/02-talk-to-ai/lesson-2.1-your-first-ai-call.md) | LangChain `init_chat_model`, `invoke`, token usage, system messages, temperature, streaming | AI tutor, and the Module 1 bot with a real AI brain |
| 2.2 | Chat History with Lists | Coming soon | A chatbot that remembers the conversation |
| 2.3 | Dictionaries | Coming soon | Structured data such as price lists |
| 2.4 | `for` Loops | Coming soon | Processing many items and responses |

> The course is released lesson by lesson. Watch or star the repository to follow new lessons as they are published.

---

## Inside Every Lesson

Each lesson follows the same structure, so you always know where to look.

```mermaid
flowchart LR
    A["<b>Goal</b><br/>By the end"] --> B["<b>Mental Model</b><br/>One clear picture"]
    B --> C["<b>Concepts</b><br/>Code and tables"]
    C --> D["<b>Mini Build</b><br/>AI-flavoured script"]
    D --> E["<b>Common Errors</b><br/>Cause and fix"]
    E --> F["<b>Job and Client</b><br/>Why it pays"]
    F --> G["<b>Your Task</b><br/>Build and push"]
    G --> H["<b>Quick Check</b><br/>Test yourself"]
```

| Section | Purpose |
|---|---|
| **By the end** | A one-sentence promise of what you will be able to do |
| **Mental model** | A simple analogy that makes the concept stick |
| **Mini build** | A short, complete script tied to a real AI use case |
| **Common errors** | The exact error messages beginners hit, with causes and fixes |
| **Job and client angle** | How the skill shows up in jobs, freelancing and client work |
| **Your task** | A self-created exercise you commit and push to GitHub |
| **Key takeaways and quick check** | A five-point summary and three questions to confirm understanding |
| **Must-have resources** | Official documentation and the best references for going deeper |

---

## Assessments and Projects

Learning is measured in three ways: quick knowledge checks, small code tasks, and client-style projects with a live demo.

```mermaid
flowchart LR
    L["Lesson"] --> Q["Quick Check<br/><i>5 minutes</i>"]
    Q --> T["Code Task<br/><i>10 marks</i>"]
    T --> P["Module Project<br/><i>100 marks + demo</i>"]
    P --> G["GitHub Portfolio"]
```

### Quick checks

Five multiple-choice questions plus one *Predict the Output* question per lesson. Answer without notes or AI tools first, then run the code to check yourself.

| Assessment | Covers |
|---|---|
| [Module 1 Quick Checks, Part 1](docs/assessments/module-1-quick-checks.md) | Lessons 1.1 to 1.4 |
| [Module 1 Quick Checks, Part 2](docs/assessments/module-1-quick-checks-part-2.md) | Lessons 1.5 to 1.8 |

### Code tasks

Small, client-style exercises, one per lesson, each marked out of 10 and pushed as a single commit.

| Assessment | Covers | Tasks |
|---|---|---|
| [Module 1 Code Tasks, Part 1](docs/assessments/module-1-code-tasks.md) | Lessons 1.1 to 1.4 | AI career intro, toolkit proof, client-ready repo, business prompt builder |
| [Module 1 Code Tasks, Part 2](docs/assessments/module-1-code-tasks-part-2.md) | Lessons 1.4 to 1.8 | Prompt builder, model profile card, prompt cleaner, model router, business helper bot |

### Module projects

Each project starts with a client story, is marked out of 100, and ends with a three-minute demo pitched like a freelancer.

| Project | Covers | The brief |
|---|---|---|
| [AI Prompt Kit for a Local Business](docs/assessments/module-1-project-brief.md) | Lessons 1.1 to 1.4 | A tool that turns a business's details into three ready-to-use AI prompts, tested on a real model |
| [AI Front Desk for a Local Business](docs/assessments/module-1-project-brief-part-2.md) | Lessons 1.1 to 1.8 | A front desk that answers FAQs with rules, calculates exact price quotes, routes other questions to a local or cloud model, and prints a session report |

**Project marking at a glance**

| Score | Level |
|:-:|---|
| 85 to 100 | Client-ready |
| 70 to 84 | Strong, minor fixes |
| 50 to 69 | Working, needs polish |
| Below 50 | Redo and resubmit |

AI tools are allowed throughout the course, but you must be able to explain every line you submit. A project you cannot explain in the demo is capped at 50 marks.

---

## Getting Started

### Prerequisites

| Tool | Purpose | Verify with |
|---|---|---|
| [uv](https://docs.astral.sh/uv) | Installs Python and packages, manages the project | `uv --version` |
| [Python 3.13](https://www.python.org) | The language (installed through uv) | `uv run python --version` |
| [VS Code](https://code.visualstudio.com) or [Antigravity](https://antigravity.google) | Code editor | `code --version` |
| [Git](https://git-scm.com) and a [GitHub](https://github.com) account | Version control and portfolio | `git --version` |
| [Ollama](https://ollama.com/download) | Run AI models locally, for free | `ollama --version` |
| [Claude Code](https://docs.claude.com/en/docs/claude-code) (optional) | AI coding agent in the terminal | `claude --version` |

Full installation steps for macOS, Linux and Windows are in [Lesson 1.2](docs/01-python-basics/1.2-setting-up-ai-dev-toolkit.md).

### Quick start

**1. Clone the repository and install dependencies**

```bash
git clone https://github.com/the-schoolofai/python-ai.git
cd python-ai
uv sync
```

**2. Run the first script**

```bash
uv run main.py
```

**3. Prepare for Module 2 (AI calls)**

```bash
ollama pull llama3.2           # about 2 GB; use llama3.2:1b on 8 GB RAM laptops
uv add langchain langchain-ollama
```

**4. Start learning**

Open [Lesson 1.1](docs/01-python-basics/1.1-welcome-genai-agentic-ai.md) and work through the lessons in order.

> **Tip:** always run code with `uv run`. It uses the project's own virtual environment, even if you forget to activate it.

### Recommended workflow

```mermaid
flowchart LR
    A["Read the lesson"] --> B["Type the code<br/>yourself"]
    B --> C["Run with<br/>uv run"]
    C --> D["Complete<br/>Your Task"]
    D --> E["Take the<br/>Quick Check"]
    E --> F["Commit<br/>and push"]
    F --> A
```

Use AI coding assistants to *explain*, not to skip learning. Ask for an explanation, then type the code yourself.

---

## Repository Layout

```text
python-ai/
├── code/                         Lesson and project scripts (.py)
│   └── lesson_01_intro.py
├── docs/
│   ├── 01-python-basics/         Module 1 lessons (1.1 to 1.8)
│   ├── 02-talk-to-ai/            Module 2 lessons (2.1 onward)
│   └── assessments/              Quick checks, code tasks and project briefs
├── notebooks/                    Jupyter notebooks (.ipynb)
├── main.py                       First script
├── pyproject.toml                Project definition and dependencies
├── uv.lock                       Exact dependency versions
├── .python-version               Pinned Python version (3.13)
└── README.md                     You are here
```

### File naming conventions

| Item | Convention | Example |
|---|---|---|
| Lesson scripts | `code/lesson_<NN>_<topic>.py` | `code/lesson_05_variables.py` |
| Module 2 scripts | `code/lesson_<M>_<N>_<topic>.py` | `code/lesson_2_1_first_ai_call.py` |
| Project scripts | `code/project_m<M>_<name>.py` | `code/project_m1_front_desk.py` |
| Commit messages | `Task <N>: <short description>` | `Task 1.5: model profile card` |

---

## Tech Stack

| Layer | Technology | Why it was chosen |
|---|---|---|
| Language | Python 3.13 | A stable release that AI libraries fully support |
| Project and packages | uv | One fast tool for Python versions, environments and lock files |
| LLM framework | LangChain | The same code works across Ollama, Claude, OpenAI and Gemini |
| Local models | Ollama (Llama 3.2) | Free, private and offline, ideal for learning and sensitive client data |
| Notebooks | Jupyter (ipykernel) | Interactive experiments inside VS Code |
| Version control | Git and GitHub | Team collaboration and a public portfolio |

---

## Core Resources

| Topic | Resource |
|---|---|
| Python | [Official tutorial](https://docs.python.org/3/tutorial/) |
| uv | [Documentation](https://docs.astral.sh/uv) |
| LangChain | [Models guide](https://docs.langchain.com/oss/python/langchain/models) and [Ollama integration](https://docs.langchain.com/oss/python/integrations/chat/ollama) |
| Ollama | [Model library](https://ollama.com/library) |
| Prompting | [Prompt engineering overview (Anthropic)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) |
| Agents | [Building effective agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents) |
| Tools for agents | [Model Context Protocol](https://modelcontextprotocol.io) |
| Further study | [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses) |

---

<div align="center">

**Python for AI** is created by **Rizwan** at **[The School of AI](https://github.com/the-schoolofai)**.

Clients pay for outcomes, not code. Learn to deliver both.

</div>
