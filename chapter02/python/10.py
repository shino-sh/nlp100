#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    lines = f.readlines()
  print len(lines)

if __name__ == '__main__':
  main()
