def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "age": user["age"],
        "email": user["email"]
    }

def log_helper(log) -> dict:
    return {
        "data" :{
               "id": str(log["_id"]),
        "password": log["password"],
         "name": log["name"],

        }
    }

def form_helper(form) -> dict:
    return {
        "id": form["id"],
        "name": form["name"],
        "date": form["date"],
        "company": form["company"]
    }

def dashboard_helper(dash) -> dict:
    return {
        "message" : {
        "id" : dash["id"],
        "name" : dash["name"],
        "country" : dash["country"],
        "company" : dash["company"],
        "phone_number" : dash["phone_number"],
        "address" : dash["address"]
        }
    }
