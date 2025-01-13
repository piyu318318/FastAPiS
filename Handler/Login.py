from fastapi import HTTPException
import datetime
from typing import Optional
import jwt


class LoginUserClass:
    def Login(self, connection, username, password, SECRET_KEY, ALGORITHM):
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
        db_user = cursor.fetchone()

        if db_user and db_user[2] == password:  # Assuming plain-text password storage (not secure)
            user_data = {"username": username}

            # Create access token
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
            to_encode = user_data.copy()
            to_encode.update({"exp": expire})
            access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

            # Create refresh token
            refresh_expire = datetime.datetime.utcnow() + datetime.timedelta(days=7)
            refresh_to_encode = user_data.copy()
            refresh_to_encode.update({"exp": refresh_expire})
            refresh_token = jwt.encode(refresh_to_encode, SECRET_KEY, algorithm=ALGORITHM)

            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")