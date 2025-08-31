from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class Exercises(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExerciseResponseDict(TypedDict):
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercises]


class CreateExerciseResponseDict(TypedDict):
    exercises: Exercises


class UpdateExerciseResponse(TypedDict):
    exercise: Exercise


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание exercises
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на изменение exercises
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self) -> Response:
        """
        Метод получения всех exercises

        :return: Объект Response с данными ответа.
        """
        return self.client.get(url="/api/v1/exercises")

    def get_exercise_api(self, exercises_id: str) -> Response:
        """
        Метод получения конкретного exercise по id

        :param exercises_id: Идентификатор exercises
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url=f"/api/v1/exercises/{exercises_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод для создания exercises

        :param: create_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url="/api/v1/exercises", json=request)

    def update_exercise_api(self, request: UpdateExercisesRequestDict, exercise_id: str) -> Response:
        """
        Метод для изменения exercises

        :param: update_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :param: exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления exercises по exercise_id

        :param exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url=f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request=request)
        return response.json()

    def get_exercises(self) -> GetExercisesResponseDict:
        response = self.get_exercises_api()
        return response.json()

    def get_exercise(self, exercises_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercises_id=exercises_id)
        return response.json()

    def update_exercise(self, request: UpdateExercisesRequestDict, exercises_id: str) -> UpdateExerciseResponse:
        response = self.update_exercise_api(request=request, exercise_id=exercises_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param
    :return Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))