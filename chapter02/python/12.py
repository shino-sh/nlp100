#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    col12 = [tuple(line.split("\t")[:2]) for line in f.readlines()]
  for i in range(2):
    with codecs.open("col{}.txt".format(i+1), "w", "utf8") as f_out:
      f_out.write("\n".join(zip(*col12)[i]))

if __name__ == '__main__':
  main()
