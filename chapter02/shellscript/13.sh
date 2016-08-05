#!/usr/bin/bash

echo_and_do () {
  echo "> $1"
  eval "$1"
}

echo_and_do "paste col1.txt col2.txt > col12.txt"
echo_and_do "cat col12.txt"
