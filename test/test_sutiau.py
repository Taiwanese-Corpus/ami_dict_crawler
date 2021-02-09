from unittest.case import TestCase

from crawler import EDictionarySpider

from scrapy.http import TextResponse, Request
from urllib.request import urlopen


class SuTiau(TestCase):
    def test_tshi(self):
        kiatko = EDictionarySpider().parse(liansuann(
            'https://e-dictionary.apc.gov.tw/trv/terms/44_28269.htm')
            )
        tsuliau = next(kiatko)
        self.assertEqual(tsuliau, {
            'sutiau': 'a'
        })


def liansuann(url):
    要求 = Request(url)
    with urlopen(url) as f:
        return TextResponse(
            url,
            body=f.read(),
            encoding='utf-8',
            request=要求,
        )
