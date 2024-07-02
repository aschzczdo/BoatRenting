import bcrypt
from models.db import postgres_connection

def register_user(username, email, password, name, surname):
    conn = postgres_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Generate a salt and hash the password using bcrypt
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            # Insert user data into the database
            query = """
            INSERT INTO "User" (username, email, password, salt, role_id, account_status_id)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING user_id;
            """
            cursor.execute(query, (username, email, hashed_password, salt, 1, 1))
            user_id = cursor.fetchone()[0]

            # Insert profile data into the database
            query = """
            INSERT INTO "Profile" (user_id, name, surname)
            VALUES (%s, %s, %s);
            """
            cursor.execute(query, (user_id, name, surname))

            conn.commit()
            return True  # Registration successful

        except Exception as e:
            print(f"Error registering user: {e}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    return False  # Registration failed
