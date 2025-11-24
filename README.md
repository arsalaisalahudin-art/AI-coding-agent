AgentCourse — The Vibe Coding Agent

A Pythonist agent that understands, edits, and fixes Python files while exploiting connected tools.

🧠 What is AgentCourse?

AgentCourse is a Vibe Coding Agent — a Python-powered autonomous agent that can:

Read, understand, and analyze Python files

Make intelligent modifications and fixes

Programmatically edit code while preserving logic

Use connected tools (e.g., a calculator module) to enhance its capabilities

Think of it as a basic, foundational coding AI: it doesn’t just run code, it actively interprets and improves it.

🛠 Key Components
1. Agent Core

Location: agentcourse/

Responsibilities:

Read and process Python code

Apply changes or fixes autonomously

Maintain basic understanding of Python syntax and logic

2. Tools for the Agent

Functions (in functions/):

File I/O utilities

Python file execution scripts

Helpers for reading, writing, and analyzing files

📁 Repository Structure
agentcourse/
    Core agent code and utilities
calculator/
    Tool available for the agent
functions/
    Utility functions for file handling and code execution
call_function.py
config.py
generated-icon.png
lib64/
main.py
tests.py
.replit
.gitignore
.python-version

🚀 Getting Started
Prerequisites

Python 3.11+ (or the version specified in .python-version)

Installation

Clone the repository:

git clone https://github.com/arsalaisalahudin-art/agentcourse.git


Navigate into the folder:

cd agentcourse


(Optional) Install dependencies:

pip install -r requirements.txt

💡 Usage

Run the agent: Start by running agentcourse/main.py or other scripts in agentcourse/.

Testing: Check tests.py to see example behaviors and fixes applied by the agent.

Example:

python agentcourse/main.py

🤝 Contributing

Fork the repository

Create a new branch for your feature

Commit your changes

Push your branch and open a Pull Request

📜 License

This project is open-source under the MIT License.

📬 Contact

Author: Salahudin Khan
GitHub: arsalaisalahudin-art
