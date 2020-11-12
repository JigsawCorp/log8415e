#!/bin/bash

sudo yum -y install git
git clone https://github.com/JigsawCorp/log8415e.git

hdfs dfs -mkdir input

# Fetch input datasets 
mkdir input_datasets
wget -P input_datasets "http://goo.gl/9GqADe"
wget -P input_datasets "http://www.gutenberg.org/files/219/219-0.txt"
wget -P input_datasets "https://tinyurl.com/y2somksc"
wget -P input_datasets "http://www.gutenberg.org/cache/epub/39850/pg39850.txt"
wget -P input_datasets "http://www.gutenberg.org/cache/epub/8578/pg8578.txt"

# Copy datasets to hdfs
hdfs dfs -copyFromLocal input_datasets/9GqADe input
hdfs dfs -copyFromLocal input_datasets/219-0.txt input
hdfs dfs -copyFromLocal input_datasets/y2somksc input
hdfs dfs -copyFromLocal input_datasets/pg39850.txt input
hdfs dfs -copyFromLocal input_datasets/pg8578.txt input

# Results 
mkdir results

# Linux execution
echo "Executing Linux command"
echo "9GqADe:" >> results/linux_time.txt
(time cat input_datasets/9GqADe | tr ' ' '
' | sort | uniq -c > results/linux_9GqADe.txt) &>> results/linux_time.txt 
echo "219-0.txt:" >> results/linux_time.txt
(time cat input_datasets/219-0.txt | tr ' ' '
' | sort | uniq -c > results/linux_219-0.txt) &>> results/linux_time.txt 
echo "y2somksc:" >> results/linux_time.txt
(time cat input_datasets/y2somksc | tr ' ' '
' | sort | uniq -c > results/linux_y2somksc.txt) &>> results/linux_time.txt 
echo "pg39850.txt:" >> results/linux_time.txt
(time cat input_datasets/pg39850.txt | tr ' ' '
' | sort | uniq -c > results/linux_pg39850.txt) &>> results/linux_time.txt 
echo "pg8578.txt:" >> results/linux_time.txt
(time cat input_datasets/pg8578.txt | tr ' ' '
' | sort | uniq -c > results/linux_pg8578.txt) &>> results/linux_time.txt 

# Hadoop execution
echo "Executing Hadoop"
echo "9GqADe:" >> results/hadoop_time.txt
(time hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files log8415e/tp2/mapper.py,log8415e/tp2/reducer.py -mapper mapper.py -reducer reducer.py -input input/9GqADe -output output/9GqADe >> results/hadoop_9GqADe.txt) &>> results/hadoop_time.txt
echo "219-0:" >> results/hadoop_time.txt
(time hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files log8415e/tp2/mapper.py,log8415e/tp2/reducer.py -mapper mapper.py -reducer reducer.py -input input/219-0.txt -output output/219-0 >> results/hadoop_219-0.txt) &>> results/hadoop_time.txt
echo "y2somksc:" >> results/hadoop_time.txt
(time hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files log8415e/tp2/mapper.py,log8415e/tp2/reducer.py -mapper mapper.py -reducer reducer.py -input input/y2somksc -output output/y2somksc >> results/hadoop_y2somksc.txt) &>> results/hadoop_time.txt
echo "pg39850.txt:" >> results/hadoop_time.txt
(time hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files log8415e/tp2/mapper.py,log8415e/tp2/reducer.py -mapper mapper.py -reducer reducer.py -input input/pg39850.txt -output output/pg39850 >> results/hadoop_pg39850.txt) &>> results/hadoop_time.txt
echo "pg8578.txt:" >> results/hadoop_time.txt
(time hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files log8415e/tp2/mapper.py,log8415e/tp2/reducer.py -mapper mapper.py -reducer reducer.py -input input/pg8578.txt -output output/pg8578 >> results/hadoop_pg8578.txt) &>> results/hadoop_time.txt

