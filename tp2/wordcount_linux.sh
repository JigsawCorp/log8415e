#!/bin/bash

# Linux execution
echo "Executing Linux command WordCount"

# For each dataset
for i in {1..1}
do
	echo "Executing WordCount for data$i"
	echo "Executing WordCount for data$i:" >> results/linux_time.txt

	# Execute command 5 times
	for j in {1..5}
	do
		echo -n "data$i - Execution $j - "
		echo "data$i - Execution $j:" >> results/linux_time.txt
		# Execute WordCount program and calculate execution time
		(time cat input_datasets/data$i.txt | tr ' ' '
		' | sort | uniq -c > results/linux_data${i}_exec${j}.txt) &> results/linux_time_tmp.txt 
		cat results/linux_time_tmp.txt >> results/linux_time.txt
		echo "" >> results/linux_time.txt	
		grep real results/linux_time_tmp.txt | sed 's/real[[:blank:]]*//g'
	done	
done

rm results/linux_time_tmp.txt 
