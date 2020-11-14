#!/bin/bash

# Linux execution
echo "Executing Linux command"
for i in {1..5}
do
	echo "data$i:" >> results/linux_time.txt
	for j in {1..5}
	do
		echo "Execution $j:" >> results/linux_time.txt
		(time cat input_datasets/data$i.txt | tr ' ' '
		' | sort | uniq -c > results/linux_data$i.txt) &>> results/linux_time.txt 	
	done	
done
