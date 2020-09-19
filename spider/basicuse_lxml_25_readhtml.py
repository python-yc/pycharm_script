# -*- coding: utf-8 -*-

from lxml import etree

html = etree.parse("./test.xml")

rst = etree.tostring(html, pretty_print=True)

print(rst)

