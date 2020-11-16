#!/bin/bash

# Remove hdfs output directory
hdfs dfs -rm -r output

# Remove all results from results directory
rm results/*