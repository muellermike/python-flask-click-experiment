from models.user import User
from datalayers.db import execute
import base64

def store_user(user: User):
    """
    Handle all logic to store a user into the data storage.
    """

    # write base64 string to mp3 file
    """mp3_gender_data = base64.b64decode(user.gender.recording)
    newFileGender = open("gender.mp3", "wb")
    newFileGender.write(mp3_gender_data)
    mp3_age_data = base64.b64decode(user.age.recording)
    newFileAge = open("age.mp3", "wb")
    newFileAge.write(mp3_age_data)"""

    # INSERT Statement for the insertion of a User.
    sql = "INSERT INTO User (ID, UniParkID, GenderRecordingFK, AgeRecordingFK) VALUES (%s, %s, %s, %s)"

    inserted_user = execute(sql, (user.id, user.id, user.gender.id, user.age.id), "INSERT")
    
    return inserted_user

def get_user(user_id: int):
    """
    Get the user by the id from the database
    """

    # SELECT Statement for the selection of a User.
    sql = "SELECT PK, ID FROM User WHERE PK = %s"

    user = execute(sql, (int(user_id)), "SELECT")

    return user