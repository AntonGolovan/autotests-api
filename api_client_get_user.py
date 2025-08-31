from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email, get_fake_last_name, get_fake_first_name


# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_payload = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName=get_fake_last_name(),
    firstName=get_fake_first_name(),
    middleName=get_fake_first_name()
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(request=create_user_payload)
create_user_response_data = create_user_response
print('Create user data:', create_user_response_data)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_payload['email'],
    password=create_user_payload['password']
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response_data['user']['id'])
print('Get user data:', get_user_response)