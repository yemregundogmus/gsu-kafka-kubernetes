import pika
import time

def consume():
    # RabbitMQ bağlantısı
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Kuyruk oluşturma
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f'Consumed: {body.decode()}')
        # Tüketim hızı
        time.sleep(3)

    # Mesajı tüketiciye bağla
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    consume()
