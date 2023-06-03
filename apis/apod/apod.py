from httpx import get
from ..base_model import Base
from .parser import Apod
from datetime import date

class Date:
    def __init__(self, d: int, m: int, y: int):
        self.d = d
        self.m = m
        self.y = y

    def __str__(self):
        return f"{self.y}-{self.m}-{self.d}"
    


class APOD(Base):
    base_url = "https://api.nasa.gov/planetary/apod"

    def __init__(self, api_key: str) -> None:
        super.__init__(api_key=api_key)  # type: ignore

    def today(self) -> Apod:
        return Apod(get(self.base_url, params={"api_key": self.api_key}).json())

    def date(self, date: Date) -> Apod:
        return Apod(
            get(
                self.base_url, params={"api_key": self.api_key, "date": str(date)}
            ).json()
        )

    def range_dates(self, sd: Date, ed: Date) -> list[Apod]:
        results = get(
            self.base_url,
            params={"api_key": self.api_key, "start_date": sd, "end_date": ed},
        )
        return [Apod(i) for i in results.json()]

    def rand_images(self, n: int = 1) -> list[Apod]:
        results = get(self.base_url, params={"api_key": self.api_key, "count": n})
        return [Apod(i) for i in results.json()]
