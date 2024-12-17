from kafka import KafkaProducer
import time

def produce():
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    
    while True:
        # Üretilen mesaj
        message = f'Hello World! {time.time()}'
        # Mesajı kuyruğa gönder
        producer.send('mytopic', message.encode('utf-8'))
        print(f'Produced: {message}')
        # Üretim hızı
        time.sleep(2)

if __name__ == '__main__':
    produce()
