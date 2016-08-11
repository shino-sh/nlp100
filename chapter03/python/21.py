#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from wiki_article import get_filtered_articles

def main():
  re_category = re.compile(u'\[\[Category:(.*?)\]\]')
  
  for article in get_filtered_articles(u"イギリス"):
    print "article: {}".format(article["title"].encode("utf8"))
    categories = filter(lambda x: re_category.match(x), article["text"].split("\n"))
    for category in categories:
      print category

if __name__ == '__main__':
  main()
