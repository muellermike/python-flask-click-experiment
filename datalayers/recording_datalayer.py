from models.recording import Recording
from datalayers.db import execute


def store_recording(recording: Recording):
    """
    Handle all logic to store a recoring into the data storage.
    """
    sql = "INSERT INTO Recording (TimeToRecording, Recording) VALUES (%s, %s)"

    inserted_recording = execute(sql, (recording.time_to_recording, recording.recording), "INSERT")
    
    return inserted_recording