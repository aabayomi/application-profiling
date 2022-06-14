from live_metrics import SageAppMetricsServer
from runtime_metrics import profiler
from thread import thread
import logging
import threading
import time


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    metric_service = profiler('firstprime.py')
    print(metric_service.metric)

    job_list = [metric_service.runTau,metric_service.runSystemProfile]
    job = thread(job_list)
    job.run_job()

    while True:
        time.sleep(1)
        # metric_service.


    # Setup custom Prometheus metric exporter
    # metrics_service = SageAppMetricsServer({'latency': SageAppMetricsServer.METRIC_TIMER,
    #                                         'fps': SageAppMetricsServer.METRIC_RATE,
    #                                         'x': SageAppMetricsServer.METRIC_NUMBER})

    # # This would be the app main function below doing some heavy-lifting neural network inferencing
    # while True:
    #     metrics_service.start_timer('latency')  # Start a timer for the metric "latency"

    #     # This could be setup/preprocessing code that is relevant to the latency metric but maybe not the fps metric
    #     print('This whole code block is being timed for latency...')
    #     time.sleep(1)

    #     # This could be a code block where FPS is relevant (I just put a useless for loop in here for example)
    #     metrics_service.start_timer("fps")
    #     x = 1
    #     for i in range(1, 1000):
    #         x = x * i
    #     metrics_service.push_metric('x', x)
    #     metrics_service.stop_timer("fps")

    #     metrics_service.stop_timer('latency')  # Stop the timer for the latency metric and let the server push the metric onto the stack
