import dataclasses


@dataclasses.dataclass
class ClientUsers:
    id: int
    name: str
    username: str
    password: str
    email: str
    phone: str
    address: str
    city: str
    zip: str
    country: str
    created_at: str
    imgBase64: str


@dataclasses.dataclass
class CleanServiceProviders:
    id: int
    name: str
    username: str
    password: str
    email: str
    phone: str
    address: str
    city: str
    zip: str
    country: str
    created_at: str
    cleanServiceType: str
    imgBase64: str
