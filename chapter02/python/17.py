#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    col1 = [line.split("\t")[0] for line in f.readlines()]
  print "\n".join(set(col1))

if __name__ == '__main__':
  main()
