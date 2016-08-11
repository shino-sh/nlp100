#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import requests
from wiki_article import get_filtered_articles

def main():
  re_info      = re.compile(u'\|(.*?)\s=\s(.*(<ref>[\s\S]*?</ref>)+|.*)')

  for article in get_filtered_articles(u"イギリス"):
    print "article: {}".format(article["title"].encode("utf8"))
    info_dic = {x.group(1): x.group(2) for x in re_info.finditer(article["text"])}

  imageinfo_url = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:{}&prop=imageinfo&&iiprop=url&format=json".format(info_dic[u"国旗画像"])
  response = requests.get(imageinfo_url).json()
  print response['query']['pages']['347935']['imageinfo'][0]['url']

if __name__ == '__main__':
  main()
