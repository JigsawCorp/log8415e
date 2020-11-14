# -*- coding: utf-8 -*-
"""
WordCount with PySpark and S3
"""
import boto3
import sys
import string
from pyspark.sql import SparkSession

# Create spark session   
spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

# Create boto3 session
session = boto3.Session(aws_access_key_id='ASIAXEEIBJ3CZ4AQNGPP',
                   aws_secret_access_key='7B8vxDTVYQHuOr1Ag3mR3bmXg0NwJ4PVVAvKhW9W',
                   aws_session_token='FwoGZXIvYXdzEIX//////////wEaDM/Y8VkjOblacR3/yCLRAY2duH1+EdmUqzT3KZU2WA1CXFy8EVgETgZ3IoTtY+ctZGDzlyG0t9RmFKDrWpVJplu1miEKmAsWMhYnD96cYB0M8YJcBCPDZXpVkNgclCpTE90XgisQayh8xEdv41wvYU3HNtTjf/jm54ez8WdQxymaKAOHa6JyY8cQpFINXiGSRhy5KcTxnM6+2EysHX45S5y0ANPtp6YuScAM22bbE5mYD05t613OCtUb0JbVCoYDr2vctkI8hxJTvK/eQTMV18iBoC66XtmKmYcQ6ZZmhVi2KPPqwP0FMi3m36ZYmsofD88oSuY6aAhaG7Fn3u63i1/5SOpc+0+PSf5Qd3i7t3QMuqIsMIQ=',
                   region_name='us-east-1')
                    
s3 = session.resource('s3')

# Get bucket
bucket = s3.Bucket('log8415efirstbucket') 

# Get file
fileobj = bucket.Object(key=sys.argv[1])

# Read content of the file and decode
filedata = fileobj.get()["Body"].read()
content = filedata.decode('latin-1')

# Remove punctuation from string
cleaned = content.translate(str.maketrans('', '', string.punctuation))

# Remove leading spaces, lowercase, and split into list
words_list = cleaned.strip().lower().split()

# Transform into rdd and perform word count
wordcount = spark.sparkContext.parallelize(words_list)\
            	.map(lambda x:(x,1)) \
                .reduceByKey(lambda x,y: x+y)

# Collect and print results into file
out_path = "s3://log8415efirstbucket/"
wordcount.saveAsTextFile(out_path+sys.argv[2])

# End spark session
spark.stop() 
