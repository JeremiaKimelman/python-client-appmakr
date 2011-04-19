import unittest
from decimal import Decimal as D

from pyutil import jsonutil as json
import mock

from appmakr import Client
from appmakr.util import APIError, DecodeError, is_valid_lat, is_valid_lng, is_valid_ip, to_unicode

MY_OAUTH_KEY = 'MY_OAUTH_KEY'
MY_OAUTH_SECRET = 'MY_SECRET_KEY'
TESTING_LAYER = 'TESTING_LAYER'

API_VERSION = '1.0'
API_HOST = 'http://www.dev.appmakr.com'
API_PORT = 80

class ReallyEqualMixin:
    def failUnlessReallyEqual(self, a, b, msg='', *args, **kwargs):
        self.failUnlessEqual(a, b, msg, *args, **kwargs)
        self.failUnlessEqual(type(a), type(b), msg="a :: %r, b :: %r, %r" % (a, b, msg), *args, **kwargs)

class ToUnicodeTest(unittest.TestCase, ReallyEqualMixin):
    def test_to_unicode(self):
        self.failUnlessReallyEqual(to_unicode('x'), u'x')
        self.failUnlessReallyEqual(to_unicode(u'x'), u'x')
        self.failUnlessReallyEqual(to_unicode('\xe2\x9d\xa4'), u'\u2764')

class DecodeErrorTest(unittest.TestCase):
    def test_repr(self):
        body = 'this is not json'
        try:
            json.loads('this is not json')
        except ValueError, le:
            e = DecodeError(body, le)
        else:
            self.fail("We were supposed to get an exception from json.loads().")

        self.failUnless("Could not decode JSON" in e.msg, repr(e.msg))
        self.failUnless('JSONDecodeError' in repr(e), repr(e))

    def add_like(self, like):
        if (like.__class__ != Like):
            raise TypeError("Please send a correct Like Object, you passed in:" + str(like))

        endpoint = self._endpoint('likes')
        if endpoint != self.endpoints.update():
            raise TypeError("Please send the correct endpoint, you passed in:" + str(endpoint))

        self._request(endpoint, "POST", like.to_dict())

class ClientTest(unittest.TestCase):
    def setUp(self):
        self.client = Client(MY_OAUTH_KEY, MY_OAUTH_SECRET, host=API_HOST, port=API_PORT)

    def test_is_valid_ip(self):
        self.failUnless(is_valid_ip('192.0.32.10'))
        self.failIf(is_valid_ip('i am not an ip address at all'))

    def test_wrong_endpoint(self):
        self.assertRaises(Exception, self.client._endpoint, 'wrongwrong')

    def test_get_likes_useful_validation_error_message(self):
        c = Client('whatever', 'whatever')
        try:
            c.socialize.add_like('wrong thing')
        except TypeError, e:
            self.failUnless(str(e).startswith('Please send a correct Like Object'), str(e))
        else:
            self.fail('Should have raised exception.')

    def test_APIError(self):
        e = APIError(500, 'whee', {'status': "500"})
        self.failUnlessEqual(e.code, 500)
        self.failUnlessEqual(e.msg, 'whee')
        repr(e)
        str(e)

EXAMPLE_BODY = "{}"
