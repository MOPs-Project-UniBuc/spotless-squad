import enum


class UpdateStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3


class UpdatePasswordStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    PASSWORD_TOO_SHORT = 4
