from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


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
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises(self) -> Response:
        """
        Метод получения всех exercises

        :return: Объект Response с данными ответа.
        """
        return self.client.get(url="/api/v1/exercises")

    def get_exercises_by_id(self, exercises_id: str) -> Response:
        """
        Метод получения конкретного exercises по exercise_id

        :param exercises_id: Идентификатор exercises
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url=f"/api/v1/exercises/{exercises_id}")

    def create_exercises(self, create_exercises_payload: CreateExercisesRequestDict) -> Response:
        """
        Метод для создания exercises

        :param: create_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url="/api/v1/exercises", json=create_exercises_payload)

    def update_exercises(self, update_exercises_payload: UpdateExercisesRequestDict, exercise_id: str) -> Response:
        """
        Метод для изменения exercises

        :param: update_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :param: exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url=f"/api/v1/exercises/{exercise_id}", json=update_exercises_payload)

    def delete_exercises(self, exercise_id: str) -> Response:
        """
        Метод для удаления exercises по exercise_id

        :param exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url=f"/api/v1/exercises/{exercise_id}")
