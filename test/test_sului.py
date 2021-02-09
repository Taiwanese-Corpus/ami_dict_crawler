from test import SuTiau


class O(SuTiau):
    url = (
        'https://e-dictionary.apc.gov.tw'
        '/trv/terms/m/115.htm'
    )

    def test_bohunlui(self):
        self.assertEqual(self.sutiau['sutiau'], 'O', self.sutiau)

    def test_késueh_susing(self):
        self.assertEqual(
            self.sutiau['kesueh'][0]['詞類'], '',
            self.sutiau
        )
