#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from wiki_article import get_filtered_articles

def main():
  re_info = re.compile(u'\|(.*?)\s=\s(.*(<ref>[\s\S]*?</ref>)+|.*)')

  for article in get_filtered_articles(u"イギリス"):
    print "article: {}".format(article["title"].encode("utf8"))
    info_dic = {x.group(1): x.group(2) for x in re_info.finditer(article["text"])}
    for k, v in info_dic.items():
      print k, v

if __name__ == '__main__':
  main()
