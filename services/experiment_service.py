from flask import current_app
from datalayers.experiment_datalayer import load_user_experiment, store_experiment, store_experiment_exercises, update_experiment_endtime
from models.experiment import Experiment
from services.exercise_service import get_exercises
from services.user_service import find_user_by_id

def create_experiment(experiment: Experiment):
    """
    implements the logic to create a new experiment. This means that first it is checked whether the user exists
    in the database or not. After positive, random 8 questions of each task are loaded and stored into the database.
    """
    # before creating an experiment setup it is checked whether the user really exists in the database
    if not find_user_by_id(experiment.user):
        return None
    
    # load a number of exercises which have the correct answer left
    lefties = get_exercises("left", current_app.config["NUMBER_OF_EXERCISES"])
    # load a number of exercises which have the correct answer right
    righties = get_exercises("right", current_app.config["NUMBER_OF_EXERCISES"])

    # after both recordings have been stored, the user itself can be stored with the corresponding foreign keys.
    result = store_experiment(experiment)

    # save the generated experiment id into the experiment object
    experiment.id = result

    store_experiment_exercises(lefties + righties, experiment)
    
    return result

def update_experiment(experiment: Experiment):
    """
    implements the logic to update an existing experiment. This means that first it is checked whether the user exists and has this experiment.
    After that all allowed updated are executed.
    """
    # UPDATE endtime of experiment when the endtime is not set yet (logic in SQL Statement)
    result = update_experiment_endtime(experiment)

    return result