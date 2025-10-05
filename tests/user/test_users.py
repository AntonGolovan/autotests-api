import pytest
import allure
from http import HTTPStatus
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from allure_commons.types import Severity  # Импортируем enum Severity из Allure


@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)  # Используем enum
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.USERS)  # Добавили feature
class TestUsers:
    @pytest.mark.parametrize(
        "email", ["mail.ru", "gmail.com", "example.com"],
        ids=lambda domain: f'Test create user wint email domain: {domain}'
    )
    @allure.tag(AllureTag.CREATE_ENTITY)  # Используем enum
    @allure.story(AllureStory.CREATE_ENTITY)  # Добавили story
    @allure.severity(Severity.BLOCKER)  # Добавили severity
    @allure.title("Create user")
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain=email))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)  # Используем enum
    @allure.story(AllureStory.GET_ENTITY)  # Добавили story
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    @allure.title("Get user me")
    def test_get_user_me(self, function_user: UserFixture,private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validate_json_schema(response.json(), response_data.model_json_schema())