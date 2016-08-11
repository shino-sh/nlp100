#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from wiki_article import get_filtered_articles

def main():
  re_section = re.compile(u'(={2,})(.*?)(={2,})')

  for article in get_filtered_articles(u"イギリス"):
    print "article: {}".format(article["title"].encode("utf8"))
    sections = [x.group(2, 1) for x in re_section.finditer(article["text"])]
    for section in sections:
      print "{} (level: {})".format(section[0].encode("utf8"), len(section[1])-1)

if __name__ == '__main__':
  main()
