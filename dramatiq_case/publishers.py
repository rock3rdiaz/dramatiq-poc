import dramatiq
import httpx
import json
from dramatiq_case.receivers import processor, validation, validation_error_callback
from . import redis_broker, redis_client


@dramatiq.actor
def main_publisher():
    print('---------------- running main_publisher actor')
    message = 'Hello world!'
    redis_client.publish('assistants_channel', message)


@dramatiq.actor(queue_name='data_messages')
def analyzer(order_id):
    print('---------------- running order actor')
    info = {
        'order_id': order_id
    }
    with httpx.Client() as client:
        response = client.get('https://pokeapi.co/api/v2/pokemon/ditto')
        info['details'] = response.json()
    print(f'--------- analyzer response: {info}')
    #processor.send_with_options(args=(info,), delay=10000)
    validation.send_with_options(args=(), on_failure=validation_error_callback)
