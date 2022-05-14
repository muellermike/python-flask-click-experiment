import random
from datalayers.db import execute
from models.experiment import Experiment
from models.recording import Recording

def store_experiment(experiment: Experiment):
    """
    Store experiment with the information into the database
    """
    sql = "INSERT INTO Experiment (UserFK, Start) VALUES (%s, %s)"

    experiment_id = execute(sql, (experiment.user, experiment.start), "INSERT")
    
    return experiment_id

def store_experiment_exercises(exercises, experiment: Experiment):
    """
    Stores all experiment exercises into the database
    """
    # sql statement to insert multi rows
    sql = "INSERT INTO ExperimentExercise (ExperimentFK, ExerciseFK) VALUES (%s, %s)"

    # create list with the experiment id and the exercise id to insert into the database
    experiment_exercises = list([(experiment.id, e["PK"]) for e in exercises])
    random.shuffle(experiment_exercises)
    
    # execute the INSERT MANY statement
    execute(sql, (experiment_exercises), "INSERT MANY")

    return True

def update_experiment_exercise(recording: Recording):
    """
    Updates the experiment exercise with the recording foreign key
    """
    # sql statement to update a row
    sql = "UPDATE ExperimentExercise SET RecordingFK = %s WHERE ExperimentFK = %s AND ExerciseFK = %s"

    # execute the UPDATE statement
    execute(sql, (recording.id, recording.experiment_id, recording.exercise_id), "UPDATE")

    return True

def load_user_experiment(experiment_id: int, user_id: int):
    """
    Loads a specific experiment for a specific user
    """
    # sql statement for the experiment load
    sql = "SELECT * FROM Experiment WHERE PK = %s AND UserFK = %s"

    # execute sql statement
    result = execute(sql, (experiment_id, user_id), "SELECT")

    if not result:
        return None

    return result

def load_experiment_exercise(experiment_id: int, exercise_id: int):
    """
    Loads a specific experiment exercise by experiment id and exercise id
    """
    # sql statement for the selection
    sql = "SELECT * FROM ExperimentExercise WHERE ExperimentFK = %s AND ExerciseFK = %s"

    # execute sql statement
    result = execute(sql, (experiment_id, exercise_id), "SELECT")

    return result