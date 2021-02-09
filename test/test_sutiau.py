from test import SuTiau


class A(SuTiau):
    url = 'https://e-dictionary.apc.gov.tw/trv/terms/44_28269.htm'

    def test_tshi(self):
        self.assertEqual(self.sutiau, {
            'sutiau': 'a'
        }, self.sutiau)
