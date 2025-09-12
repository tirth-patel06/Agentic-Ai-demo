# 🤖 Agentic Assistant Demo

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20App-brightgreen?logo=streamlit)](https://agentic-ai-demo-tirth-main.streamlit.app/)

A minimal demo of an **Agentic AI system** built with [Streamlit](https://streamlit.io/), [LangChain](https://www.langchain.com/), and [Groq](https://groq.com/).  
It takes a high-level task, breaks it into subtasks, maps them into JSON actions, and simulates how agents execute them in real-time.

---

## 🧩 System Flow

![System Flow](Backend/subTask2-Flow.png)

---

## 🧠 Model Used
- **LLM**: `llama3-70b-8192` (via **Groq API**)  
- **LangChain**: prompt templates + JSON output parser  
- **Streamlit**: interactive frontend for user input & live logs  

---

## ⚡ Features
- Breaks a high-level task into **3–6 major subtasks**  
- Converts subtasks into **structured JSON actions** (`subtask`, `action_type`, `description`)  
- Routes each action to the correct **specialized agent** (email, booking, poster, form, etc.)
- Simulates **agent execution logs** (step-by-step, expandable in UI)
-  Supports **college club–oriented tasks** like:

   - Sending mails

   - Booking classrooms

   - Arranging equipment

   - Designing posters

   - Scheduling meetings

   - Generating forms & certificates

---

## 🔎 Approach

1. **Task Decomposition**  
   - Used a **prompt with `groq/compound`** to break down the user query into **clear subtasks**.  
   - The model was instructed to return only a **numbered list** for clean parsing.  

2. **JSON Mapping**  
   - A second **structured prompt** was used with the same model.  
   - Subtasks were mapped into JSON objects with fields:  
     - `subtask` → original task  
     - `action_type` → one of predefined categories  
     - `description` → short explanation  

3. **Output Parsing**  
   - Used `JsonOutputParser` from LangChain to ensure valid JSON output.  

4. **Agent Simulation Layer**  
   - Added a **mock agent function** that simulates execution logs (`assigned → working → completed`).  
   - Streamlit updates logs in real-time for a **step-by-step agentic flow**.  

---
```
AGENTIC-CHATBOT/
├── Backend/
│   ├── branch.py
│   ├── subTask2.py
│   └── subTask2-Flow.png
│
├── UI/
│   └── main.py
│
├── requirements.txt
└── README.md    
```
---
🔗 **Try the demo here:** [Agentic AI Demo]((https://agentic-ai-demo-xazqx6ja4lqtxlqrmz27vz.streamlit.app/))
