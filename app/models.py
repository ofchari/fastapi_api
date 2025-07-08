from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

         
    #   Login User Model 
class Log(BaseModel):
    name: str
    password: str


    #  Form Data 
class Form(BaseModel):
    id : int
    name : str 
    date : str
    company : str
