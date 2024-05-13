import bcrypt
from models.db import mysql_connection
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

def check_password(plain_password, hashed_password):
    # Check if the plain password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

def login_user(username, password):
    conn = mysql_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Retrieve the hashed password and salt from the database
            query = "SELECT password, salt FROM User WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                hashed_password, salt = result
                hashed_password = hashed_password.encode('utf-8')  # Convert to bytes

                # Use the retrieved salt to verify the password
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    print("Logged in")
                    return True  # Login successful
                else:
                    return False  # Incorrect password
            else:
                return False  # User not found

        except Exception as e:
            print(f"Error logging in user: {e}")

        finally:
            cursor.close()
            conn.close()

    return False  # Login failed