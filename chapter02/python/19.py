#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import collections

def main():
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    col1 = [line.split("\t")[0] for line in f.readlines()]
  count_dict = collections.Counter(col1)
  for k, v in sorted(count_dict.items(), key=lambda x:x[1], reverse=True):
    print k

if __name__ == '__main__':
  main()
