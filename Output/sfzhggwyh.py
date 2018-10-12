# -*- coding: utf-8 -*-
import scrapy

from web.items import WebItem

class SfzhggwyhSpider(scrapy.Spider):
    name = 'sfzhggwyh'
    allowed_domains = ['fgw.hunan.gov.cn']
    start_urls = ['http://fgw.hunan.gov.cn/xxgk_70899/tzgg/']
    for i in range(1,40):
        a = "http://fgw.hunan.gov.cn/xxgk_70899/tzgg//index_"+str(i) +".html"
        start_urls.append(a)
    pass

    def parse(self, response):
        if response.status == 200:

            source = u'省发展和改革委员会'
            # response.xpath('//title/text()').extract()[0]
    
            for sel in response.xpath('//table/tbody/tr'):
                # print source
                # print sel.xpath('./td/a/text()').extract()[0]
                # print sel.xpath('./td/a/@href').extract()[0]
                # print sel.xpath('./td[3]/text()').extract()[0]
                item = WebItem()
                item['source'] = source
                item['title'] = sel.xpath('./td/a/text()').extract()[0]
                item['link'] = self.start_urls[0]+sel.xpath('./td/a/@href').extract()[0]
                item['posttime'] = sel.xpath('./td[3]/text()').extract()[0]
                print item['title']
                yield item
    pass
