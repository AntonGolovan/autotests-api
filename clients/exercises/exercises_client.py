from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class Exercise(TypedDict):
    """
    Описание структуры Exercise
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получения списка заданий
    """
    courseId: str


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения задания
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка заданий
    """
    exercises: list[Exercise]


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания
    """
    exercise: Exercise


class UpdateExerciseResponse(TypedDict):
    """
    Описание структуры ответа на обновление задания
    """
    exercise: Exercise


class CreateExerciseRequestDict(TypedDict):
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


class UpdateExerciseRequestDict(TypedDict):
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

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка exercises

        :param: Словарь с courseId.
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url="/api/v1/exercises", params=query)

    def get_exercise_api(self, exercises_id: str) -> Response:
        """
        Метод получения задания по exercises_id

        :param exercises_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url=f"/api/v1/exercises/{exercises_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания задания

        :param: create_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url="/api/v1/exercises", json=request)

    def update_exercise_api(self, request: UpdateExerciseRequestDict, exercise_id: str) -> Response:
        """
        Метод для изменения задания  по exercise_id

        :param: update_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :param: exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания по exercise_id

        :param exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url=f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request=request)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query=query)
        return response.json()

    def get_exercise(self, exercises_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercises_id=exercises_id)
        return response.json()

    def update_exercise(self, request: UpdateExerciseRequestDict, exercises_id: str) -> UpdateExerciseResponse:
        response = self.update_exercise_api(request=request, exercise_id=exercises_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param
    :return Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))