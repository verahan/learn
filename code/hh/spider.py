# -*- coding: utf-8 -*-
__author__ = 'hanxue'

import urllib2
import time

url = [''] * 50
link = 1

vera_blog = 'http://chuansong.me/account/one_hanhan'

contents = urllib2.urlopen(vera_blog).read()
#print contents

title = contents.find(r'blog_title')
href = contents.find(r'href=', title)
html = contents.find(r'.html',href)
url[0] = contents[(href + 6):(html +5)]
content = urllib2.urlopen(url[0]).read()
open(url[0][-26:], 'w+').write(content)
print '0 have downloaded', url[0]

while  title != -1 and href != -1 and html != -1 and link < 50:
    #con[href + 6:html + 5]是用来取con字符串href后6位到html倒数5位之间的字符串
    url[link] = contents[href + 6:html + 5]
    #打开读取每一篇文章地址，并存储在content中
    content = urllib2.urlopen(url[link]).read()
    #打开hanhan这个文件夹，如果里面没有url[link][-26:]这个字符串命名的文件，便将content里的内容写入，命名为url[link][-26:]
    open(url[link][-26:],'w+').write(content)
    print link,'have downloaded',url[link]
    title = contents.find(r'blog_title',html)
    href = contents.find(r'href=',title)
    html = contents.find(r'.html',href)
    #自增记数
    link = link +1

