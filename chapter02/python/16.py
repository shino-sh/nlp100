#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  print "split file by N lines.",
  print "input N :",
  n = int(raw_input())
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    lines = f.readlines()
  split_lines = [lines[i:i+n] for i in range(0, len(lines), n)]
  for i, n_lines in enumerate(split_lines):
    with codecs.open("out_{}.txt".format(i+1), "w", "utf8") as f_out:
      f_out.write("".join(n_lines).strip())

if __name__ == '__main__':
  main()
