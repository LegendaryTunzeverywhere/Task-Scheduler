import schedule
import time

class TaskScheduler:
    def __init__(self):
        self.jobs = []

    def add_task(self, interval, job_func, *args, **kwargs):
        job = schedule.every(interval).seconds
        job.do(job_func, *args, **kwargs)
        self.jobs.append(job)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
