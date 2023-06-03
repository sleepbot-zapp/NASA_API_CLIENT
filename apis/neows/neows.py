from httpx import get as g
from ..base_model import Base, Date
from datetime import date as d
from ..errors import IncorrectDataTypeException, DateBeyondException


class NEOWS(Base):
    base_url = "hhttps://api.nasa.gov/neo/rest/v1/feed"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key=api_key)  # type: ignore

    def search(self, sd: Date | int | str, ed: Date | int | str) -> None:
        if not isinstance(sd, Date) and (isinstance(sd, str) or isinstance(sd, int)):
            sd = Date.from_str(sd)
        else:
            raise IncorrectDataTypeException(type(sd), "Date, str, int")
        if not isinstance(ed, Date) and (isinstance(ed, str) or isinstance(ed, int)):
            ed = Date.from_str(ed)
        else:
            raise IncorrectDataTypeException(type(ed), "Date, str, int")
        self.checkdate(sd)
        self.checkdate(ed)
        return g(
            self.base_url,
            params={"api_key": self.api_key, "start_date": sd, "end_date": ed},  # type: ignore
        )

    @staticmethod
    def checkdate(date: Date):
        if int(str(date).replace("-", "")) > int(d.today().strftime("%Y%m%d")):
            raise DateBeyondException(str(date))
