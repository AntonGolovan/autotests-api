import httpx
from pprint import pprint

login_payload = {
    "email": "golovan@example.com",
    "password": "golovan123456"
}

base_url = "http://localhost:8000"
login_url = "/api/v1/authentication/login"
get_user_me_url = "/api/v1/users/me"

login_response = httpx.post(url=base_url + login_url, json=login_payload)
login_response_data = login_response.json()
access_token = login_response_data["token"]["accessToken"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

get_user_me_response = httpx.get(url=base_url + get_user_me_url, headers=headers)
get_user_me_response_data = get_user_me_response.json()

pprint(f"Status code: {get_user_me_response.status_code}", indent=4)
pprint(f"User info: {get_user_me_response_data}", indent=4)



