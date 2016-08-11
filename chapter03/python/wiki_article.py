#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json

def get_filtered_articles(word):
  with codecs.open("jawiki-country.json", "r", "utf8") as f:
    articles = [json.loads(line) for line in f]

  return filter(lambda x: word in x["title"], articles)
