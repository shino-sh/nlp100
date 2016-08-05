#!/usr/bin/bash

echo_and_do () {
  echo "> $1"
  eval "$1"
}

echo_and_do "split -l 10 hightemp.txt out."
echo_and_do "cat out.aa"
echo_and_do "cat out.ab"
echo_and_do "cat out.ac"
