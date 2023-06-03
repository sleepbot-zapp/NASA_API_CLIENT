class Base:
    """
    A base class for all API models
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
