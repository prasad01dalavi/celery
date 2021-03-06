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

pip install sqlalchemy
```

## Celery Commands:
```bash
# For a complete listing of the command-line options available
celery worker --help

# There are also several other commands available, and help is also available
celery help

# Start the celey app
celery -A tasks worker --loglevel=info
```

## Python Shell:
```bash
>> from tasks import add
>> result = add.delay(5, 5)
>> result.status
'PENDING'
>> result.status    # After 10 seconds
'SUCCESS'    
>> result = add.delay(5, 5)
>> result.ready()
'False'
>> result.ready()   # After 10 sec
'True'
>> result.get()
10
```

