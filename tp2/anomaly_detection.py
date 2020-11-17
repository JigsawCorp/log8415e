from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract

spark = SparkSession.builder.getOrCreate()
spark._jsc.hadoopConfiguration().set("fs.s3.access.key", "MY_ACCESS_KEY")
spark._jsc.hadoopConfiguration().set("fs.s3.secret.key", "MY_SECRET_KEY")

data_path = "s3://path/to/data_dump.csv"

df = spark.read.csv(data_path, header=True, sep=',', inferSchema=False)

# Functions using regexp_extract for readability
def extract_date(n):
    return regexp_extract(col('date'), '(\d\d\d\d)-(\d\d)-(\d\d)', n)
def extract_ip(n):
    return regexp_extract(col('ip_address'), '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', n)

# Rows with anomalies for every column:

print("1- Anomalies for member_id:")
# (None)
df.select('*')\
    .filter(~df.member_id.rlike('^\d{6}$'))\
    .show()

print("2- Anomalies for date:")
# Anomaly 1: Invalid format for 'day' ('1' instead of '01')
df.select("*")\
    .filter(~df.date.rlike('^(\d\d\d\d)-(\d\d)-(\d\d)$') |
            (extract_date(3) > 31) | (extract_date(3) < 1) |
            (extract_date(2) < 1) | (extract_date(2) > 12) |
            (extract_date(1) > 2020))\
    .show()

print("3- Anomalies for country:")
# (None)
df.select('*')\
    .filter(~df.country.rlike('^[A-Z][A-Z]$'))\
    .show()

print("4- Anomalies for gender:")
# (None)
df.select('*')\
    .filter(~df.gender.isin(['Female', 'Male']))\
    .show()

print("5- Anomalies for ip_address:")
# Anomaly 2: Value above 255 (777)
df.select('*')\
    .filter((~df.ip_address.rlike('^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')) |
            (extract_ip(1) < 0) | (extract_ip(1) > 255) |
            (extract_ip(2) < 0) | (extract_ip(2) > 255) |
            (extract_ip(3) < 0) | (extract_ip(3) > 255) |
            (extract_ip(4) < 0) | (extract_ip(4) > 255))\
    .show()

print("6- Anomalies for amount:")
# (None)
df.select('*')\
    .filter(~df.amount.rlike('^\$(0|[1-9]\d*)\.(\d{2})$'))\
    .show()

print("7- Anomalies for vip:")
# (None)
df.select('*')\
    .filter(~df.vip.isin(['true', 'false']))\
    .show()

print("8- Anomalies for product_id:")
# (None)
df.select('*')\
    .filter(~df.product_id.rlike('^(\d{3})(\d{3})$'))\
    .show()

print("9 Anomalies for card_type:")
# (None)
df.select('*')\
    .filter(~df.card_type.rlike('^[a-z]+(?:-[a-z]+)*$'))\
    .show()

print("10- Anomalies for serial:")
# Anomaly 3: Serial number too long
df.select('*')\
    .filter(~df.serial.rlike('^\d{3}-\d{2}-\d{4}$'))\
    .show()

print("11- Anomalies for zone:")
# (None)
df.select('*')\
    .filter(~df.zone.rlike('^zone[1-7]$'))\
    .show()