from http import HTTPStatus
import allure
import pytest
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_get_exercise_response,
    assert_update_exercise_response,
    assert_exercise_not_found_response,
    assert_get_exercises_response,
)
from tools.assertions.schema import validate_json_schema
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from allure_commons.types import Severity  # Импортируем enum Severity из Allure


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)  # Добавили теги
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.EXERCISES)  # Добавили feature
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.CREATE_ENTITY)  # Добавили story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Create exercise")  # Добавили заголовок
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        request = CreateExerciseRequestSchema(
            course_id=function_course.course_id
        )
        response = exercises_client.create_exercise_api(request=request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request=request, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)  # Добавили тег
    @allure.story(AllureStory.GET_ENTITY)  # Добавили story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Get exercise")  # Добавили заголовок
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        response = exercises_client.get_exercise_api(exercises_id=function_exercise.exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(get_exercise_response=response_data, create_exercise_response=function_exercise.response)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.UPDATE_ENTITY)  # Добавили story
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    @allure.title("Update exercise")  # Добавили заголовок
    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(exercise_id=function_exercise.exercise_id, request=request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request=request, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.DELETE_ENTITY)  # Добавили story
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    @allure.title("Delete exercise")  # Добавили заголовок
    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        delete_exercise_response = exercises_client.delete_exercise_api(exercise_id=function_exercise.exercise_id)
        get_exercise_response = exercises_client.get_exercise_api(exercises_id=function_exercise.exercise_id)
        get_exercise_response_data = InternalErrorResponseSchema.model_validate_json(get_exercise_response.text)

        assert_status_code(delete_exercise_response.status_code, HTTPStatus.OK)
        assert_status_code(get_exercise_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(actual=get_exercise_response_data)
        validate_json_schema(
            instance=get_exercise_response.json(), schema=get_exercise_response_data.model_json_schema()
        )

    @allure.tag(AllureTag.GET_ENTITIES)  # Добавили тег
    @allure.story(AllureStory.GET_ENTITIES)  # Добавили story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Get exercises")  # Добавили заголовок
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture,
            function_course: CourseFixture
    ):
        query = GetExercisesQuerySchema(
            course_id=function_course.course_id
        )

        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(get_exercises_response=response_data, create_exercise_responses=[function_exercise.response])
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())