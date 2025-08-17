# 🤖 Agentic Assistant Demo

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20App-brightgreen?logo=streamlit)](https://agentic-ai-demo-task2.streamlit.app/)

A minimal demo of an **Agentic AI system** using [Streamlit](https://streamlit.io/) + [LangChain](https://www.langchain.com/) + [Groq](https://groq.com/).  
It takes a high-level task, breaks it into subtasks, maps them into JSON actions, and simulates how agents execute them in real-time.

---

## 🧠 Model Used
- **LLM**: `llama3-70b-8192` (via **Groq API**)  
- **LangChain**: for task decomposition, prompt templates, and JSON parsing  
- **Streamlit**: for the interactive frontend  

---

## ⚡ Features
- Task → **3–6 major subtasks**  
- Subtasks → **structured JSON actions** (`subtask`, `action_type`, `description`)  
- Real-time **agent execution logs**  

---

🔗 **Try it here:** [Agentic AI Demo](https://agentic-ai-demo-task2.streamlit.app/)
