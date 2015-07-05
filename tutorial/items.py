# -*- coding: utf-8 -*-
from scrapy import Item,Field


class DmozItem(Item):
    title=Field()
    link=Field()
    writer=Field()
    writeDate=Field()
    View=Field()
    comment=Field()
    recommand=Field()