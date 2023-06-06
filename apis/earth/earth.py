from httpx import get as g
from ..base_models import Base, Date


class EARTH(Base):
    base_url = "https://api.nasa.gov/planetary/earth/imagery"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key=api_key)  # type: ignore

    