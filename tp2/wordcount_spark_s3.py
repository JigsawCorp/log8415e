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
session = boto3.Session(aws_access_key_id='ASIAXEEIBJ3CYJKHM6F3',
                   aws_secret_access_key='Wwag1tBtEwdjRWTeYQr5+nfcvtmmBRcqN1Cy2sqf',
                   aws_session_token='FwoGZXIvYXdzELX//////////wEaDDs+t++OpeVPts3T0iLRAU4S/gszvMCY92Mp+bazAgItc2cO1j3Fo9No+A41kAbj6nIxco5uYyGhyaRhxdcmcNlS6sQBgk28Ff//ZiBZBS6k9eKjsRHnSwmICiEljF+5X2r0YkkSKJX7M3VbbbVSweNozFmbR6E/YYnzAgBudhnd8hngum4fJD27iSssaXmoQ0IZm9DRUudjxuHdFFbmisn0iSyurgSnOeCWBAqzotCARXwqAVwjxyToFAK5kn0jgmLd6iFTkApmfyTky5PnUg8tnVt6iYYVdjm2ZgEB3cisKN+dy/0FMi31dQAdhD0i+F4vjHifi3bkeL+ManE8MO0hNbYHGFLI6bSq7QJbPnHmvpt3HU8=',
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
