import enum


class BookingStatus(enum.Enum):
    SUCCESS = 1
    PROVIDER_NOT_FOUND = 2
    PROVIDER_NOT_AVAILABLE = 3
