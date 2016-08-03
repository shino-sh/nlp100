#! /usr/bin/env python
# -*- coding: utf-8 -*-

def templete(x, y, z):
  return "{}時の{}は{}".format(x, y, z)

def main():
  print templete("12", "気温", "22.4")

if __name__ == '__main__':
  main()
