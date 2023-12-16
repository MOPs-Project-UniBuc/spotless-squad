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


class UpdatePhoneStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    NUMBER_TOO_SHORT = 4
    NUMBER_TOO_LONG = 5


class UpdateAddressStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    ADDRESS_IS_NONE = 4
