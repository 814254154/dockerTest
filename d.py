# coding: utf8
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from locust import User, task,events
import time
import gevent

# class Request(BaseHTTPRequestHandler):
#     def __init__(self, environment):
#         self.environment = environment
#     def do_GET(self):
#         self.send_response(200)
#         print("stop")
#         self.environment.runner.quit()


class Dummy(User):
    @task(20)
    def hello(self):
        pass

# def A(environment):
#     Host = ('127.0.0.1', 9999)
#     HTTPServer(Host, Request(environment)).serve_forever()
#     print("dsdsd")
# @events.test_start.add_listener
# def on_test_start(environment, **kwargs):
#     print("A new test is starting")
#     t = Thread(target=A(environment))
#     t.start()
#     print("B new test is starting")
# def checker(environment):
#     while not environment.runner.state in [STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP]:
#         time.sleep(1)
#         if environment.runner.stats.total.fail_ratio > 0.2:
#
#             print(f"fail ratio was {environment.runner.stats.total.fail_ratio}, quitting")
#             environment.runner.quit()
#             return
#
#
# @events.init.add_listener
# def on_locust_init(environment, **_kwargs):
#     if not isinstance(environment.runner, WorkerRunner):
#         gevent.spawn(checker, environment)