#! /usr/bin/env python
# -*- coding: utf-8 -*-

def gen_ngram(sequence, n):
  ngram = []
  for i in range(len(sequence) - n + 1):
    ngram.append(sequence[i:i+n])
  return ngram

def main():
  x_text = "paraparaparadise"
  y_text = "paragraph"
  x_set = set(gen_ngram(x_text, 2))
  y_set = set(gen_ngram(y_text, 2))
  union = x_set.union(y_set)
  intersection = x_set.intersection(y_set)
  difference = x_set.difference(y_set)
  print "char bigram of {:<16} : {}".format(x_text, x_set)
  print "char bigram of {:<16} : {}".format(y_text, y_set)
  print "  union of X Y          : {}".format(union)
  print "  intersection of X Y   : {}".format(intersection)
  print "  difference of X Y     : {}".format(difference)
  print "  'se' is included in X : {}".format("se" in x_set)
  print "  'se' is included in Y : {}".format("se" in y_set)

if __name__ == '__main__':
  main()
