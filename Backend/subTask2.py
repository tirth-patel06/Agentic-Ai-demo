from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

# Convert the task into samll subtask
model1 = ChatGroq(model="llama3-70b-8192", temperature=0.3)

subtask_prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant that breaks down tasks into clear subtasks.
    Task: "{query}"
    Break it down into 3-6 sequential subtasks But also take care that each subtask has no other subtask divide it in major subtask.
    Return them as just a simple numbered list no other header or footer content as we only need the task list only.
""")

# Generate the subtak into array of json so that we can decide further which model is need to call
model2 = ChatGroq(model="llama3-70b-8192", temperature=0)
parser = JsonOutputParser()

map_prompt = ChatPromptTemplate.from_template("""
You are an AI that maps subtasks into structured actions for a multi-agent system. 

For each subtask below, return a JSON object with:
- "subtask": original text
- "action_type": one of [send_mail, book_classroom, generate_poster, arrange_equipment, schedule_meeting, announce_event, execute_task]
- "description": short note on how this action would be performed

Also take care the whole output is array of this json no other header or foorter is required just the array of json for each task is in the output
Subtasks:
{subtasks}
""")

# funtion to use the model and call

def process_query(query: str):
    """Main backend function: query → subtasks → JSON mapping"""
    # Step 1: Generate subtasks
    chain1 = subtask_prompt | model1
    response1 = chain1.invoke({"query": query})
    lines = response1.content.strip().split("\n")
    subtasks = [l.lstrip("123456.-•*: ").strip() for l in lines if l.strip()]

    # Step 2: Generate structured JSON
    chain2 = map_prompt | model2 | parser
    response2 = chain2.invoke({"subtasks": "\n".join(subtasks)})

    return subtasks, response2

print(process_query("Organize a robotics workshop"))