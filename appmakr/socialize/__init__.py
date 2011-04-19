import urllib

from pyutil import jsonutil as json

from appmakr.util import json_decode, deep_swap, deep_validate_lat_lng, is_appmakrhandle, APPMAKRHANDLE_RSTR
from appmakr.models import Like
from appmakr import Client as ParentClient


class Client(ParentClient):

    def __init__(self, key, secret, api_version='0.1', host='http://www.dev.appmakr.com', port=80):
        self.subclient = True
        ParentClient.__init__(self, key, secret, host=host, port=port)

        self.endpoints.update([
            ('likes', 'socialize/likes/')])

    #Our Like layer

    def add_like(self, like):
        if (like.__class__ != Like):
            raise TypeError("Please send a correct Like Object, you passed in:" + str(like))

        endpoint = self._endpoint('likes')
        self._request(endpoint, "PUT", like.to_dict())
