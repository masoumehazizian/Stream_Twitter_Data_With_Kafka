
#... producer file ...#

import pandas as pd
from kafka import KafkaProducer
import json

# Load the CSV file
df = pd.read_csv('../Datasets/tweets.csv')

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Send the first 100 tweets to the Kafka topic 'testTopic'
for index, row in df.head(100).iterrows():  # Only take the first 100 rows
    tweet_text = row['tweets']  # Assuming 'tweets' is the column with tweet content
    producer.send('testTopic', value=tweet_text)  # Encode to bytes for Kafka

# Ensure all messages are sent before closing the producer
producer.flush()
