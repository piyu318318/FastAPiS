
class RegisterUser:
    def register(self,connection,username, email, password):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Users (username, emailid, password) VALUES (%s, %s, %s)",
                       (username, email, password))
        connection.commit()
        return {"status": "200", "message": "User registered successfully"}

