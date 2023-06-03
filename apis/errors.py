class ApiKeyInvalidException(Exception):
    def __init__(self) -> None:
        super().__init__(
            "The ApiKey provided is invalid. If you do not have one apply for one at: https://api.nasa.gov/#signUp"
        )


class IncorrectDataTypeException(Exception):
    def __init__(self, i_d: str, c_d: str) -> None:
        super().__init__(
            f"The datatype provided ({i_d}) cannot be considered as an argument, only the following datatypes are allowed: ({c_d})"
        )


class DateBeyondException(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Date {arg} is in the future")
