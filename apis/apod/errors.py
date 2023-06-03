class DateBeyondException(Exception):
    def __init__(self, arg: str) -> None:
        super().__init__(f"Date {arg} is in the future")

