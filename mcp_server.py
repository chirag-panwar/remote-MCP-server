# mcp_server.py
from fastmcp import FastMCP
from math_logic import addition, subtraction, multiplication, division

mcp = FastMCP(name="Math MCP Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return addition(a, b)

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return subtraction(a, b)

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return multiplication(a, b)

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    return division(a, b)

if __name__ == "__main__":
    mcp.run()
