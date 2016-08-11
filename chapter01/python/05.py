#! /usr/bin/env python
# -*- coding: utf-8 -*-

def gen_ngram(sequence, n):
  ngram = []
  for i in range(len(sequence) - n + 1):
    ngram.append(sequence[i:i+n])
  return ngram

def main():
  sentence = "I am an NLPer"
  words = sentence.translate(None, ',.').split(" ")
  word_bigram = gen_ngram(words, 2)
  char_bigram = gen_ngram(sentence, 2)
  print word_bigram
  print char_bigram

if __name__ == '__main__':
  main()
