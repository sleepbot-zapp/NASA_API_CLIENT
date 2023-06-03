class ApiKeyInvalidException(Exception):
    def __init__(self) -> None:
        super().__init__(
            "The ApiKey provided is invalid. If you do not have one apply for one at: https://api.nasa.gov/#signUp"
        )
