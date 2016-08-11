#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from wiki_article import get_filtered_articles

def main():
  re_info      = re.compile(u'\|(.*?)\s=\s(.*(<ref>[\s\S]*?</ref>)+|.*)')
  re_emphasis  = re.compile(u'\'{2,5}')
  re_interlink = re.compile(u'\[{2}(.*?)\]{2}')
  re_markup1   = re.compile(u'<(.*?)>')
  re_markup2   = re.compile(u'\[(.*?)\]')
  re_language  = re.compile(u'{{.*?\|.*?\|(.*?)}}')

  for article in get_filtered_articles(u"イギリス"):
    print "article: {}".format(article["title"].encode("utf8"))
    _article = re.sub(re_emphasis,  "",    article["text"])
    _article = re.sub(re_interlink, r'\1', _article)
    _article = re.sub(re_markup1,   "",    _article)
    _article = re.sub(re_markup2,   "",    _article)
    _article = re.sub(re_language,  r'\1', _article)
    info_dic = {x.group(1): x.group(2) for x in re_info.finditer(_article)}
    for k, v in info_dic.items():
      print k, v

if __name__ == '__main__':
  main()
