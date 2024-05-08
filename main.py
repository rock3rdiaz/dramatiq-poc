import asyncio

from dramatiq_case.publishers import analyzer, main_publisher
from dramatiq_case.receivers import main_subscriptor


async def start():
    try:
        #analyzer.send_with_options(args=(121212,), delay=20000)
        main_publisher.send()
        main_subscriptor.send()
    except Exception as ex:
        print('------------', ex)


if __name__ == '__main__':
    asyncio.run(start())
