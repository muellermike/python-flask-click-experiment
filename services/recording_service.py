from datalayers.experiment_datalayer import load_experiment_exercise, load_user_experiment, update_experiment_exercise
from datalayers.recording_datalayer import store_recording
from models.recording import Recording

def add_recording_to_exercise(recording: Recording):
    """
    checks all parameter and stores the recording then
    """
    # before storing the recording it is checked, whether this user_experiment exists.
    user_ex = load_user_experiment(recording.experiment_id, recording.user_id)
    
    if user_ex is None:
        # if the experiment for the user doesn't exist, return None
        return None
    
    # check that this exercise has not been answered yet
    ex = load_experiment_exercise(recording.experiment_id, recording.exercise_id)

    # if exercise hasn't been found or RecordingFK is already filled, than return None
    if not ex or ex[0]["RecordingFK"] is not None:
        return None
    
    # if everythind is fine until now, store the recording into the recording table
    stored_recording_id = store_recording(recording)

    # add the new recording id to the exerpiment exercise
    recording.id = stored_recording_id

    # set the recording foreign key to the current experiment exercise
    update_experiment_exercise(recording)

    return recording.id
