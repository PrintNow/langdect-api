#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

import tornado.ioloop
import tornado.options
import tornado.web
from fasttext.FastText import _FastText

from handler.LangDetectHandler import LangDetectHandler
from handler.TextRecognitionHandler import TextRecognitionHandler


def make_app(model):
    return tornado.web.Application([
        (r"/", LangDetectHandler),
        (r"/v2", TextRecognitionHandler, dict(model=model)),
    ])


def load_fasttext_model():
    # 初始化 FastText 模型

    ### 用这种方式会出现 WARNING
    # fasttext_model = fasttext.load_model('database/lid.176.bin')

    # 先用这种方式解决 —— https://github.com/facebookresearch/fastText/issues/1056#issuecomment-1278058705
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return _FastText(model_path)


if __name__ == "__main__":
    num_processes = int(os.getenv('NUM_PROCESSES', '1'))
    host = os.getenv('LISTEN_HOST', '0.0.0.0')
    port = int(os.getenv('LISTEN_PORT', '8899'))

    # FatstText 模型路径
    model_path = 'database/lid.176.bin'

    try:
        # 启动 Tornado 应用，并将模型传递给 Application 设置
        app = make_app(model=load_fasttext_model())

        # 启用 Tornado 的日志功能
        tornado.options.parse_command_line()

        # 设置进程数量和监听端口号
        app.num_processes = num_processes
        app.listen(port, host)

        print("Listening on: http://{}:{}".format(host, port))
        tornado.ioloop.IOLoop.current().start()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
