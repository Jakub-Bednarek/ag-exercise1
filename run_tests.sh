#! /bin/bash

for UT in $(find . -name "*tests.py"); do python3 -m unittest -v ./${UT}; done
