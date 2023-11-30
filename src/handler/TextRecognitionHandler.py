import tornado.web
import json


class TextRecognitionHandler(tornado.web.RequestHandler):
    def initialize(self, model):
        self.model = model

    def post(self):
        # 获取 POST 请求中的 JSON 数据
        try:
            json_data = json.loads(self.request.body.decode('utf-8'))
        except json.JSONDecodeError:
            self.write_error_response("Invalid JSON data")
            return

        # 批量处理 JSON 数据中的文本
        results = self.recognize_texts(json_data)

        # 返回结果，ensure_ascii设置为False以保持原始字符
        response_data = {"code": 200, "msg": "ok", "data": results}
        self.write(json.dumps(response_data, ensure_ascii=False))

    def recognize_texts(self, texts):
        # 使用模型进行批量文本识别
        predictions = self.model.predict(texts)

        # 处理每个文本的识别结果
        results = []

        # 遍历元组中的两个列表
        for i, (labels, probabilities) in enumerate(zip(predictions[0], predictions[1])):
            # 处理每个元素
            for label, probability in zip(labels, probabilities):
                results.append({
                    "text": texts[i],
                    "language": label.replace('__label__', ''),
                    "probability": round(float(probability), 2)
                })

        return results

    def write_error_response(self, message):
        # 返回错误响应
        response_data = {"code": 422, "msg": message}
        self.set_status(422)
        self.write(json.dumps(response_data, ensure_ascii=False))
