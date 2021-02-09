from test import SuTiau


class ImTong(SuTiau):
    url = (
        'https://e-dictionary.apc.gov.tw'
        '/trv/terms/m/48.htm'
    )

    def test_sutiau(self):
        self.assertEqual(self.sutiau['sutiau'], 'eadas', self.sutiau)

    def test_sutiau_boimtong(self):
        self.assertIsNone(
            self.sutiau['imtong'],
            self.sutiau
        )
