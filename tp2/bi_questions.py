# -*- coding: utf-8 -*-
"""
Business Intelligence Questions

"""
import boto3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct, desc
import pandas as pd
import io

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
fileobj = bucket.Object(key='data_dump.csv')
filedata = fileobj.get()["Body"].read().decode('utf-8')

# filedata is a string
data = io.StringIO(filedata)

# Convert to pandas
pandas_df=pd.read_csv(data, sep=",")
pandas_df=pandas_df.astype(str)

# COnvert to pyspark
df = spark.createDataFrame(pandas_df)
df.show(5)

# Question 1: How many distinct members are included in the data set? 
num_members = df.select(df.member_id).distinct()
print("Question 1: Number of distinct members:")
print(str(num_members.count()) + "\n") #2500

# Question 2: Date of first purchase
first_purchase = df.select("date").agg({"date":"min"}).first()[0]
print("Question 2: Date of first purchase:")
print(str(first_purchase) + "\n")

# Question 3: Different card types
different_card_types = df.select(df.card_type).dropDuplicates().collect()
print("Question 3: Different card types:")
for card_type in different_card_types:
    print(card_type[0])
print("")

# Question 4: How many VIP members do we have in our data set?
num_VIP_members = num_members.filter(df.vip == "True").count()
print("Question 4: Number of VIP members:")
print(str(num_VIP_members) + "\n") # 1303

# Other way around
num_VIP = df.filter(df.vip == "True").select(df.member_id).distinct().count()
print("Question 4 (Other way around): Number of VIP members:")
print(str(num_VIP) + "\n") # 2486

# Question 5: How many Canadian female members purchased an item from Zone7
q4 = num_members.filter((df.gender == "Female") & (df.country == "CN")).count()
print("Question 5: Number of Canadian female members purchased from Zone7:")
print(str(q4) + "\n") #215

# Other way around
q4_1 = df.filter((df.gender == "Female") & (df.country == "CN")).select(df.member_id).distinct().count()
print("Question 5 (Other way around): Number of Canadian female members purchased from Zone7:")
print(str(q4_1) + "\n") # 1487

# Question 6: Item with max price
max_price_item = df.orderBy(desc("amount")).select("product_id", "amount").first()
print("Question 6: Item with max price:")
print("product_id: " + str(max_price_item[0]) + ", amount: " + str(max_price_item[1]) + "\n")

# Question 7: Top 3 countries where people made purchase
top_countries = df.groupBy(df.country).count().sort(desc("count")).limit(3).collect()
print("Question 7: Top 3 countries where people made purchase:")
for country in top_countries:
    print("country: " + str(country[0]) + ", purchases made: " + str(country[1]))
print("")
