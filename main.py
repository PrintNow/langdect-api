from typing import Optional, Awaitable

import tornado.ioloop
import tornado.web

import json
import tornado.web

from langdetect import detect
from langdetect import DetectorFactory


class LangDetectHandle(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def post(self):
        raw_body = self.request.body.decode('utf-8')
        try:
            json_body = json.loads(raw_body)
        except BaseException:
            json_body = {}

        DetectorFactory.seed = 0

        result_list = []
        for i, text in enumerate(json_body):
            # 处理识别结果
            result_list.append({
                'text': text,
                'language': detect(text)
            })

        if json_body and result_list:
            resp = {'code': 200, 'msg': 'ok', 'data': result_list}
        else:
            self.set_status(400)
            resp = {'code': 201, 'msg': '待识别的文本内容���空或不正确，请检查', 'source': raw_body}

        self.write(resp)


def make_app():
    return tornado.web.Application([
        (r"/", LangDetectHandle),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8899)
    tornado.ioloop.IOLoop.current().start()
