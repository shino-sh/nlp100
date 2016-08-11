#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
from wiki_article import get_filtered_articles

def main():
  re_mediafile = re.compile(u'(File|ファイル):([^\.]+\.\w+)')

  for article in get_filtered_articles(u"イギリス"):
    print "article: {}".format(article["title"].encode("utf8"))
    mediafiles = [x.group(2) for x in re_mediafile.finditer(article["text"])]
    for mediafile in mediafiles:
      print mediafile.encode("utf8")

if __name__ == '__main__':
  main()
