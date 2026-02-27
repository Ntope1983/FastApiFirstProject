from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI 🚀"}


@app.get("/ping")
def read_root():
    return {"message": "pong"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}"}


@app.get("/add")
def add_numbers(a: int, b: int, c: int):
    return {"The sum of two numbers is": f" {a + b + c}"}


@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result": f" {a * b}"}


@app.get("/hello_user")
def greet(name: str, age: int):
    return {"Message": f" Hello {name}. You are {age} years old"}

@app.get("/average")
def greet(numbers:list):
    return {"Message": f" Hello {name}. You are {age} years old"}