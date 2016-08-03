#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  print "print head N lines.",
  print "input N :",
  n = int(raw_input())
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    for line in f.readlines()[:n]:
      print line.strip()

if __name__ == '__main__':
  main()
