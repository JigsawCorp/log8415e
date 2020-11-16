#!/bin/bash

# Hadoop execution
echo "Executing Hadoop WordCount"

# For each dataset
for i in {1..5}
do
	echo "Executing WordCount for data$i"
	echo "Executing WordCount for data$i:" >> results/hadoop_time.txt

	# Execute command 5 times
	for j in {1..5}
	do
		echo -n "data$i - Execution $j - "
		echo "data$i - Execution $j:" >> results/hadoop_time.txt
		# Execute WordCount program and calculate execution time
		(time hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files log8415e/tp2/hadoop_mapper.py,log8415e/tp2/hadoop_reducer.py -mapper hadoop_mapper.py -reducer reducer.py -input input/data$i.txt -output output/hadoop/data${i}_exec${j} &>> results/hadoop_data${i}_exec${j}.txt) &> results/hadoop_time_tmp.txt 	
		cat results/hadoop_time_tmp.txt >> results/hadoop_time.txt
		echo "" >> results/hadoop_time.txt
		grep real results/hadoop_time_tmp.txt | sed 's/real[[:blank:]]*//g'
	done	
done

rm results/hadoop_time_tmp.txt 
