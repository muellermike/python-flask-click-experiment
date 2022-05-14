import six

from flask import Blueprint, request, jsonify
from models.recording import Recording  # noqa: E501
import util
from services.recording_service import add_recording_to_exercise

recordings_endpoint = Blueprint('recordings_endpoint', __name__)

@recordings_endpoint.route('/recordings', methods=['PUT'])
def add_recording():  # noqa: E501
    """Add a new recording to a experiment exercise

     # noqa: E501

    :param body: Recording object that needs to be added to a experiment exercise.
    :type body: dict | bytes

    :rtype: None
    """
    body = Recording.from_dict(request.get_json())  # noqa: E501

    recording_id = add_recording_to_exercise(body)
    
    return jsonify(recording_id)
