# -*- coding: utf-8 -*-
"""
BI Questions

@author: marie
"""
import boto3
from pyspark.sql import SparkSession

# Create spark session   
spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

# Create boto3 session
session = boto3.Session(aws_access_key_id='ASIATXRCESCTGDRZVPNO',
                   aws_secret_access_key='EyqMaEFXErM3b/W+0Igloi+W1f6P1noP1fqM5len',
                   aws_session_token='FwoGZXIvYXdzEFgaDNF4bNoEKUxh3iLlLyLKAQTgewpTjx1254uWO2f+rNmum1jeeKHDnhiihcd5ltTMJ4y/bT7b3moIg7mfV/lwZx43Gfaf13hKTBDC4QFOmjiaxlkCId5Lui+5p/+BdUU7J7YFyuPn/ntRSqfzv/KjnAgbfLbtPTqEIoprJJR9HNW7/w7Wb6kb5wPpB3eE1kjBghCFIOo9QNm0gGg/vyBVwYDfAfunZ3IjgXjyeRqgH01cax6sVz1GDwFbUKZ76my5HO3q0hvf2vyngQQidkRu2zuMv9VEV2NKMNQo9fC2/QUyLUIk0RfQWbltbO0KmASHaR3dQLuzEJgq2b43PDNgTX9E5VRcFEs8S1gsSerfXg==',
                   region_name='us-east-1')
                    
s3 = session.resource('s3')

# Get bucket
bucket = s3.Bucket('tp2-mlb') 

# Get file
fileobj = bucket.Object(key='data_dump.csv')
filedata = fileobj.get()["Body"].read().decode('utf-8')

df = spark.read.csv(filedata, header=True, sep=',', inferSchema=True)
print('data_dump.csv')
df.show(5)

# Q1 How many distinct members are included in the data set? 
num_members = df.select(df.member_id).distinct()
print("Number of distinct members SQL:", num_members.count()) #2500

num_VIP_members = num_members.filter(df.vip == "true").count()
print("Number of VIP members SQL:", num_VIP_members) # 1303

# Q5 How many Canadian female members purchased an item from Zone7
# Assuming Canada is CA
q4 = num_members.filter((df.gender == "Female") & (df.country == "CN")).count()
print("Number of Canadian female members purchased from Zone7 SQL:", q4) #215
