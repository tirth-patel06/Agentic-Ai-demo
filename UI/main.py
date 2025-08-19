import json
from typing import List, Dict, Any
import streamlit as st
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BACKEND_IMPORT_ERROR = None
try:
    from Backend.subTask2 import get_subtasks, map_subtasks_to_actions
    from Backend.branch import get_branch
    from langchain_groq import ChatGroq
except Exception as e:
    BACKEND_IMPORT_ERROR = e

st.set_page_config(page_title="Agentic Club Bot", page_icon="🤖", layout="wide")
st.title("🤖 Agentic Club Bot — Demo UI")

ACTION_EMOJI = {
    "send_mail": "✉️",
    "book_classroom": "🏫",
    "arrange_equipment": "🧰",
    "generate_poster": "🖼️",
    "schedule_meeting": "🗓️",
    "execute_task": "⚙️",
    "generate_form": "📝",
    "generate_certificate": "🏅",
}

# Mock logs for each action type
MOCK_LOGS = {
    "send_mail": [
        "Generating mail content...",
        "Connecting to mail server...",
        "Sending mail...",
        "✅ Mail sent successfully!"
    ],
    "book_classroom": [
        "Checking classroom availability...",
        "Preparing booking request...",
        "Submitting request to admin...",
        "✅ Classroom booked!"
    ],
    "arrange_equipment": [
        "Gathering required equipment list...",
        "Contacting inventory manager...",
        "Arranging transport & setup...",
        "✅ Equipment arranged!"
    ],
    "generate_poster": [
        "Drafting poster layout...",
        "Adding event details...",
        "Applying design template...",
        "✅ Poster generated!"
    ],
    "schedule_meeting": [
        "Creating meeting agenda...",
        "Checking member availability...",
        "Scheduling on calendar...",
        "✅ Meeting scheduled!"
    ],
    "execute_task": [
        "Breaking task into subtasks...",
        "Assigning responsibilities...",
        "Tracking progress...",
        "✅ Task executed!"
    ],
    "generate_form": [
        "Designing form structure...",
        "Adding required fields...",
        "Publishing form link...",
        "✅ Form generated!"
    ],
    "generate_certificate": [
        "Fetching participant details...",
        "Applying certificate template...",
        "Generating PDF files...",
        "✅ Certificates generated!"
    ],
}

def groq_model():
    return ChatGroq(model="llama3-70b-8192", temperature=0)

query = st.text_input("Enter your query:", "Organise the robotics club workshop")

if st.button("Run Pipeline"):
    with st.spinner("Generating subtasks..."):
        subtasks: List[str] = get_subtasks(query)
    st.subheader("Subtasks")
    for i, s in enumerate(subtasks, 1):
        st.write(f"{i}. {s}")

    with st.spinner("Mapping subtasks to actions..."):
        mapped = map_subtasks_to_actions(subtasks)
        mapped = json.loads(mapped) if isinstance(mapped, str) else mapped

    st.subheader("Mapped Actions")
    for i, m in enumerate(mapped, 1):
        emoji = ACTION_EMOJI.get(m.get("action_type", ""), "🔧")
        st.write(f"{i}. {emoji} **{m['action_type']}** — {m['subtask']}")

    with st.spinner("Running agents..."):
        branch = get_branch(groq_model())
        results: List[Dict[str, Any]] = []
        for t in mapped:
            res = branch.invoke(t)
            results.append({
                "subtask": t["subtask"],
                "action_type": t["action_type"],
                "response": getattr(res, "content", str(res)),
            })

    st.subheader("Agent Logs")
    from collections import defaultdict
    grouped_logs = defaultdict(list)
    for r in results:
        grouped_logs[r["action_type"]].append(r)

    for action_type, tasks in grouped_logs.items():
        emoji = ACTION_EMOJI.get(action_type, "🔧")
        st.markdown(f"### {emoji} {action_type}")

        for i, r in enumerate(tasks):
            with st.expander(f"{i+1}. {r['subtask']}", expanded=(i == 0)):
                mock_steps = MOCK_LOGS.get(action_type, ["Processing task...", "✅ Done!"])
                for step in mock_steps:
                    st.write(step)

                st.markdown("---")
                st.markdown(r["response"])