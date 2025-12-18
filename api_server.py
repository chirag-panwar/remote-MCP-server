from fastapi import FastAPI, HTTPException
import math_logic

app = FastAPI(title="Math API")

@app.get("/add")
def add(a: float, b: float):
    return {"result": math_logic.addition(a, b)}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": math_logic.subtraction(a, b)}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": math_logic.multiplication(a, b)}

@app.get("/divide")
def divide(a: float, b: float):
    try:
        return {"result": math_logic.division(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
