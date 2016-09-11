SQL Select, Where 
Main Class: select.select
Data : dataset/sql/sample.csv

SQL Grouping
Main Class: groupBy.groupBy
Data : dataset/sql/sample.csv

SQL Join
Main Class: join.Join
Data : dataset/sql/joinNames.csv ,  dataset/sql/joinTrades.csv

You'll specify two input paths at the command line instead of the usual 1.



Running an MR job: 
Step 0: Add Hadoop JARs before you build a JAR from this source code. 

Step 1: Add the input data to HDFS.  Sample data is provided in the dataset folder. 
$ hadoop fs -copyFromLocal <inputdata> <hdfs location> 

Step2: Run the MR job 
$ hadoop jar <JAR file path> <Main class name> <inputfile or input directory> <output directory>

Step3: To view the output
$ hadoop fs -cat <outputdir> 

