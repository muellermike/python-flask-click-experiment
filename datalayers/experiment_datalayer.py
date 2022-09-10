import random
from datalayers.db import execute
from models.exercise_answer import ExerciseAnswer
from models.experiment import Experiment

def store_experiment(experiment: Experiment):
    """
    Store experiment with the information into the database
    """
    sql = "INSERT INTO Experiment (UserFK, Start, ImageTime) VALUES (%s, %s, %s)"

    experiment_id = execute(sql, (experiment.user, experiment.start, experiment.image_time), "INSERT")
    
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

def update_experiment_exercise(exercise: ExerciseAnswer):
    """
    Updates the experiment exercise with the answer
    """

    if exercise.full_text_answer is not None:
        if exercise.full_text_answer.lower() == "there are more dots on the right side":
            exercise.answer = "right"
        elif exercise.full_text_answer.lower() == "there are more dots on the left side":
            exercise.answer = "left"
        else:
            exercise.answer = "unclear"
        
        sql = "UPDATE ExperimentExercise SET Answer = %s, FullTextAnswer = %s, AnswerStoredTimestamp = %s, TimeToClick = %s, TimeToSubmit = %s WHERE ExperimentFK = %s AND ExerciseFK = %s"
        execute(sql, (exercise.answer, exercise.full_text_answer, exercise.time, exercise.time_to_click, exercise.time_to_submit, exercise.experiment_id, exercise.exercise_id), "UPDATE")
    else:
        sql = "UPDATE ExperimentExercise SET Answer = %s, AnswerStoredTimestamp = %s, TimeToClick = %s, TimeToSubmit = %s WHERE ExperimentFK = %s AND ExerciseFK = %s"
        execute(sql, (exercise.answer, exercise.time, exercise.time_to_click, exercise.time_to_submit, exercise.experiment_id, exercise.exercise_id), "UPDATE")

    return True

def update_experiment_endtime(experiment: Experiment):
    """
    Updates the experiment endtime
    """
    # sql statement to update experiment endtime
    sql = "UPDATE Experiment SET End = %s WHERE PK = %s AND UserFK = %s AND End IS NULL"

    # execute the UPDATE statement
    execute(sql, (experiment.end, experiment.id, experiment.user), "UPDATE")

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