import redis
import json

from config import REDIS_HOST, REDIS_PORT, TASK_QUEUE


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


def add_task(task):
    redis_client.rpush(
        TASK_QUEUE,
        json.dumps(task)
    )


def get_task():

    result = redis_client.blpop(
        TASK_QUEUE,
        timeout=5
    )

    if result is None:
        return None

    queue_name, task_data = result

    return json.loads(task_data)


def get_queue_size():

    return redis_client.llen(TASK_QUEUE)