#!/usr/bin/env python3

# Code inspired by https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/ 
# and https://levelup.gitconnected.com/map-reduce-with-python-hadoop-on-aws-emr-341bdd07b804

from collections import defaultdict
import sys

word_count = defaultdict(int)
for line in sys.stdin:
    try:
        line = line.strip()
        word, count = line.split()
        count = int(count)
    except:
        continue
    word_count[word] += count
for word, count in word_count.items():
    print(count, word)