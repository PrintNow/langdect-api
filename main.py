#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

import tornado.ioloop

from LangDetectHandler import LangDetectHandler

app = tornado.web.Application([
    (r"/", LangDetectHandler),
])

if __name__ == "__main__":
    num_processes = int(os.getenv('NUM_PROCESSES', '4'))
    port = int(os.getenv('LISTEN_PORT', '8899'))

    print(f"num_processes: {num_processes}")
    print(f"listen_port: {port}")

    app.num_processes = num_processes
    app.listen(port)

    tornado.ioloop.IOLoop.current().start()
