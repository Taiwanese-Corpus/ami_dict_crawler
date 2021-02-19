# -*- coding: utf-8 -*-
import scrapy


class EDictionarySpider(scrapy.Spider):
    name = "ami"
    allowed_domains = ["e-dictionary.apc.gov.tw"]
    download_delay = 0
    辭典網址 = 'https://e-dictionary.apc.gov.tw/{}/terms.htm'

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',

        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 0.5,
        'AUTOTHROTTLE_DEBUG': True,

        'DOWNLOAD_DELAY': 5,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CONCURRENT_REQUESTS_PER_IP': 1,

        'RETRY_ENABLED': True,
        'RETRY_TIMES': 5,
        'RETRY_HTTP_CODES': [500, 502, 503, 504, 522, 524, 408, 429, 400],
    }

    def __init__(self, lang='ami', ad=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [self.辭典網址.format(lang)]
        self.lang = lang

    def parse(self, response):
        yield from self.掠詞條(response)
        for a in response.css(
            'div.wordlist_select ul.picker li a'
        ):
            yield response.follow(a.attrib['href'], self.parse)
        for a in response.css(
            'div.wordlist_scrollcontent ul.list_box li a.w_term'
        ):
            yield response.follow(a.attrib['href'], self.parse)

    def 掠詞條(self, response):
        sutiau = response.css(
            'h2.main_title span::text'
        ).get()
        self.logger.debug('掠 {} 詞條'.format(sutiau))

        if sutiau is None:
            self.logger.warning('{} 詞條無資料'.format(sutiau))
            return
        try:
            詞條音檔路徑 = response.css(
                'div.main_entry_word > span.volume audio'
            ).attrib['src']
        except KeyError:
            imtong = None
        else:
            imtong = response.urljoin(詞條音檔路徑)
        kesueh = []
        for pit in response.css(
            'div.main_entry_word div.defin'
        ):
            tuapiau = pit.css('strong')
            sului = tuapiau.css('ul li::text').get()
            try:
                if sului.startswith('詞類：'):
                    sului = sului[3:]
            except AttributeError:
                sului = ''
            leku = []
            for li in pit.css(
                'div.row div.col-md-12 ul.exam_lst li'
            ):
                tsokgi_leku = ''.join(
                    li.css('p.stc button *::text, p.stc::text').getall()
                ).strip()
                leku_imtong = None
                leku_imtong_nuaui = li.css('p.stc span.volume audio')
                if leku_imtong_nuaui:
                    leku_imtong = leku_imtong_nuaui.attrib['src']
                    if leku_imtong:
                        leku_imtong = response.urljoin(leku_imtong)
                leku.append({
                    'leku': tsokgi_leku,
                    'imtong': leku_imtong,
                    'huagi': li.css('p.trans::text').get(),
                })
            kesueh.append({
                'mia': tuapiau.css('span.num::text').get(),
                'huagi': tuapiau.css('span.num ~ span::text').get(),
                '詞類': sului,
                'leku': leku,
            })
        yield {
            'sutiau': sutiau,
            'imtong': imtong,
            'kesueh': kesueh,
        }
