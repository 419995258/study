import re

s = "I am python modules test for re modules"
print re.search('am',s)
print re.search('am',s).group()
print re.match('am',s)
print re.match('I am',s)
print re.match('I am',s).group()
print re.findall('modules',s)
re.finditer('modules',s)
for sre in re.finditer('modules',s):
    print (sre.group())