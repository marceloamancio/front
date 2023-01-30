from enum import auto
from strenum import StrEnum

class Operation(StrEnum):
    CREATE_TOPIC = auto()
    MAKE_SUBSCRIPTION = auto()
    SEND_MESSAGE = auto()
    READ_MESSAGE = auto()
    HELLO = auto()

default_message = "default hello!"