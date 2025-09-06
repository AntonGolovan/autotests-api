import pytest
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client

# Импортируем запрос и ответ создания пользователя, модель данных пользователя
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()
