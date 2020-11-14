#!/bin/bash

# Hadoop execution
echo "Executing Hadoop WordCount"
for i in {1..5}
do
	echo "Executing WordCount for data$i"
	echo "Executing WordCount for data$i:" >> results/hadoop_time.txt
	for j in {1..5}
	do
		echo "data$i - Execution $j"
		echo "data$i - Execution $j:" >> results/hadoop_time.txt
		(time hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files log8415e/tp2/mapper.py,log8415e/tp2/reducer.py -mapper mapper.py -reducer reducer.py -input input/data$i.txt -output output/hadoop/data${i}_exec${j} &>> results/hadoop_data${i}_exec${j}.txt) &>> results/hadoop_time.txt 	
		echo "" >> results/hadoop_time.txt
	done	
done

