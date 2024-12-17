# Queue Examples Project

This project includes example producer and consumer applications using popular message queue systems: **Kafka**, **RabbitMQ**, and **Redis**. Each queue system is explained step-by-step, including its setup and execution.

---

## Project Structure

```plaintext
queque-examples/
|-- kafka_example/           # Example application for Kafka
|   |-- producer.py          # Kafka Producer (Message producer)
|   |-- consumer.py          # Kafka Consumer (Message consumer)
|   |-- docker-compose.yml   # Kafka service configuration
|   |-- Dockerfile           # Docker image for Kafka application
|   |-- requirements.txt     # Required Python libraries
|
|-- rabbitmq_example/        # Example application for RabbitMQ
|   |-- producer.py          # RabbitMQ Producer (Message producer)
|   |-- consumer.py          # RabbitMQ Consumer (Message consumer)
|   |-- docker-compose.yml   # RabbitMQ service configuration
|   |-- Dockerfile           # Docker image for RabbitMQ application
|   |-- requirements.txt     # Required Python libraries
|
|-- redis_example/           # Example application for Redis
|   |-- producer.py          # Redis Producer (Message producer)
|   |-- consumer.py          # Redis Consumer (Message consumer)
|   |-- docker-compose.yml   # Redis service configuration
|   |-- Dockerfile           # Docker image for Redis application
|   |-- requirements.txt     # Required Python libraries
|
|-- README.md                # Project description (this file)
```

---

## Technologies Used

1. **Kafka**: Distributed, scalable message queue system.
2. **RabbitMQ**: Lightweight and reliable message queue server.
3. **Redis**: In-memory database used as a simple message queue system.
4. **Docker**: Containerization to run all systems in a local environment.
5. **Python**: Language used for producer and consumer applications.

---

## Setup and Execution

Independent configurations are provided for each queue system. Follow the steps below to run the systems.

### 1. Kafka

#### Running the Service:

```bash
cd kafka_example
docker-compose up --build
```

- **Kafka Broker** and **Zookeeper** are started.
- Producer and Consumer containers will also start.

#### How It Works:
- **Producer**: `producer.py` sends messages to the Kafka queue.
- **Consumer**: `consumer.py` consumes messages from the queue.

---

### 2. RabbitMQ

#### Running the Service:

```bash
cd rabbitmq_example
docker-compose up --build
```

- The RabbitMQ service starts, and the **Management UI** is accessible at `http://localhost:15672`.
  - Username: `guest`
  - Password: `guest`

#### How It Works:
- **Producer**: `producer.py` sends messages to the RabbitMQ queue.
- **Consumer**: `consumer.py` consumes messages from the queue.

---

### 3. Redis

#### Running the Service:

```bash
cd redis_example
docker-compose up --build
```

- The Redis service starts and is accessible through port `6379`.

#### How It Works:
- **Producer**: `producer.py` sends messages to the Redis queue.
- **Consumer**: `consumer.py` consumes messages from the queue.

---

## Dependencies

Required dependencies for each system are listed in the `requirements.txt` file:

| System       | Library        |
|--------------|----------------|
| Kafka        | kafka-python   |
| RabbitMQ     | pika           |
| Redis        | redis          |

Docker containers are configured to automatically install dependencies.

---

## Use Cases

- **Kafka**: Ideal for real-time data streaming.
- **RabbitMQ**: Suitable for reliable messaging and job queue systems.
- **Redis**: Preferred for fast and simple message queues.