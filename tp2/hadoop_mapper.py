#!/usr/bin/env python3 

# Code inspired by https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/ 
# and https://levelup.gitconnected.com/map-reduce-with-python-hadoop-on-aws-emr-341bdd07b804

import sys 
import string
try: 
    for line in sys.stdin: 
        # Remove trailing whitespace and split each word in a list
        line = line.strip() 
        words = line.split(' ') 
        for w in words: 
            # Only print actual words
            if w: 
                print(w, '\t', 1)
except:
    pass
