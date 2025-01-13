from pydantic import BaseModel
from databaseConnection import databaseConnection
import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from Handler.Register import RegisterUser
from Handler.Login import LoginUserClass
from Handler.Users import UserDetails


SECRET_KEY = "e720c4e4ef798f260b3395a09517c4a5672bf0d56d44a34ddcbb3a603d88b493"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

class UserRegisterBodyRequest(BaseModel):
    username: str
    email: str
    password: str

class UserLoginBodyRequest(BaseModel):
    username: str
    password: str


def verifyToken(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # The payload will contain the user information
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def getCurrentUser(token: str = Depends(verifyToken)):
    return token  # Returns the payload of the decoded token

# Initialize database connection
databaseClassObj = databaseConnection()
connection = databaseClassObj.databaseConnect()
cursor = connection.cursor()

@app.post("/fastapis/register/")
async def registerUser(user: UserRegisterBodyRequest):
    username = user.username
    email = user.email
    password = user.password

    if username and email and password:
        RegisterUserOBJ = RegisterUser()
        response = RegisterUserOBJ.register(connection,username, email, password)
        return response
    else:
        raise HTTPException(status_code=400, detail="username, email, and password are required")

@app.post("/fastapis/login/")
async def loginUser(user: UserLoginBodyRequest):
    username = user.username
    password = user.password

    if username and password:
        LoginUserClassOBJ = LoginUserClass()
        response = LoginUserClassOBJ.Login(connection,username,password,SECRET_KEY,ALGORITHM)
        return response
    else:
        raise HTTPException(status_code=400, detail="Username and password are required")



@app.get("/fastapis/getUsersDetails/")
async def getUsersDetails(userid: int, current_user: dict = Depends(getCurrentUser)):
    if userid:
        UserDEtailsobj = UserDEtails()
        response = UserDEtailsobj.UserDetails(connection,userid)
        return response