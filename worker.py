import time
import uuid
import subprocess

from task_queue import get_task


WORKER_ID = str(uuid.uuid4())[:8]


def execute_task(task):

    print("\n-----------------------------")
    print(f"Worker ID : {WORKER_ID}")
    print(f"Task ID   : {task['task_id']}")
    print(f"Command   : {task['command']}")
    print("-----------------------------")

    try:

        result = subprocess.run(
            task["command"],
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            print(
                f"Task {task['task_id']} completed successfully"
            )

            print("Output:")
            print(result.stdout)

        else:

            print(
                f"Task {task['task_id']} failed"
            )

            print(result.stderr)

    except Exception as error:

        print(
            f"Error executing task: {error}"
        )


def start_worker():

    print("==============================")
    print("Distributed Worker Started")
    print(f"Worker ID: {WORKER_ID}")
    print("==============================")

    while True:

        task = get_task()

        if task is None:
            continue

        execute_task(task)

        time.sleep(1)


if __name__ == "__main__":
    start_worker()