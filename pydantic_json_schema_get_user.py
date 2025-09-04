from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import (
    CreateUserRequestSchema,
    GetUserResponseSchema,
)
from tools.assertions.schema import validate_json_schema
from tools.fakers import *

public_users_client = get_public_users_client()

create_user_request =  CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name=get_fake_last_name(),
    first_name=get_fake_first_name(),
    middle_name=get_fake_first_name()
)

create_user_response = public_users_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password = create_user_request.password
)

private_users_client = get_private_users_client(user=authentication_user)
get_user_response = private_users_client.get_user_api(user_id=create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)