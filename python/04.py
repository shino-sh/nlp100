#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
  sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
  indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]
  element_symbol = {}
  for i, word in enumerate(sentence.translate(None, ',.').split(" "), 1):
    if i in indexes:
      element_symbol[i] = word[:1]
    else:
      element_symbol[i] = word[:2]
  print element_symbol

if __name__ == '__main__':
  main()
