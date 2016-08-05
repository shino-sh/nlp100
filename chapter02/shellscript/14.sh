#!/usr/bin/bash

echo_and_do () {
  echo "> $1"
  eval "$1"
}

echo_and_do "head -n 5 hightemp.txt"
