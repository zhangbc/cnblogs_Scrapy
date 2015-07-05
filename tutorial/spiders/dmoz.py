# -*- coding: utf-8 -*-
import scrapy,re
from tutorial.items import DmozItem
from scrapy.http import Request

class DmozSpider(scrapy.Spider):
    name="cnblogs"

    # 减慢爬虫速度(s)
    # download_delay=1

    # 包含了spider允许爬取的域名(domain)列表(list)
    allowed_domains=['cnblogs.com']
    # 方法一
    # start_urls=[
    #     'http://www.cnblogs.com'
    # ]

    # 方法二
    # scrapy crawl myspider -a category=args
    def __init__(self,category=1,*args,**kwargs):
        super(DmozSpider, self).__init__(*args,**kwargs)
        self.start_urls=['http://www.cnblogs.com/sitehome/p/%s'%category]

    def parse(self, response):
        for sel in response.xpath('//div [@class="post_item"]'):
            itm=DmozItem()
            itm['recommand']=sel.xpath('div/div/span[@class="diggnum"]/text()').extract()
            itm['title']=sel.xpath('div/h3/a/text()').extract()
            itm['link']=sel.xpath('div/h3/a/@href').extract()
            itm['writer']=sel.xpath('div/div/a[@class="lightblue"]/text()').extract()
            str1=sel.xpath('div/div[@class="post_item_foot"]/text()').extract()[1]
            itm['writeDate']=re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2}',str1)
            str2=sel.xpath('div/div/span[@class="article_view"]/a/text()').extract()[0]
            itm['View']=re.findall('\d+',str2)
            str3=sel.xpath('div/div/span[@class="article_comment"]/a/text()').extract()[0].replace('\r\n','').strip()
            itm['comment']=re.findall('\d+',str3)
            yield itm
        self.log('Cnblogs response from %s just arrived!'%response.url)

        # 自动获取下一页
        for index in range(2,11):
            url='http://www.cnblogs.com/sitehome/p/'+str(index)
            yield Request(url,callback=self.parse)