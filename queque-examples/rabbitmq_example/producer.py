import pika
import time

def produce():
    # RabbitMQ bağlantısı
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Kuyruk oluşturma
    channel.queue_declare(queue='hello')

    while True:
        # Üretilen mesaj
        message = f'Hello World! {time.time()}'
        # Mesajı kuyruğa gönder
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        print(f'Produced: {message}')
        # Üretim hızı
        time.sleep(2)

    connection.close()

if __name__ == '__main__':
    produce()
