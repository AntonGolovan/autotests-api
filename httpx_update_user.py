import httpx
from pprint import pprint
from tools.fakers import fake
from faker import Faker

fake = Faker()

base_url = "http://localhost:8000"
login_url = "/api/v1/authentication/login"
get_user_url = "/api/v1/users/me"
create_user_url = "/api/v1/users"
update_user_by_id_url = "/api/v1/users/"

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(url=base_url + create_user_url, json=create_user_payload)
assert create_user_response.status_code == 200, f"Wrong! Expected status code 200, Got {create_user_response.status_code}"
user_email = create_user_response.json()["user"]["email"]
user_password = create_user_payload.get("password")

login_payload = {
    "email": user_email,
    "password": user_password
}

login_response = httpx.post(url=base_url + login_url, json=login_payload)
assert login_response.status_code == 200, f"Wrong! Expected status code 200, Got {login_response.status_code}"
access_token = login_response.json()["token"]["accessToken"]

get_user_headers = {
    "Authorization": f"Bearer {access_token}"
}

get_user_response = httpx.get(url=base_url + get_user_url, headers=get_user_headers)
assert get_user_response.status_code == 200, f"Wrong! Expected status code 200, Got {get_user_response.status_code}"
user_id = get_user_response.json()["user"]["id"]

update_user_payload = {
    "email": fake.email(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.first_name()
}

update_user_response = httpx.patch(url=base_url + update_user_by_id_url + user_id, headers=get_user_headers, json=update_user_payload)
assert get_user_response.status_code == 200, f"Wrong! Expected status code 200, Got {get_user_response.status_code}"
pprint(f"Update user data: {update_user_response.json()}",indent=4)
