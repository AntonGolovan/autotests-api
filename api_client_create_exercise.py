from clients.authentication.authentication_client import get_authentication_client
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExercisesRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import *

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName=get_fake_last_name(),
    firstName=get_fake_first_name(),
    middleName=get_fake_first_name()
)

create_user_response = public_users_client.create_user(request=create_user_request)
print('Create user data:', create_user_response)

authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)

authentication_client = get_authentication_client()

files_client = get_files_client(user=authentication_user)
courses_client = get_courses_client(user=authentication_user)


create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)

create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

exercises_client = get_exercises_client(user=authentication_user)

create_exercise_request = CreateExercisesRequestDict(
    title="Test Exercise 1",
    courseId=create_course_response["course"]["id"],
    maxScore=20,
    minScore=5,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="2 weeks",
)

create_exercise_response = exercises_client.create_exercise(request=create_exercise_request)
print('Create exercise data:', create_exercise_response)