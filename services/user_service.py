from flask import current_app
from datalayers.recording_datalayer import store_recording
from models.user import User
from datalayers.user_datalayer import get_user, store_user

def add_user(user: User):
    """
    checks all parameters and adds user to the storage
    """
    # before storing the user both recordings (age and gender) have to be saved
    age_id = store_recording(user.age)
    gender_id = store_recording(user.gender)
    user.age.id = age_id
    user.gender.id = gender_id

    # after both recordings have been stored, the user itself can be stored with the corresponding foreign keys.
    result = store_user(user)
    return result

def find_user_by_id(user_id: int):
    """
    Searches for a userId in the database to check if a user exists.
    """

    result = get_user(user_id)
    if(len(result) == 1):
        return True

    return False