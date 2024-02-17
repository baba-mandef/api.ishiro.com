from enum import Enum

class BaseEnum(Enum):
    @classmethod
    def keys(cls):
        return [k.name for k in cls]

    @classmethod
    def values(cls):
        return [k.value for k in cls]

    @classmethod
    def items(cls):
        return [(k.value, k.name) for k in cls]
    

class CategoryTypeEnum(BaseEnum):
    income = "income"
    expense = "expense"
    wallet = "wallet"


class ActivityTypeEnum(BaseEnum):
    income = "income"
    expense = "expense"
    