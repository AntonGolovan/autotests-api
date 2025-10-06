import allure
from clients.api_client import APIClient
from httpx import Response
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExercisesResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseResponseSchema,
)
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка exercises

        :param: Словарь с courseId.
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url="/api/v1/exercises", params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercises_id}")
    def get_exercise_api(self, exercises_id: str) -> Response:
        """
        Метод получения задания по exercises_id

        :param exercises_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url=f"/api/v1/exercises/{exercises_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания задания

        :param: create_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url="/api/v1/exercises", json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercises_id}")
    def update_exercise_api(self, request: UpdateExerciseRequestSchema, exercise_id: str) -> Response:
        """
        Метод для изменения задания  по exercise_id

        :param: update_exercises_payload: Словарь с title, courseId, maxScore, minScore, orderIndex,
        description, estimatedTime.
        :param: exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url=f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercises_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания по exercise_id

        :param exercise_id: Идентификатор exercise
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url=f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercises_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercises_id=exercises_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, request: UpdateExerciseRequestSchema, exercises_id: str) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(request=request, exercise_id=exercises_id)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param
    :return Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user=user))