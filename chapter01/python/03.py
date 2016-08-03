#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
  sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
  word_length_list = map(len, sentence.translate(None, ',.').split(" "))
  print word_length_list

if __name__ == '__main__':
  main()
