#!/bin/bash

echo "Started running all WordCount methods"

source log8415e/tp2/wordcount_linux.sh
source log8415e/tp2/wordcount_hadoop.sh
source log8415e/tp2/wordcount_spark_hdfs.sh
source log8415e/tp2/wordcount_spark_s3.sh

echo "Finished running all WordCount methods"
