class UserDetails:
    def UserDetails(self, connection, userid):
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("SELECT username, userid, password FROM users WHERE userid = %s", (userid,))
            result = cursor.fetchone()
            if not result:
                return {"status": "400", "message": "User not found"}
            username = result["username"]
            userid = result["userid"]
            password = result["password"]
            return {"username": username, "userid": userid, "password": password}
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching user details: {e}")
        finally:
            cursor.close()
