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
session = boto3.Session(aws_access_key_id='ASIAXEEIBJ3C4Y77QR7H',
                   aws_secret_access_key='regNEMN0Q/7+2aiMmL1RN8HbXAxxDB4/XRu9WIXY',
                   aws_session_token='FwoGZXIvYXdzEIH//////////wEaDPRObcT8oje4GyEwOCLRAQh4IrItsFsw1MtweDpA5QoMB40bFzx0FGMgYkcYa5TEW2p8MhxNiU4BN+EqqKF2IUyFMh9+kh8JTtut7LZ9aUi8Cgg1vdZ+yGE6q2PGYRreW2QbWGrDXM/Jij9rbeL5aARQ1RMIPUZiZRKHuD5dtJo0aEHAdUdjjCtp8arf9QTl31Ch74G6a0q1C9RNOUpCfRc4zkGgdVAa03f9bd1UV2uCBNgqnN+ER8yn7NakbFNUB8uusGQwXb0JWdvqk80mrRfcjClqWPyVy0JDG8FLfeH4KID7v/0FMi3JHee4kEmOy6EkRyLbgX/n0EQMExlMDYv1ngRWagh8Vd05tpZZ/fhJ+/NXLR8=',
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
