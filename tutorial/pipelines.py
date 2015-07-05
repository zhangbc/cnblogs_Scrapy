# -*- coding: utf-8 -*-
import json
from scrapy.exceptions import DropItem

# 按条件过滤结果 推荐指数>0
class CommentPipeline(object):
    def process_item(self,item,spider):
        if item['recommand'][0]>='0':
            return item
        else:
            raise DropItem('recommand<=0%s'%item)

class TutorialPipeline(object):
    def __init__(self):
        self.file=open('items.json','w')
    def process_item(self, item, spider):
        line=json.dumps(dict(item))+'\n'
        self.file.write(line)
        return item
