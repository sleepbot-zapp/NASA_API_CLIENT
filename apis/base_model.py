class Base:
    """
    A base class for all API models
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key


class Date:
    def __init__(self, d: int | str, m: int | str, y: int | str) -> None:
        self.d = d if len(str(d)) == 2 else f"0{d}"
        self.m = m if len(str(m)) == 2 else f"0{m}"
        self.y = y

    def __str__(self) -> str:
        return f"{self.y}-{self.m}-{self.d}"

    @classmethod
    def from_str__or_int(cls, string: str | int):
        string = str(string).replace("-", "").replace("/", "")
        return Date(string[:2], string[2:4], string[4:])