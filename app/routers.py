from fastapi import APIRouter
from .models import User
from .models import Log
from .models import Form

router = APIRouter()

#    Create User //
@router.post("/create-user")
def create_user(user: User):
    return {
        "message": "User created successfully!",
        "user": {
            "name": user.name,
            "age": user.age,
            "email": user.email
        }
    }

#     Auth Login Data //
@router.post("/auth_login")
def auth_login(log : Log):
    return {
        "data" : "Created Successfully",
        "log" : {
            "username" : log.name,
            "password" : log.password
        }
    }

#      Texformfield Data //
@router.post("/fields_data")
def fields_data(fie : Form):
    return{
        "data" : "Created Data Successfully",
        "fie" : {
            "id" : fie.id,
            "name" : fie.name,
            "date" : fie.date,
            "company" : fie.company
        }
    }

    #  Get API //
@router.get("/")
def login():
    return {"message": "Hi FastAPI Dev"}


#    Post API //

@router.get("/fields_data")
def formfields():
    return {
        "message" : {
            
        "id": 1,
        "name": "Hari krish",
        "date": "08/07/2025",
        "company": "Regenbt"
    }
        }
    

