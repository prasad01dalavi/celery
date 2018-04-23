# Celery
Manages Asynchronous Tasks. How to use celery in python.

## Installations:
1. We need a Broker. Dowload it from the following link:
http://www.rabbitmq.com/download.html

2. Erlarge is a dependency for RabbitMQ. Download it from the following link:
http://www.erlang.org/downloads

3. Install celery using pip 
```bash
pip install celery==3.1.0
```

## Celery Commands:
```bash
# Start the celey app
celery -A tasks worker --loglevel=info

# 
```

