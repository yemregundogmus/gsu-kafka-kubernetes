# Python tabanlı bir imaj kullan
FROM python:3.9-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gerekli Python kütüphanelerini yükle
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Betikleri çalışma dizinine kopyala
COPY . .

# Varsayılan çalışma komutu
CMD ["python", "producer.py"]
