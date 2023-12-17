import enum


class UpdateNameStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    NAME_IS_NONE = 4


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


class UpdateCityStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    CITY_IS_NONE = 4


class UpdateZipStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    ZIP_INVALID = 4


class UpdateCountryStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    COUNTRY_IS_NONE = 4


class UpdateImgStatus(enum.Enum):
    SUCCESS = 1
    FAILURE = 2
    USER_NOT_FOUND = 3
    NAME_IS_NONE = 4
