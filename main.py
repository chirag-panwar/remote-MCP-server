from fastmcp import FastMCP
import math_logic

mcp = FastMCP("math-mcp")

@mcp.tool()
def add(a: float, b: float) -> float:
    return math_logic.addition(a, b)

@mcp.tool()
def subtract(a: float, b: float) -> float:
    return math_logic.subtraction(a, b)

@mcp.tool()
def multiply(a: float, b: float) -> float:
    return math_logic.multiplication(a, b)

@mcp.tool()
def divide(a: float, b: float) -> float:
    return math_logic.division(a, b)

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
