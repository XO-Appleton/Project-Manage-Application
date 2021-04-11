from enum import Enum, auto

class OpEnum(Enum):

    CREATE = auto()
    MODIFY = auto()
    DELETE = auto()
    VIEW = auto()
    USE_FEATURE = auto()
    EXIT = auto()


if __name__ == "__main__":
    print(OpEnum.CREATE)