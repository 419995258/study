#-*- coding:utf-8 -*-
from scrapy.selector import Selector
with open('superHero.xml','r') as fp:
    body = fp.read()
    #print body
    # 输出所有信息
    xPath = Selector(text=body).xpath('/*').extract()
    print 1
    print xPath
    # 输出第一个节点
    xPath2 = Selector(text=body).xpath('/html/body/superhero/class[1]').extract()
    print 2
    print xPath2
    # 输出最后一个节点
    xPath3 = Selector(text=body).xpath('/html/body/superhero/class[last()]').extract()
    print 3
    print xPath3
    # 输出属性为某个值
    xPath4 = Selector(text=body).xpath('//name[@lang="en"]').extract()
    print 4
    print xPath4
    # 输出倒数第二个属性lang为en的值
    subBody = Selector(text=body).xpath('/html/body/superhero/class[last()]').extract()
    print 5
    xPath5 = Selector(text=subBody[0]).xpath('//name[@lang="en"]').extract()
    print xPath5



    # css选择器
    # 输出所有
    css1 = Selector(text=body).css('class').extract()
    print 'css1'
    print css1
    # 输出class name
    css2 = Selector(text=body).css('class name').extract()
    print 'css2'
    print css2
    # 输出class name的第一个
    css3 = Selector(text=body).css('class name').extract()[0]
    print 'css3'
    print css3
    # 输出css带某个条件
    css4 = Selector(text=body).css('[lang="en"]').extract()
    print 'css4'
    print css4