# -*- coding: utf-8 -*-
from urllib.parse import urljoin
import scrapy
from scrapy.selector import Selector
from sys import stderr

class Spider(scrapy.Spider):
    name = "ami"
    allowed_domains = ["e-dictionary.apc.gov.tw"]
    download_delay = 0
    辭典網址 = 'https://e-dictionary.apc.gov.tw/{}/terms.htm'

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
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
            yield {
                'href': a.attrib['href'],
                'text': a.css('a::text').get(),
            }
        for a in response.css(
            'div.wordlist_scrollcontent ul.list_box li a.w_term'
        ):
            yield {
                'href': a.attrib['href'],
                'text': a.css('a::text').get(),
            }

    def 掠詞條(self, response):
        self.logger.debug('掠 {} 詞條'.format(response.meta['詞條名']))
        這詞條 = Selector(response)
        data = {'examples': []}
        data['name'] = 這詞條.xpath(
            '//div[@id="oGHC_Term"]/span/text()'
        ).extract_first()
        if data['name'] is None:
            self.logger.warning('{} 詞條無資料'.format(response.meta['詞條名']))
            return
        詞條音檔路徑 = 這詞條.xpath('//div[@id="oGHC_Term"]/a/@rel').extract_first()
        if 詞條音檔路徑:
            data['pronounce'] = urljoin(response.url, 詞條音檔路徑)
        else:
            data['pronounce'] = None
        data['frequency'] = ''.join(
            這詞條.xpath('//div[@id="oGHC_Freq"]/descendant::text()').extract()
        )

        try:
            data['source'] = (
                這詞條
                .xpath('//div[@id="oGHC_Source"]/a[@class="ws_term"]/text()').
                extract_first()
            )
        except:
            data['source'] = None
        descriptions = [''.join(x.xpath('descendant::text()').extract())
                        for x in 這詞條.xpath('//div[@class="block"]/div[1]')]
        sentences = [''.join(x.xpath('descendant::text()').extract()).strip()
                     for x in 這詞條.xpath('//div[@class="block"]/div[2]/table/tr[1]/td')]
        pronounces = [urljoin(response.url, x.extract()) for x in 這詞條.xpath(
            '//div[@class="block"]/div[2]/table/tr[1]/td/a[@class="play"]/@rel')]
        zh_Hants = [''.join(x.xpath('text()').extract()) for x in 這詞條.xpath(
            '//div[@class="block"]/div[2]/table/tr[2]/td')]
        for i in range(len(descriptions)):
            data['examples'].append({
                'description': descriptions[i],
                'sentence': sentences[i] if len(sentences) > i else None,
                'pronounce': pronounces[i] if len(pronounces) > i else None,
                'zh_Hant': zh_Hants[i] if len(zh_Hants) > i else None
            })
        return data
