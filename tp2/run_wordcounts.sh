#!/bin/bash

echo "Started running all WordCount methods"

source ./wordcount_linux.sh
source ./wordcount_hadoop.sh
source ./wordcount_spark_hdfs.sh
source ./wordcount_spark_s3.sh

echo "Finished running all WordCount methods"
