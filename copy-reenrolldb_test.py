import pprint
import random
import data
import uuid

from database import engine, SessionLocal, Base
from pydantic import validate_arguments, ValidationError
from models import User, Course, Service, Submission, Environment
from crud import *

Base.metadata.create_all(bind=engine)

session = SessionLocal()

# # User
# u = {
#     "id": "fd2vyoq7",
#     "username": "",
#     "sso_sub": "0000000-0000-0000-0000-00000000000",
#     "sso_preferred_username": "user0",
#     "sso_email": "user0@example.com",
#     "sso_given_name": "User",
#     "sso_family_name": "Name",
#     "sso_name": "User Name",
#     "preferred_username": "user0",
#     "preferred_email": "user1@example.com",
#     "document": None
# }
#
# try:
#     result = crud.create_user(session, u)
#     # print("result:", result)
# except crud.ModelAlreadyExistsError:
#     print("User model already exists in database.")

# Update environment record by document
# result = crud.update_environment_by_document(session, env_document=data.env_dict_no_vscode)

# result = crud.update_environment(db=session,
#                                  env=data.env)

# for i in range(100):
#     user_id = str(uuid.uuid4())
#     preferred_username = "user-" + user_id.split("-")[0]
#
#     # Mock user data
#     user_data = {
#         "id": user_id,
#         "username": preferred_username,
#         "sso_sub": "0000000-0000-0000-0000-00000000000",
#         "sso_preferred_username": "user0",
#         "sso_email": "user0@example.com",
#         "sso_given_name": "User",
#         "sso_family_name": "Name",
#         "sso_name": "User Name",
#         "preferred_username": preferred_username,
#         "preferred_email": "user1@example.com",
#     }
#
#     # Create user
#     result = create_user(db=session, user=user_data)
#     print(result.username)

# for i in range(100):
#     # Mock course data
#     course_id = random.randint(1, 1000)
#
#     cs_135 = {
#         "id": course_id,
#         "subject": "CS",
#         "catalog_number": "135",
#         "semester": "F23",
#         "hidden": False
#     }
#
#     course = create_course(db=session, course=cs_135)
#     print("course_id:", course_id)

# res = get_course(db=session, semester="F23", subject="CS", catalog_number="135")
#
# for key in res.__dir__():
#     value = getattr(res, key)
#     if not f"{key}".startswith('_'):
#         print(f"{key}: {value}")

# get_submission(db=session, id=)

# User
u = {
    "id": "fd2vyoq6",
    "username": "",
    "sso_sub": "0000000-0000-0000-0000-00000000000",
    "sso_preferred_username": "user0",
    "sso_email": "user0@example.com",
    "sso_given_name": "User",
    "sso_family_name": "Name",
    "sso_name": "User Name",
    "preferred_username": "user0",
    "preferred_email": "user1@example.com",
}

# Course
c = {
    "subject": "CS",
    "catalog_number": "202",
    "semester": "F23",
    "hidden": False,
}

# Service
s = {
    "name": "linux_remote_container_22",
    "display_name": "Linux Container Remote Desktop",
}

#Submission
# user = get_user(session, u["id"])
# course = get_course(session, c["subject"], c["catalog_number"], c["semester"])
# service = get_service(session, s["name"])
#
# sub = {
#     "user": user,
#     "courses": [course],
#     "services": [service],
# }
#
# print(sub)

# for i in range(150):
#     service_id = random.randint(1, 2000)
#     service_name = f"linux_remote_container_{service_id}"
#
#     service_data = {
#         "id": service_id,
#         "name": service_name,
#         "display_name": "Linux Container Remote Desktop",
#     }
#
#     res = create_service(db=session, service=service_data)
#     print(res.name)


for i in range(100):
    user_id = random.randint(1, 100)
    environment_id = data.env_dict["id"] + '_' + str(random.randint(1, 1000))

    user = get_users(db=session, skip=0, limit=100)

    env = {
        "id": environment_id,
        "user": user[user_id],
        "document": data.env_dict
    }

    res = create_environment(db=session, environment=env)
    print(res.id)

session.close()

# res = get_users(db=session)
# print(len(res))
