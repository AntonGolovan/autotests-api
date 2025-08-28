from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):

    def create_new_user_api(self, create_user_data: CreateUserRequestDict) -> Response:
        """
        Метод для создания нового пользователя
        :param create_user_data: Словарь с данными по пользователю: email, password, lastName, firstName, middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.client.post(url="/api/v1/users", json=create_user_data)