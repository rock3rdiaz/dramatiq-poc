import os
import dramatiq
from dotenv import load_dotenv


from dramatiq.brokers.redis import RedisBroker
from redis import Redis


load_dotenv()


redis_client = Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0)

redis_broker = RedisBroker(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0)
dramatiq.set_broker(redis_broker)
