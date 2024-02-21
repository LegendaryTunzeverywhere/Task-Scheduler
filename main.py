from scheduler import TaskScheduler
from example import example_task

if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Add a task to run the example task every 5 seconds
    scheduler.add_task(5, example_task)

    # Run the task scheduler
    scheduler.run()
