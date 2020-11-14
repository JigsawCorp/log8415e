#!/bin/bash

# Spark HDFS execution
echo "Executing Spark HDFS WordCount"
for i in {1..5}
do
	echo "Executing WordCount for data$i:" >> results/spark_hdfs_time.txt
	for j in {1..5}
	do
		echo "data$i - Execution $j:" >> results/spark_hdfs_time.txt
		(time spark-submit --master yarn log8415e/tp2/wordcount_spark_hdfs.py data1.txt spark/hdfs/data${i}_exec${j} &>> results/spark_hdfs_data${i}_exec${j}.txt) &>> results/spark_hdfs_time.txt
		echo "" >> results/spark_hdfs_time.txt
	done	
done

