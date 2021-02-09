from test import SuTiau


class A(SuTiau):
    url = 'https://e-dictionary.apc.gov.tw/trv/terms/44_28269.htm'

    def test_詞條名(self):
        self.assertEqual(self.sutiau['sutiau'], 'a', self.sutiau)

    def test_詞條音檔(self):
        self.assertEqual(
            self.sutiau['imtong'],
            'https://e-dictionary.apc.gov.tw/MultiMedia/audio/trv/a_{1}.mp3',
            self.sutiau
        )

    def test_késueh(self):
        self.assertEqual(len(self.sutiau['kesueh']), 4, self.sutiau)

    def test_késueh_huagi(self):
        self.assertEqual(
            self.sutiau['kesueh'][0]['huagi'], '不信任',
            self.sutiau
        )

    def test_késueh_susing(self):
        self.assertEqual(
            self.sutiau['kesueh'][0]['詞類'], '動詞、嘆詞',
            self.sutiau
        )

    def test_késueh_leku(self):
        self.assertEqual(
            len(self.sutiau['kesueh'][1]['leku']), 2,
            self.sutiau,
        )

    def test_leku_tsokgi(self):
        self.assertEqual(
            self.sutiau['kesueh'][1]['leku'][0]['leku'],
            'A! qlahang wa.',
            self.sutiau,
        )

    def test_leku_imtong(self):
        self.assertEqual(
            self.sutiau['kesueh'][1]['leku'][0]['imtong'],
            'https://e-dictionary.apc.gov.tw/MultiMedia/audio/trv/a_{1}_@_2.1.mp3',
            self.sutiau,
        )

    def test_leku_huagi(self):
        self.assertEqual(
            self.sutiau['kesueh'][1]['leku'][0]['huagi'],
            '啊!要小心。',
            self.sutiau,
        )

    def test_leku_tsokgi_boimtong(self):
        self.assertEqual(
            self.sutiau['kesueh'][1]['leku'][1]['leku'],
            'A! Quyu wa!',
            self.sutiau['kesueh'][1]['leku'][1],
        )

    def test_leku_boimtong(self):
        self.assertIsNone(
            self.sutiau['kesueh'][1]['leku'][1]['imtong'],
            self.sutiau['kesueh'][1]['leku'][1],
        )
