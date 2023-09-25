from typing import Union, Optional

from pydantic import BaseModel


class EnvironmentBase(BaseModel):
    id: str
    document: dict | str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    id: str
    username: str
    sso_sub: str

    preferred_email: str
    preferred_username: str

    sso_email: str
    sso_preferred_username: str
    sso_given_name: str
    sso_family_name: str
    sso_name: str

    document: Optional[dict]

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    id: Optional[int]
    subject: str
    catalog_number: str
    semester: str

    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    id: Optional[int]
    name: str
    display_name: str

    class Config:
        orm_mode = True


class SubmissionBase(BaseModel):
    class Config:
        orm_mode = True


class Course(CourseBase):
    pass


class CourseCreate(Course):
    pass


class Service(ServiceBase):
    pass


class ServiceCreate(Service):
    pass


class Submission(SubmissionBase):
    pass


class SubmissionCreate(Submission):
    user: UserBase
    services: list[Service]
    courses: list[Course]


class User(UserBase):
    submissions: Optional[list[Submission]]
    environments: Optional[list[EnvironmentBase]]


class Environment(EnvironmentBase):
    user: UserBase
    submission: Optional[SubmissionBase]
    document: Optional[dict]


class EnvironmentCreate(EnvironmentBase):
    user: UserBase
    submission: Optional[SubmissionBase]
    document: Optional[dict]


class UserCreate(UserBase):
    pass


class UserSearch(BaseModel):
    username: str


class UserSearchResult(BaseModel):
    status: bool
