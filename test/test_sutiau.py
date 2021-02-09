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
