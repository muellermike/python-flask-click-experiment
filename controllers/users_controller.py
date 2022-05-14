from flask import Blueprint, abort, request
from models.recording import Recording
from models.user import User  # noqa: E501
from services import user_service
import util

users_endpoint = Blueprint('users_endpoint', __name__)

@users_endpoint.route('/users', methods=['POST'])
def add_user(body):  # noqa: E501
    """Add a new user as experiment participant

     # noqa: E501

    :param body: User object that needs to be added as experiment participant.
    :type body: dict | bytes

    :rtype: None
    """
    body = User.from_dict(request.get_json())  # noqa: E501

    print("test build pipeline")
    
    if is_valid(body):
        return body
        result = user_service.add_user(body)
    else:
        abort(400, "Please provide all required attributes.")
    
    return result

def is_valid(user: User):
    """
    Checks all the params whether they are all available or not
    """
    isValid = False
    if user.id and user.gender.recording and user.gender.time_to_recording and user.age.recording and user.age.time_to_recording:
        isValid = True

    return isValid