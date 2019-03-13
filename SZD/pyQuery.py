# coding=utf-8
from pyquery import PyQuery as pq  #pyquery模块




# 执行更新操作
content = '''<p class=MsoNormal><p class=MsoNormal><span lang="EN-US" style='font-family:"Times New Roman","serif"'>
<span lang="EN-US" style='font-family:"Times New Roman","serif"'>
<img height="68" id="图片 1786" src="/alEngin/upload/word/4028803a2c408e3e012c409026b60005/2c2880432c7d6f51012c7e300e9c0021/2c2880432dc13f98012e4c90f56401d6/2c2880432dc13f98012e4c9171c801d7/2c2880432dc13f98012e4c9171e701d8.files/image001.jpg" width="94"/>
</span></span></p>
</p>'''
doc = pq(content)
# span = doc('span')
# doc('p').remove_class('MsoNormal')
# doc('span').css('font-family','').attr('lang','')

# 清除所有的class
doc('[class=MsoNormal]').remove_class('MsoNormal')
# doc下所有的元素清除font和lang
doc('*').css('font-family','').attr('lang','')
print(doc)

