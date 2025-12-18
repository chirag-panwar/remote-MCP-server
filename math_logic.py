# Good, this error is actually confirming the exact root cause.
# Let’s fix it cleanly and permanently, not with hacks.

# ❌ Why this error keeps happening
# TypeError: 'FunctionTool' object is not callable
# What this means (plain English)
# subtract is NOT a normal Python function
# It is a FastMCP FunctionTool
# FunctionTools are metadata objects, not callable functions
# So this will never work:
# subtract(a, b)   ❌
# As long as subtract comes from @mcp.tool(), it is not callable.

# math_logic.py

def addition(a: float, b: float) -> float:
    return a + b

def subtraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
