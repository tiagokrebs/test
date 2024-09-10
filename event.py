from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

def publish_message(topic, value):
    try:
        value_bytes = json.dumps(value).encode('utf-8')
        producer.send(topic, value_bytes)  
        producer.flush()
        print("Message published successfully.")
    except Exception as e:
        print(f"Error publishing message: {e}")
