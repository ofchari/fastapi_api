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

pip install -r requirements.txt

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
.\env\Scripts\Activate.ps1
uvicorn main:app --reload




                                        /// Mongodb Config to fastAPI ///

```
'mongod' is not recognized as an internal or external command
```

means **MongoDB is not added to your system's PATH** or **not installed yet**.

Let’s fix this in 3 quick steps:

---

## ✅ Step 1: Check If MongoDB Is Installed

### Go to:

```
C:\Program Files\MongoDB\Server\6.0\bin\
```

> (If you don’t see this, MongoDB isn’t installed yet — go to Step 2)

If you **see files like** `mongod.exe`, `mongo.exe`, etc., then MongoDB is installed — just not in your system PATH.

---
pip install motor

## ✅ Step 2: (If Not Installed) Install MongoDB

### 1. Download MongoDB Community Server MSI:

👉 [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

* Choose:

  * **Windows**
  * **MSI**
  * Version: LTS or Current (e.g., 6.0)

### 2. Run Installer:

* Choose **Complete Setup**
* ✔️ Make sure to **Install MongoDB as a Service**
* ✔️ Optionally install **MongoDB Compass** (GUI)

Once installed, check `C:\Program Files\MongoDB\Server\6.0\bin\`

---

## ✅ Step 3: Add MongoDB to PATH (If Already Installed)

### 1. Open System Environment Variables:

* Press `Windows Key`
* Search: **"Environment Variables"**
* Open: **Edit system environment variables**
* Click: **Environment Variables**

### 2. Under **System Variables**:

* Find `Path`
* Click **Edit**
* Click **New**
* Add this line (adjust if version differs):

```
C:\Program Files\MongoDB\Server\6.0\bin
```

### 3. Click **OK** on all windows.

---

## ✅ Step 4: Restart Command Prompt

Close and reopen `cmd`, then test:

```bash
mongod
```

It should now start the MongoDB server.

---

## ✅ Optional: Start MongoDB Service

If you installed as a service, run:

```bash
net start MongoDB
```

Then test the shell:

```bash
mongo
```

---

### ✅ After That, Your FastAPI Project Will Work with This Connection:

```python
MONGO_DETAILS = "mongodb://localhost:27017"



Clean separation:

models.py = input format

helpers.py = output format

database.py = DB connection

routes.py = logic



