# coding: utf-8

from __future__ import absolute_import

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util


class ExerciseAnswer(Model):

    def __init__(self, answer: str=None, experiment_id: int=None, user_id: int=None, exercise_id: int=None):  # noqa: E501
        """ExerciseAnswer - a model defined in Swagger

        :param answer: The answer of this Experiment Exercise.  # noqa: E501
        :type answer: string
        :param experiment_id: The experiment_id of this Recording.  # noqa: E501
        :type experiment_id: int
        :param user_id: The user_id of this Recording.  # noqa: E501
        :type user_id: int
        :param exercise_id: The exercise_id of this Recording.  # noqa: E501
        :type exercise_id: int
        """
        self.swagger_types = {
            'id': int,
            'answer': str,
            'experiment_id': int,
            'user_id': int,
            'exercise_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'recording': 'recording',
            'experiment_id': 'experimentId',
            'user_id': 'userId',
            'exercise_id': 'exerciseId'
        }

        self._id = id
        self._answer = answer
        self._experiment_id = experiment_id
        self._user_id = user_id
        self._exercise_id = exercise_id

    @classmethod
    def from_dict(cls, dikt) -> 'ExerciseAnswer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExerciseAnswer of this ExerciseAnswer.  # noqa: E501
        :rtype: ExerciseAnswer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def answer(self) -> str:
        """Gets the answer of this ExerciseAnswer.


        :return: The answer of this ExerciseAnswer.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        """Sets the anser of this ExerciseAnswer.


        :param answer: The answer of this ExerciseAnswer.
        :type answer: str
        """
        if answer is None:
            raise ValueError("Invalid value for `answer`, must not be `None`")  # noqa: E501

        self._answer = answer

    @property
    def experiment_id(self) -> int:
        """Gets the experiment_id of this ExerciseAnswer.


        :return: The experiment_id of this ExerciseAnswer.
        :rtype: int
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id: int):
        """Sets the experiment_id of this ExerciseAnswer.


        :param experiment_id: The experiment_id of this ExerciseAnswer.
        :type experiment_id: int
        """

        self._experiment_id = experiment_id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this ExerciseAnswer.


        :return: The user_id of this ExerciseAnswer.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this ExerciseAnswer.


        :param user_id: The user_id of this ExerciseAnswer.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def exercise_id(self) -> int:
        """Gets the exercise_id of this ExerciseAnswer.


        :return: The exercise_id of this ExerciseAnswer.
        :rtype: int
        """
        return self._exercise_id

    @exercise_id.setter
    def exercise_id(self, exercise_id: int):
        """Sets the exercise_id of this ExerciseAnswer.


        :param exercise_id: The exercise_id of this ExerciseAnswer.
        :type exercise_id: int
        """

        self._exercise_id = exercise_id