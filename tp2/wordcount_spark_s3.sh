#!/bin/bash

# Spark S3 execution
echo "Executing Spark S3 WordCount"

# For each dataset
for i in {1..1}
do
	echo "Executing WordCount for data$i"
	echo "Executing WordCount for data$i:" >> results/spark_s3_time.txt

	# Execute command 5 times
	for j in {1..5}
	do
		echo "data$i - Execution $j - "
		echo "data$i - Execution $j:" >> results/spark_s3_time.txt
		# Execute WordCount program and calculate execution time
		(time spark-submit --master yarn log8415e/tp2/wordcount_spark_s3.py data$i.txt results/spark/s3/data${i}_exec${j} &>> results/spark_s3_data${i}_exec${j}.txt) &> results/spark_s3_time_tmp.txt
		cat results/spark_s3_time_tmp.txt >> results/spark_s3_time.txt
		echo "" >> results/spark_s3_time.txt
		grep real results/spark_s3_time_tmp.txt | sed 's/real[[:blank:]]*//g'
	done	
done

rm results/spark_s3_time_tmp.txt 

