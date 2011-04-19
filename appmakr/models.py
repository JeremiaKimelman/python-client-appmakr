import time
import copy
from pyutil import jsonutil as json
from util import json_decode, deep_swap, is_appmakrhandle, APPMAKRHANDLE_RSTR
from pyutil.assertutil import precondition

class Like(object):
    def __init__(self, url, title, lat, lng):
        self.url = url
        self.title = title
        self.lat = lat
        self.lng = lng

    def to_dict(self):
        return {
            'url': self.url,
            'title': self.title,
            'lat': self.lat,
            'lng': self.lng,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return "Like(url=%s, title=%s, lat=%s, lng=%s)" % (self.url, self.title, self.lat, self.lng)

    def __hash__(self):
        return hash((self.url, self.title))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.title == other.title
