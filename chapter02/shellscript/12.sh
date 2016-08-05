#!/usr/bin/bash

echo_and_do () {
  echo "> $1"
  eval "$1"
}

echo_and_do "cut -f 1 hightemp.txt > col1.txt"
echo_and_do "cut -f 2 hightemp.txt > col2.txt"
echo_and_do "cat col1.txt"
echo_and_do "cat col2.txt"
