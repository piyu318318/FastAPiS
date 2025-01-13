
class RegisterUser:
    def register(self,connection,username, email, password):
        cursor = connection.cursor()
        try:
            cursor.execute("select * from users where email = %s",email)
            result = cursor.fetchone()
            if result:
                return {"status": "400", "message": "already registered using this email"}

            cursor.execute("select * from users where email = %s", username)
            result = cursor.fetchone()
            if result:
                return {"status": "400", "message": "This Username already is in used please use another Username"}

            cursor.execute("INSERT INTO Users (username, emailid, password) VALUES (%s, %s, %s)",
                           (username, email, password))
            connection.commit()
            return {"status": "200", "message": "User registered successfully"}
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching user details: {e}")
        finally:
            cursor.close()
