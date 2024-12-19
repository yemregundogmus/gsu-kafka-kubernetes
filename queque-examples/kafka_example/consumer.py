from kafka import KafkaConsumer
import time

def consume():
    consumer = KafkaConsumer(
        'mytopic',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest', 
        group_id='my-group'
    )

    for message in consumer:
        print(f'Consumed: {message.value.decode("utf-8")}')
        # Tüketim hızı
        time.sleep(3)

if __name__ == '__main__':
    consume()
