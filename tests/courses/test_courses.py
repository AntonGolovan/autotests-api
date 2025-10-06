from http import HTTPStatus
import allure
import pytest
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import (
    UpdateCourseRequestSchema,
    UpdateCourseResponseSchema,
    GetCoursesQuerySchema,
    GetCoursesResponseSchema,
    CreateCourseRequestSchema,
    CreateCourseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (
    assert_update_course_response,
    assert_get_courses_response,
    assert_create_course_response,
)
from tools.assertions.schema import validate_json_schema
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from allure_commons.types import Severity  # Импортируем enum Severity из Allure



@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)  # Добавили теги
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.COURSES)  # Добавили feature
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
class TestCourses:
    @allure.tag(AllureTag.CREATE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.CREATE_ENTITY)  # Добавили story
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Create course")  # Добавили заголовок
    def test_create_course(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_file: FileFixture
    ):
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.file_id,
            created_by_user_id=function_user.user_id
        )
        response = courses_client.create_course_api(request=request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_course_response(request=request, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)  # Добавили тег
    @allure.story(AllureStory.GET_ENTITIES)  # Добавили story
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Get courses")  # Добавили заголовок
    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_course: CourseFixture
    ):
        # Формируем параметры запроса, передавая user_id
        query = GetCoursesQuerySchema(user_id=function_user.user_id)
        # Отправляем GET-запрос на получение списка курсов
        response = courses_client.get_courses_api(query)
        # Десериализуем JSON-ответ в Pydantic-модель
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        # Проверяем, что код ответа 200 OK
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что список курсов соответствует ранее созданным курсам
        assert_get_courses_response(response_data, [function_course.response])

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)  # Добавили тег
    @allure.story(AllureStory.UPDATE_ENTITY)  # Добавили story
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    @allure.title("Update course")  # Добавили заголовок
    def test_update_course(
            self,
            courses_client: CoursesClient,
            function_course: CourseFixture
    ):
        # Формируем данные для обновления
        request = UpdateCourseRequestSchema()
        # Отправляем запрос на обновление курса
        response = courses_client.update_course_api(function_course.course_id, request)
        # Преобразуем JSON-ответ в объект схемы
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # Проверяем, что данные в ответе соответствуют запросу
        assert_update_course_response(request, response_data)

        # Валидируем JSON-схему ответа
        validate_json_schema(response.json(), response_data.model_json_schema())