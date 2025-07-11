from fastapi import APIRouter
from .models import User,Log,Form,Dashboard
from .database import user_collection, log_collection, form_collection,dashboard_collection
from .helpers import user_helper, log_helper, form_helper,dashboard_helper

router = APIRouter()

@router.post("/create-user")
async def create_user(user: User):
    user_dict = user.dict()
    new_user = await user_collection.insert_one(user_dict)
    created_user = await user_collection.find_one({"_id": new_user.inserted_id})
    return {
        "message": "User created successfully!",
        "user": user_helper(created_user)
    }

@router.post("/auth_login")
async def auth_login(log: Log):
    log_dict = log.dict()
    new_log = await log_collection.insert_one(log_dict)
    created_log = await log_collection.find_one({"_id": new_log.inserted_id})
    return {
        "data": "Created Successfully",
        "log": log_helper(created_log)
    }

@router.post("/fields_data")
async def fields_data(fie: Form):
    fie_dict = fie.dict()
    new_fie = await form_collection.insert_one(fie_dict)
    created_fie = await form_collection.find_one({"_id": new_fie.inserted_id})
    return {
        "data": "Created Data Successfully",
        "fie": form_helper(created_fie)
    }

@router.post("/dashboard_data")
async def dashboard_data(dass : Dashboard):
    dass_dict = dass.dict()
    new_dass = await dashboard_collection.insert_one(dass_dict)
    created_dass = await dashboard_collection.find_one({"_id" : new_dass.inserted_id})
    return{
        "message" : "Created Sucessfully",
        "dass" : dashboard_helper(created_dass) 
    }


        #  Get Login API Data //
@router.get("/auth_login_data")
async def logdta():
    created_log = await log_collection.find_one()
    return {
        "data": "Fetched Successfully",
    "log": log_helper(created_log)
    }


        #   Get API for Form Fields data //
@router.get("/form_fieldss_data")
async def form_fieldss_data():
    created_fie = await form_collection.find_one()
    return {
        "data": "fetched Data Successfully",
        "fie": form_helper(created_fie)
    }


         
@router.get("/dashboard_get")
async def dashboard_get():
    created_dass = await dashboard_collection.find_one()
    return {
        "message" : "fetched data Sucessfully",
        "das" : dashboard_helper(created_dass) 
    }
