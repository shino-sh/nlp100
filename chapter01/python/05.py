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
  char_bigram = [gen_ngram(word, 2) for word in words]
  char_bigram.remove([])
  print word_bigram, char_bigram

if __name__ == '__main__':
  main()
