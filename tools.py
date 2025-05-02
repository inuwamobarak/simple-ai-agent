from langchain.tools import tool

@tool
def say_hello(name: str) -> str:
    """Greets a person by name."""
    return f"Hello, {name}!"

@tool
def get_user_age(name: str) -> str:
    """Use this tool to find the user's age."""
    if "bob" in name.lower():
        return "42 years old"
    return "41 years old"
