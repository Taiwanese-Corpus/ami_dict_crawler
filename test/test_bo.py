from test import SuTiau


class OoPehPhah(SuTiau):
    url = (
        'https://e-dictionary.apc.gov.tw'
        '/trv/terms/44_282691212.htm'
    )

    def test_bô詞條_所致傳連結(self):
        self.assertNotIn('sutiau', self.sutiau, self.sutiau)
