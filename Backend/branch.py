from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda

send_mail_prompt = ChatPromptTemplate.from_template("""
You are handling a send_mail task.
Subtask: {subtask}
Description: {description}
Generate the email content or next step.

Make sure:
- Use simple formal English.
- Keep it concise (max 6-8 sentences).
- Include subject line and email body separately.
""")

book_classroom_prompt = ChatPromptTemplate.from_template("""
You are an assistant that drafts a classroom booking request for the college administration.
Subtask: {subtask}

Output:
- A short formal request (suitable to send to administration).
- Include date, time, and purpose placeholders.
""")

generate_poster_prompt = ChatPromptTemplate.from_template("""
You are a poster content generator for college club events.
Subtask: {subtask}

Output:
- Event title
- Date, Time, Venue placeholders
- Key highlights (3-4 points)
- Call-to-action line (e.g., "Join us!", "Register now!")
""")

arrange_equipment_prompt = ChatPromptTemplate.from_template("""
You are a resource checklist assistant for a college workshop.
Subtask: {subtask}

List the equipment, tools, and resources required for execution in bullet points.
""")

schedule_meeting_prompt = ChatPromptTemplate.from_template("""
You are a scheduling assistant for a college club.
Subtask: {subtask}

Output:
- Meeting agenda
- Suggested date & time (placeholder format)
- Participants needed
""")

execute_task_prompt = ChatPromptTemplate.from_template("""
You are an execution tracking assistant.
Subtask: {subtask}

Output:
- A short action plan (2-3 steps)
- Success criteria for completion
""")

generate_form_prompt = ChatPromptTemplate.from_template("""
You are a form generator assistant for college club events.
Subtask: {subtask}

Generate:
- Form title
- Form type (Registration / Feedback)
- Suggested fields (Name, Email, Roll no, etc.)
""")

generate_certificate_prompt = ChatPromptTemplate.from_template("""
You are a certificate content generator for college workshops/events.
Subtask: {subtask}

Output certificate text with placeholders:
- Certificate Title
- "This is to certify that [Name]..."
- Event Name, Date, Venue placeholders
- Signature placeholders (Faculty, Club Head)
""")

default_prompt = ChatPromptTemplate.from_template("""
No specific action type matched.
Subtask: {subtask}
Description: {description}
Provide generic guidance.
""")

def get_branch(model):
    return RunnableBranch(
        (lambda x: x["action_type"] == "send_mail", send_mail_prompt | model),
        (lambda x: x["action_type"] == "book_classroom", book_classroom_prompt | model),
        (lambda x: x["action_type"] == "generate_poster", generate_poster_prompt | model),
        (lambda x: x["action_type"] == "arrange_equipment", arrange_equipment_prompt | model),
        (lambda x: x["action_type"] == "schedule_meeting", schedule_meeting_prompt | model),
        (lambda x: x["action_type"] == "execute_task", execute_task_prompt | model),
        (lambda x: x["action_type"] == "generate_form", generate_form_prompt | model),
        (lambda x: x["action_type"] == "generate_certificate", generate_certificate_prompt | model),
        default_prompt | model   # 👈 no "default=" here
    )