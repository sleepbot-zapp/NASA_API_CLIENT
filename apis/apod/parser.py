from ..errors import ApiKeyInvalidException

class Apod:
    def __init__(self, data) -> None:
        self.data = data
        try:
            self.data['error']['message']
        except KeyError:
            pass
        else:
            raise ApiKeyInvalidException

    @property
    def copyright(self):
        return self.data.get("copyright") or None

    @property
    def date(self):
        return self.data.get("date") or None

    @property
    def title(self):
        return self.data.get("title") or None

    @property
    def explanation(self):
        return self.data.get("explanation") or None

    @property
    def media_type(self):
        return self.data.get("media_type") or None

    @property
    def hdurl(self):
        return self.data.get("hdurl") or None

    @property
    def url(self):
        return self.data.get("url") or None
