python --version

Create Project : 
mkdir fastapi_project
cd fastapi_project

Create Virtual Env : 
python -m venv env
 activate : .\env\Scripts\activate

FastAPI : 
pip install fastapi

Uvicorn : 
pip install uvicorn 


Create main file : 
main.py
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Dev!"}

@app.get("/hello")
def say_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@app.get("/login")
def log():
    return {"data": "Fast API Data"}

Run : 
uvicorn main:app --reload

