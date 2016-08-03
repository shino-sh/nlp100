#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  with codecs.open("col1.txt", "r", "utf8") as f1:
    col1 = f1.read().strip().split("\n")
  with codecs.open("col2.txt", "r", "utf8") as f2:
    col2 = f2.read().strip().split("\n")
  with codecs.open("col12.txt", "w", "utf8") as f:
    f.write("\n".join([x+"\t"+y for (x, y) in zip(col1, col2)]))

if __name__ == '__main__':
  main()
