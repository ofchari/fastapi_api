from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

class Log(BaseModel):
    name: str
    password: str

class Form(BaseModel):
    id: int
    name: str
    date: str
    company: str

class Dashboard(BaseModel):
    id : int
    name : str
    country : str
    company : str
    phone_number : int
    address : str
