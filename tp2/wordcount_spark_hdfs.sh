#!/bin/bash

# Spark HDFS execution
echo "Executing Spark HDFS WordCount"

# For each dataset
for i in {1..1}
do
	echo "Executing WordCount for data$i:" >> results/spark_hdfs_time.txt
	echo "Executing WordCount for data$i" 

	# Execute command 5 times
	for j in {1..5}
	do
		echo -n "data$i - Execution $j - "
		echo "data$i - Execution $j:" >> results/spark_hdfs_time.txt
		# Execute WordCount program and calculate execution time
		(time spark-submit --master yarn log8415e/tp2/wordcount_spark_hdfs.py data$i.txt spark/hdfs/data${i}_exec${j} &>> results/spark_hdfs_data${i}_exec${j}.txt) &> results/spark_hdfs_time_tmp.txt
		cat results/spark_hdfs_time_tmp.txt >> results/spark_hdfs_time.txt
		echo "" >> results/spark_hdfs_time.txt
		grep real results/spark_hdfs_time_tmp.txt | sed 's/real[[:blank:]]*//g'
	done	
done

rm results/spark_hdfs_time_tmp.txt 


