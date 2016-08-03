#! /usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(text):
  def cipher_char(char):
    return chr(219 - ord(char)) if char.islower() else char

  cipher_text = [ cipher_char(char) for char in text ]
  return "".join(cipher_text) 

def main():
  row_text = "Hogehoge"
  encrypted_text = cipher(row_text)
  decrypted_text = cipher(encrypted_text) 
  print "row text       : {}".format(row_text)
  print "encrypted text : {}".format(encrypted_text)
  print "decrypted text : {}".format(decrypted_text)

if __name__ == '__main__':
  main()
