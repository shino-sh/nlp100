#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    rows = [line.split("\t") for line in f.readlines()]
    rows.sort(key=lambda x:x[2])
    lines = ["\t".join(row) for row in rows]
  print "".join(lines).strip()

if __name__ == '__main__':
  main()
