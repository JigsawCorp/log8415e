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
session = boto3.Session(aws_access_key_id='ASIAXEEIBJ3CX7R5RJ5D',
                   aws_secret_access_key='H+RfbhSkE5bgXxPidb9JBtqOHrAY6ZWPqV+5aXjO',
                   aws_session_token='FwoGZXIvYXdzEKf//////////wEaDCZkRf+8i/WLGOgaESLRAT3Ijm/DRWbqzeoElCmMoG1kTrRvwDsnjvPtJr7+toKhtlX0wtAXsx+8jr4uZxWTWbZcpTDTs3JhcDvKdHnmDNOKSFuMISzjg+UrrOekDlpkpV7tqWhfiEfKvsg508YQk72s9H+cYqWNwXvgE+oAWjJJoJo/cu65THo8rH4VaSshaFdMwtIPLH83MP47MmXq7Roc8PvzZ/fol6TGsfwMAGKiA9zIbOrmSC3QYNbWKOYAQljV/sorncCmOr9VkGSZwqpkrRQsp74bGu7E3MVKsYzjKJvKgP4FMi3h0OAGiTFS6u+T1pAC/Cq8Z6xQDq0b8MxON71tV38KurU4EprZCs3H/rvRvQc=',
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
