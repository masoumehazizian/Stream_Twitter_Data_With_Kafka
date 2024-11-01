.
.
# code inspired and created by Masoumeh #

from kafka import KafkaConsumer
from hdfs import InsecureClient
import six
import sys

# Handle compatibility with Python 3.12+
if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

# To connect to WebHDFS by providing the IP of the HDFS host and the WebHDFS port.
# Connect to HDFS via WebHDFS (using the correct HTTP address)
client = InsecureClient('http://localhost:9870', user='hadoopy')  # Adjust to correct WebHDFS port

# Create a Kafka consumer to consume messages from the 'testTopic'
consumer = KafkaConsumer('testTopic', bootstrap_servers=['localhost:9092'])
hdfs_path = '/TWEETDATA/tweets.txt'

print("Gonna start listening...")

# Listen for messages from Kafka
for message in consumer:
    # Decode the message received from Kafka
    values = message.value.decode('utf-8')
    print(f"Received message: {values}")  # Debugging output to see the message

    # Check if the file exists, if not, create it
    if not client.content(hdfs_path, strict=False):
        print(f"Creating {hdfs_path} in HDFS...")
        client.write(hdfs_path, data='', encoding='utf-8')

    # Write the message to HDFS, appending it to the existing file
    print("the start of client write then we will see ....")
    with client.write(hdfs_path = hdfs_path) as writer:
        writer.write(f"{values}\n")
print("DONEEEEEEEEEEE...")
