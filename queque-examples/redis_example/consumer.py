import redis
import time

# Redis bağlantısı
r = redis.Redis(host='redis', port=6379, db=0)

def consume():
    while True:
        # Kuyruktan mesaj al ve işleme al
        message = r.blpop('myqueue', timeout=0)
        if message:
            print(f'Consumed: {message[1].decode("utf-8")}')
        # Tüketim hızı
        time.sleep(3)

if __name__ == '__main__':
    consume()
