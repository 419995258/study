# coding=utf-8
from pyquery import PyQuery as pq  #pyquery模块




# 执行更新操作
content = '''
<p class=MsoNormal  style='text-align:left;vertical-align:middle'>当<img width=33 height=17
src="/alEngin/upload/word_html/subject.0013/ff8080812f67a257012f6b83b82e009d//531997a7335d4e640133620c7bdd01de/Doc2.files/image001.gif">时，求多项式<img width=188 height=24 src="/alEngin/upload/word_html/subject.0013/ff8080812f67a257012f6b83b82e009d//531997a7335d4e640133620c7bdd01de/Doc2.files/image002.gif">的值.</p>
'''
doc = pq(content)
# span = doc('span')
# doc('p').remove_class('MsoNormal')
# doc('span').css('font-family','').attr('lang','')

# 清除所有的class
# doc('[class=MsoNormal]').remove_class('MsoNormal')
# # doc下所有的元素清除font和lang
# doc('*').css('font-family','').attr('lang','')
print(doc)

