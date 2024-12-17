from kafka import KafkaConsumer
import time

def consume():
    consumer = KafkaConsumer(
        'mytopic',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest', 
        """
            - earliest: Tüketicinin geçmiş tüm mesajları işlemesi gerektiğinde. Örneğin, bir veri işleme uygulaması geçmiş tüm verileri analiz etmek istiyorsa bu ayar uygundur.
            - latest: Tüketicinin yalnızca yeni mesajlarla ilgilendiği durumlarda. Örneğin, gerçek zamanlı bir işlem sisteminde, sadece yeni gelen verileri işlemek istediğinizde bu ayarı kullanabilirsiniz.
            - none: Kesinlikle belirli bir offset'le devam edilmesi gereken ve bu offset bulunamazsa uygulamanın hata vermesi gerektiği durumlarda kullanılır.
        """
        group_id='my-group'
    )

    for message in consumer:
        print(f'Consumed: {message.value.decode("utf-8")}')
        # Tüketim hızı
        time.sleep(3)

if __name__ == '__main__':
    consume()
