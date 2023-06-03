from httpx import get as g
from ..base_model import Base
from .parser import Apod
from datetime import date as d
from .errors import DateBeyondException, IncorrectDataTypeException
from warnings import warn


class Date:
    def __init__(self, d: int|str, m: int|str, y: int|str) -> None:
        self.d = d if len(str(d)) == 2 else f"0{d}"
        self.m = m if len(str(m)) == 2 else f"0{m}"
        self.y = y

    def __str__(self) -> str:
        return f"{self.y}-{self.m}-{self.d}"
    
    @classmethod
    def from_str__or_int(cls, string: str|int):
        string = str(string).replace("-", "").replace("/", '')
        return Date(string[:2], string[2:4], string[4:])


class APOD(Base):
    base_url = "https://api.nasa.gov/planetary/apod"

    def __init__(self, api_key: str, *, image_only: int = 0) -> None:
        super().__init__(api_key=api_key)  # type: ignore
        self.image_only = image_only

    def today(self) -> Apod:
        return self.check_image_only_type(Apod(g(self.base_url, params={"api_key": self.api_key}).json()))

    def date(self, date: Date|str) -> Apod:
        if not isinstance(date, Date) and (isinstance(date, str)  or isinstance(date, int)):
            date = Date.from_str(date)
        else:
            raise IncorrectDataTypeException(type(date),'Date, str, int')
        self.checkdate(date)
        return self.check_image_only_type(
            Apod(
                g(
                   self.base_url, params={"api_key": self.api_key, "date": str(date)}
                ).json()
            )
        )

    def range_dates(self, sd: Date, ed: Date) -> list[Apod]:
        if not isinstance(sd, Date) and (isinstance(sd, str)  or isinstance(sd, int)):
            sd = Date.from_str(sd)
        else:
            raise IncorrectDataTypeException(type(sd),'Date, str, int')
        if not isinstance(ed, Date) and (isinstance(ed, str)  or isinstance(ed, int)):
            ed = Date.from_str(ed)
        else:
            raise IncorrectDataTypeException(type(ed),'Date, str, int')
        self.checkdate(sd)
        self.checkdate(ed)
        results = g(
            self.base_url,
            params={"api_key": self.api_key, "start_date": sd, "end_date": ed},  # type: ignore
        )
        if self.image_only == 0:
            return [Apod(i) for i in results.json()]
        elif self.image_only == 1:
            return [Apod(i).url for i in results.json()]
        elif self.image_only == 2:
            return [Apod(i).hdurl for i in results.json()]
        warn("The Image value type is invalid (it can have one of the following values : 0, 1, 2)")
        return [Apod(i) for i in results.json()]

    def rand_images(self, n: int = 1) -> list[Apod]:
        results = g(self.base_url, params={"api_key": self.api_key, "count": n})
        if self.image_only == 0:
            return [Apod(i) for i in results.json()]
        elif self.image_only == 1:
            return [Apod(i).url for i in results.json()]
        elif self.image_only == 2:
            return [Apod(i).hdurl for i in results.json()]
        warn("The Image value type is invalid (it can have one of the following values : 0, 1, 2)")
        return [Apod(i) for i in results.json()]

    @staticmethod
    def checkdate(date: Date):
        if int(str(date).replace("-", "")) > int(d.today().strftime("%Y%m%d")):
            raise DateBeyondException(str(date))

    def check_image_only_type(self, result):
        if self.image_only == 0:
            return result
        elif self.image_only == 1:
            return result.url
        elif self.image_only == 2:
            return result.hdurl
        else:
            warn("The Image value type is invalid (it can have one of the following values : 0, 1, 2)")
            return result
        