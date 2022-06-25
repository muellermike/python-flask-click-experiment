from models.user import User
from datalayers.db import execute

def store_user(user: User):
    """
    Handle all logic to store a user into the data storage.
    """

    # INSERT Statement for the insertion of a User.
    sql = "INSERT INTO User (ID, UniParkID, Gender, Age) VALUES (%s, %s, %s, %s)"

    inserted_user = execute(sql, (user.id, user.id, user.gender, int(user.age)), "INSERT")
    
    return inserted_user

def get_user(user_id: int):
    """
    Get the user by the id from the database
    """

    # SELECT Statement for the selection of a User.
    sql = "SELECT PK, ID FROM User WHERE PK = %s"

    user = execute(sql, (int(user_id)), "SELECT")

    return user