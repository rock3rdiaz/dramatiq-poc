import dramatiq
import json
from pathlib import Path
from . import redis_broker, redis_client


@dramatiq.actor
def main_subscriptor():
    print('---------------- running main_subscriptor actor')
    pubsub = redis_client.pubsub()
    pubsub.subscribe(['assistants_channel'])
    for mensaje in pubsub.listen():
        if mensaje["type"] == "message":
            print(f"Mensaje recibido en el canal assistants_channel: {mensaje['data'].decode('utf-8')}")

@dramatiq.actor(queue_name='process_messages')
def processor(info):
    print('---------------- running processor actor')
    path = Path(Path.cwd(), 'test.txt')
    path.write_text(json.dumps(info))
    print('---------------- processor actor complete')


@dramatiq.actor(queue_name='data_messages', max_retries=3)
def validation(info):
    print('---------------- running validation actor')


@dramatiq.actor
def validation_error_callback(message_data, exception_data):
    print(f"Message {message_data} failed:")
