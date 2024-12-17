import redis
import time

# Redis bağlantısı
r = redis.Redis(host='redis', port=6379, db=0)

def produce():
    while True:
        # Üretilen mesaj
        message = f'Message at {time.time()}'
        # Mesajı kuyruğa ekle
        r.rpush('myqueue', message)
        print(f'Produced: {message}')
        # Üretim hızı
        time.sleep(2)

if __name__ == '__main__':
    produce()
