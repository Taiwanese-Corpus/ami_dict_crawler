from unittest.case import TestCase

from crawler import EDictionarySpider

from scrapy.http import TextResponse, Request
from urllib.request import urlopen


class SuTiau(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        kiatko = EDictionarySpider().parse(
            liansuann(cls.url)
        )
        cls.sutiau = next(kiatko)


def liansuann(url):
    要求 = Request(url)
    with urlopen(url) as f:
        return TextResponse(
            url,
            body=f.read(),
            encoding='utf-8',
            request=要求,
        )
