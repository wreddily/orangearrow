import unittest
from orangearrow import AmazonRequestBuilder


EXAMPLE_ACCESS_KEY = 'AKIAIOSFODNN7EXAMPLE'
EXAMPLE_SECRET_KEY = '1234567890'
EXAMPLE_ASSOCIATE_TAG = 'mytag-20'


class TestRequestBuilder(unittest.TestCase):
    maxDiff = None

    def test_build_url(self):
        builder = AmazonRequestBuilder(
            EXAMPLE_ACCESS_KEY,
            EXAMPLE_SECRET_KEY,
            EXAMPLE_ASSOCIATE_TAG
        )
        url = builder.build_request_url(
            {
                'AWSAccessKeyId': EXAMPLE_ACCESS_KEY,
                'Service': 'AWSECommerceService',
                'AssociateTag': EXAMPLE_ASSOCIATE_TAG,
                'Operation': 'ItemLookup',
                'ItemId': '0679722769',
                'ResponseGroup': 'Images,ItemAttributes,Offers,Reviews',
                'Version': '2013-08-01'
            },
            override_timestamp='2014-08-18T12:00:00Z',
            override_protocol='http'
        )
        correct_url = ('http://webservices.amazon.com/onca/xml'
                       '?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20'
                       '&ItemId=0679722769&Operation=ItemLookup'
                       '&ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews'
                       '&Service=AWSECommerceService&Timestamp=2014-08-18T12%3A00%3A00Z'
                       '&Version=2013-08-01&Signature=j7bZM0LXZ9eXeZruTqWm2DIvDYVUU3wxPPpp%2BiXxzQc%3D')

        self.assertEqual(
            url,
            correct_url
        )
