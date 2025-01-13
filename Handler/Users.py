class UserDetails:
    def UserDetails(self, connection, userid):
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT username, userid, password FROM users WHERE userid = %s", (userid,))
            result = cursor.fetchone()
            if not result:
                raise ValueError("User not found")
            username = result["username"]
            userid = result["userid"]
            password = result["password"]
            return {"username": username, "userid": userid, "password": password}
        except Exception as e:
            # Handle potential exceptions and raise meaningful errors
            raise RuntimeError(f"An error occurred while fetching user details: {e}")
        finally:
            cursor.close()  # Always close the cursor
