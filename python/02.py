#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
  text1, text2 = u"パトカー", u"タクシー"
  concat_text = u"".join([x + y for (x, y) in zip(text1, text2)])
  print concat_text

if __name__ == '__main__':
  main()
