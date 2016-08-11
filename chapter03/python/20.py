#! /usr/bin/env python
# -*- coding: utf-8 -*-

from wiki_article import get_filtered_articles

def main():
  for article in get_filtered_articles(u"イギリス"):
    print article["text"]

if __name__ == '__main__':
  main()
