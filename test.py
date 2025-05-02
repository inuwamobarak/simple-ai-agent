import uuid
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from tools import say_hello, get_user_age

load_dotenv()

# Initialize memory and the model
memory = MemorySaver()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Create a react agent with the model, tools, and memory
app = create_react_agent(
    model,
    tools=[say_hello, get_user_age],
    checkpointer=memory,
)

# The thread id is a unique key that identifies this conversation.
thread_id = uuid.uuid4()
config = {"configurable": {"thread_id": thread_id}}

# Send an initial message asking the AI about the user's age
input_message = HumanMessage(content="Say hello to Benjamin")
for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
    event["messages"][-1].pretty_print()

# Ask the AI if it remembers the user's name
input_message = HumanMessage(content="do you remember my name?")
for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
    event["messages"][-1].pretty_print()