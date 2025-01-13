from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from databaseConnection import databaseConnection

app = FastAPI()

class UserRegistration(BaseModel):
    username: str
    email: str
    password: str

databaseClassObj = databaseConnection()
connection = databaseClassObj.databaseConnect()
cursor = connection.cursor()

@app.post("/fastapis/register/")
async def registerUser(user: UserRegistration):
    username = user.username
    email = user.email
    password = user.password

    if username and email and password:
        cursor.execute("INSERT INTO Users (username, emailid, password) VALUES (%s, %s, %s)",
                       (username, email, password))
        connection.commit()
        return {"status": "200", "message": "User registered successfully"}
    else:
        raise HTTPException(status_code=400, detail="username, email, and password are required")
