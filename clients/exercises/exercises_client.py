from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class CreateExercisesRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class UpdateExercisesRequestDict(TypedDict):
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):

    def get_exercises(self) -> Response:
        return self.client.get(url="/api/v1/exercises")

    def get_exercises_by_id(self, exercise_id: str) -> Response:
        return self.client.get(url=f"/api/v1/exercises/{exercise_id}")

    def create_new_exercises(self) -> Response:
        return self.client.post(url="/api/v1/exercises", json="")

    def update_exercises(self, exercise_id: str) -> Response:
        return self.client.patch(url=f"/api/v1/exercises/{exercise_id}", json="")

    def delete_exercises(self, exercise_id: str) -> Response:
        return self.client.get(url=f"/api/v1/exercises/{exercise_id}")

    pass
