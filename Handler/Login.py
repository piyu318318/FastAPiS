from fastapi import HTTPException
import datetime
import jwt


class LoginUserClass:
    def Login(self, connection, username, password, SECRET_KEY, ALGORITHM):
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
        dbUser = cursor.fetchone()

        if dbUser and dbUser[2] == password:
            userData = {"username": username}

            # Create access token
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
            toEncode = userData.copy()
            toEncode.update({"exp": expire})
            access_token = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)

            # Create refresh token
            refreshExpire = datetime.datetime.utcnow() + datetime.timedelta(days=7)
            refreshToEncode = userData.copy()
            refreshToEncode.update({"exp": refreshExpire})
            refresh_token = jwt.encode(refreshToEncode, SECRET_KEY, algorithm=ALGORITHM)

            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")