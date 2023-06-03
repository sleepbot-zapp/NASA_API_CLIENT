from httpx import get as g
from ..base_model import Base
from .parser import Apod
from datetime import date as d
from .errors import DateBeyondException


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
        return Apod(g(self.base_url, params={"api_key": self.api_key}).json())

    def date(self, date: Date) -> Apod:
        self.checkdate(date)
        return Apod(
            g(
                self.base_url, params={"api_key": self.api_key, "date": str(date)}
            ).json()
        )

    def range_dates(self, sd: Date, ed: Date) -> list[Apod]:
        self.checkdate(sd)
        self.checkdate(ed)
        results = g(
            self.base_url,
            params={"api_key": self.api_key, "start_date": sd, "end_date": ed},  # type: ignore
        )
        return [Apod(i) for i in results.json()]

    def rand_images(self, n: int = 1) -> list[Apod]:
        results = g(self.base_url, params={"api_key": self.api_key, "count": n})
        return [Apod(i) for i in results.json()]

    @staticmethod
    def checkdate(date: Date):
        if int(str(date).replace("-", "")) > int(d.today().strftime("%Y%m%d")):
            raise DateBeyondException(str(date))
