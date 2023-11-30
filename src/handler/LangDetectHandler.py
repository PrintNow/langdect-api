# -*- coding: UTF-8 -*-

import json
import logging

from langdetect import detect, DetectorFactory
from typing import List, Dict

import tornado.web

DetectorFactory.seed = 0

class LangDetectHandler(tornado.web.RequestHandler):
    async def post(self):
        try:
            text_list = await self.get_text_list()
        except InvalidJSONError as e:
            logging.warning(f"Failed to parse request body: {e}")
            self.set_status(400)
            self.write({
                'code': 400,
                'msg': 'Bad Request: Invalid request body'
            })
            return

        result_list = await self.detect_languages(text_list)

        self.write({
            'code': 200,
            'msg': 'OK',
            'data': result_list
        })

    async def get_text_list(self) -> List[str]:
        raw_body = self.request.body.decode('utf-8')
        try:
            text_list = json.loads(raw_body)
            if not isinstance(text_list, list):
                raise InvalidJSONError('Invalid request body format: not an array')
            for text in text_list:
                if not isinstance(text, str):
                    raise InvalidJSONError('Invalid request body format: not a string array')
        except json.JSONDecodeError as e:
            raise InvalidJSONError(f'Invalid request body JSON format: {str(e)}')

        return text_list

    async def detect_languages(self, text_list: List[str]) -> List[Dict[str, str]]:
        result_list = []
        for i, text in enumerate(text_list):
            try:
                lang = detect(text)
            except Exception as e:
                logging.error(f"Failed to detect language for '{text}': {e}")
                lang = ''

            # 处理识别结果
            result_list.append({
                'text': text,
                'language': lang
            })

        return result_list

class InvalidJSONError(Exception):
    pass
