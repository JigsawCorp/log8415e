This is a readme to explain how to run these scripts and what each file does. 

If you are reading this from within the zip that is handed-in with the report, you will need to either pull the git repo or place all these scripts inside the following structure: log8415e/tp2/. If these scripts are not executed in that specific structure, some paths will fail. 

If you are reading this from within the git repository or after setting up the required structure, you can simply execute emr_boostrap.sh follwed by cluster_configuration.sh to setup the cluster. Then, run either run_wordcounts.sh or run_bi_questions.sh to generate results. 

# File and Folder Explanation
  - results/ - This folder holds raw results performed for our report. results/time_averages.xlsx is a summary of all results.
  - emr_boostrap.sh - This script fetches all cluster dependencies and downloads the git repository containing all scripts. 
  - cluster_configuration.sh - This script sets up the cluster to perform the experiments. It fetches datasets and copies them to HDFS.
  - run_wordcounts.sh - This script simply calls all other wordcount_[method].sh scripts. It is used to start all WordCount experiments.
  - wordcount_[method].sh - These fours scripts simply call the commands to start the WordCount program for their respective method. It will call the WordCount program 5 times for each dataset.
  - clean.sh - This script cleans HDFS and results to prepare for another run of the experiments.
  - hadoop_mapper.py - This script contains the code that will be called for all map jobs in Hadoop.
  - hadoop_reducer.py - This script contains the code that will be called for all recude jos in Hadoop.
  - wordcount_spark_hdfs.py - This script contains the code that will excute the MapReduce WordCount program for Spark using HDFS.
  - wordcount_spark_s3.py - This script contains the code that will excute the MapReduce WordCount program for Spark using S3.
  - bi_questions.py - This script will execute all BI questions and generate the answers to all questions.
  - run_bi_questions.sh - This script simply calls bi_questions.py using spark.

