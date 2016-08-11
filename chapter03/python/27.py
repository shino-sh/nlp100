#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from wiki_article import get_filtered_articles

def main():
  re_info      = re.compile(u'\|(.*?)\s=\s(.*(<ref>[\s\S]*?</ref>)+|.*)')
  re_emphasis  = re.compile(u'\'{2,5}')
  re_interlink = re.compile(u'\[{2}(.*?)\]{2}')

  for article in get_filtered_articles(u"イギリス"):
    print "article: {}".format(article["title"].encode("utf8"))
    _article = re.sub(re_emphasis, "", article["text"])
    _article = re.sub(re_interlink, r'\g<1>', _article)
    infos = [x.group(1, 2) for x in re_info.finditer(_article)]
    for k, v in dict(infos).items():
      print k, v

if __name__ == '__main__':
  main()
