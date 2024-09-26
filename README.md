# Stream_Twitter_Data_With_Kafka
 
This repository demonstrates real-time streaming of Twitter data using Apache Kafka, providing a hands-on approach to building data pipelines.
It includes a Kafka producer to capture live tweets from the Twitter API, streaming them through Kafka topics. 
The consumer listens to these topics, processes the tweets, and stores them in HDFS for further analysis.

Additionally, this project serves as a guide for working with key Python libraries like kafka-python, hdfs and offering practical examples for integrating these tools in real-time data workflows. Perfect for those learning how to handle real-time data pipelines and leverage Python for streaming and storage solutions.

1. First, you'll need to install Kafka and Hadoop on your system (Windows OS in this case).
   You can refer to the following links for detailed installation guides:
   Kafka installation tutorial --> https://www.youtube.com/watch?v=w6A-uDEb7JY&t=120s
   Hadoop installation tutorial --> https://www.youtube.com/watch?v=knAS0w-jiUk&t=943s

2. Set up Your Development Environment

Once the installation is complete, use Visual Studio Code (VSCode) as your Integrated Development Environment (IDE).
Create a new virtual environment to isolate your project dependencies. 

3- Install Required Libraries
   pip install kafka   # kafka-1.3.5
   pip install hdfs    # hdfs-2.7.3
 Note: you should provide proper python version to be compatible with libraries.
 here im using python version 3.11.7

 4- before running the code you should provide kafka and hadoop enviroment to make data transportation.

    This is the command to provide Nodes, brokers using Apachi Hadoop and active kafka and zookeeper servers

    ---------------------------------------- KAFKA ------------------------------------------------
    kafka server setting --> /bin/windows/kafka-server-start.bat  /config/server.properties
    start zookeeper setting --> bin/windows/zookeeper-server-start.bat  /config/zookeeper.properties

    -----------------------------------------HADOOP ------------------------------------------------
    Firtly --> reformat DataNodes --> hdfs namenode -format
    Then --> start all dfs --> start-dfs.cmd  # this should be run in  --> cmd \hadoop\bin\ directory
    Note --> all steps to install and run kafka and hadoop servers provided in youtube links above so no worries :)

    
Here, we are working with a CSV file for demonstration purposes, but you can retrieve live data from Twitter using their API. 
The link below provides code that integrates live Twitter data.
https://docs.google.com/document/d/1dGYF5wpAIb1MZ1EgDY86VGbkmVgPq5H3QU22u0LwpF4/edit#heading=h.lm62od589w44

    
    

    

    
 
 





