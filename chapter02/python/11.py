#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def main():
  with codecs.open("hightemp.txt", "r", "utf8") as f:
    replaced_text = f.read().strip().replace("\t", " ")
  print replaced_text

if __name__ == '__main__':
  main()
