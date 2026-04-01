from fastapi import FastAPI,Depends,HTTPException
from jose import jwt   
from passlib.context import CryptContext
app = FastAPI()
#-------------- secret key use for jwt---⚙️ 
SECRET_KEY= "mysecretkey"         #It means👉 combine data + secret key/👉 hash it securely
ALGORITHM =  "HS256"
# ---------------------------fake data base ----------------------------------
user_db = {"admin" : {"username": "admin",  "password": "123" , "role": "admin"},
           "user":{"username": "user", "password":"456" , "role":"user"}
           }
# password hashing
``
# -------------------------------login API -------------------------------
@app.post("/login")                            #--------    http://127.0.0.1:8000/docs  ---------------
def login(username:str,password:str):
    user = user_db.get(username)
    if not user or user["password"] != password:
       raise HTTPException(status_code=401 ,detail = "invalid credentials") 
    token_data = {"username": username, "role":user["role"] }
    token = jwt.encode(token_data , SECRET_KEY ,algorithm=ALGORITHM )
    return {"access_token":token}
#------------------------ ROLE CHECK FUNCTION ----------------------------------
def get_current_user(token:str):
    try:                                                                                                        
        payload = jwt.decode(token ,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401 ,detail = "invalid credentials")
def role_required(required_role: str):
    def checker(user: dict = Depends(get_current_user)):
            if user["role"] != required_role:
                raise HTTPException(status_code=401, detail="invalid credentials")
            return user
    return checker
@app.get("/admin-data")     
#----------------👉 Control who can access which API based on their role -------------------------
def admin_data(user: dict = Depends(role_required("admin"))):
    return {"message": f"Hello {user['username']}, you are an admin!"}

@app.get("/user-data")
def user_data(user: dict = Depends(role_required("user"))):
    return {"message": f"Hello {user['username']}, you are a regular user!"}
           