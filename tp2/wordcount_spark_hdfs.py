# -*- coding: utf-8 -*-
"""
Spyder Editor

WordCount with PySpark and HDFS
"""
import sys
import string
from pyspark.sql import SparkSession

# Create spark session   
spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()
        
# Remove punctuation
def clean(x):
    lowercase = x.lower()
    clean_str = lowercase.translate(str.maketrans('', '', string.punctuation))
    return clean_str

# Connecting to HDFS by providing HDFS host IP and webhdfs port (50070 by default)
# Read into RDD
in_path = "hdfs:///user/hadoop/input/" + sys.argv[1]
text_file = spark.sparkContext.textFile(in_path, use_unicode=False).map(lambda x: x.decode("latin-1"))

# Perform wordcount
words_list = text_file.flatMap(lambda x: clean(x).split())
wordcount = words_list.map(lambda x: (x, 1)).reduceByKey(lambda x,y: x+y)

out_path = "hdfs:///user/hadoop/output/" + sys.argv[2]
wordcount.saveAsTextFile(out_path)
