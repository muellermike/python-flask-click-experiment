from datalayers.db import execute

def load_next_random_exercise(experimentId: int, userId: int):
    """
    Load the next random exercise which has not been answered yet.
    """
    sql = "SELECT ex.PK, Question, Mimetype, EncodedString FROM Exercise as ex JOIN ExperimentExercise as ee ON ex.PK = ee.ExerciseFK JOIN Experiment as e ON ee.ExperimentFK = e.PK WHERE ee.ExperimentFK = %s AND e.UserFK = %s AND ee.RecordingFK IS NULL ORDER BY RAND() LIMIT 1"
    
    loaded_exercise = execute(sql, (experimentId, userId), "SELECT")
    
    if not loaded_exercise:
        return None

    return loaded_exercise[0]

def load_random_exercises(answer: str, number_of_exercises: int):
    """
    Load all exercises which have the correct answer provided as parameter
    """
    # load n exercises which have the answer provided as parameter in a random order
    sql = "SELECT PK FROM Exercise WHERE CorrectAnswer = %s ORDER BY RAND() LIMIT %s"

    loaded_exercises = execute(sql, (answer, int(number_of_exercises)), "SELECT")
    
    return loaded_exercises