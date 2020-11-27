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
# WARNING: These account credential must be updated regularly, or else will not connect to S3
session = boto3.Session(aws_access_key_id='ASIAXEEIBJ3C7ERPV3MT',
                   aws_secret_access_key='zfdX/G7MxIX/Ix2EspFM3ByS95uQ/p3W61uVGbpk',
                   aws_session_token='FwoGZXIvYXdzEKr//////////wEaDNyJlh2RqNQGQ4bT5CLRAXYuqDwY/54AEShSSr97rXAiCEYA8f9XwbTjDGwd/YaSXTrNdxkox9Tw6tgA3bWdoo8WLuDl3mclBgWoDoMCMgEXwu64XsY0MOWu4YhgR4MJU0Te+/R55Q4oZNo66j6cTgoiEwNpzDmFiZbZH/lDKQ3+mJSyeCYMJhNC60SA06d4nN+2RptffJ3UINyKUtAE6SMbudQQTEv+paGAfR56XrupZKosuJ/SuMwkm+zzucrkwpI4u58eknFbkbbdQIGMM4MNVR0c21A+ah8a9SaPMlGXKKKKgf4FMi1nmGV+cv0XXRIIlH1SXdiJY6PKKQf3lty5OcZO3mguJmnXy+MYMNqNbazApYA=',
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
