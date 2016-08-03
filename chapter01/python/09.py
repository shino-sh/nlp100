#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

def shuffle(word):
  if len(word) > 4: 
    return word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
  else:
    return word

def main():
  sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
  words = sentence.split(" ")
  shuffled_sentence = " ".join([shuffle(word) for word in words])
  print "row sentence      : {}".format(sentence)
  print "shuffled sentence : {}".format(shuffled_sentence)

if __name__ == '__main__':
  main()
