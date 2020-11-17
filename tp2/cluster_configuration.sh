#!/bin/bash

# Fetch input datasets 
mkdir input_datasets
wget "http://goo.gl/9GqADe" -O input_datasets/data1.txt
wget "http://www.gutenberg.org/files/219/219-0.txt" -O input_datasets/data2.txt
wget "https://tinyurl.com/y2somksc" -O input_datasets/data3.txt
wget "http://www.gutenberg.org/cache/epub/39850/pg39850.txt" -O input_datasets/data4.txt
wget "http://www.gutenberg.org/cache/epub/8578/pg8578.txt" -O input_datasets/data5.txt

# Copy datasets to hdfs
hdfs dfs -mkdir input

hdfs dfs -copyFromLocal input_datasets/data1.txt input
hdfs dfs -copyFromLocal input_datasets/data2.txt input
hdfs dfs -copyFromLocal input_datasets/data3.txt input
hdfs dfs -copyFromLocal input_datasets/data4.txt input
hdfs dfs -copyFromLocal input_datasets/data5.txt input

# Setup results directory
mkdir results