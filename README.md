# langdetect | 语言检测 API

基于 https://github.com/Mimino666/langdetect 制作，打包成了 Docker 镜像，便于线上使用

## 使用方法

1. 你可以自己构建镜像，本项目已经包含 `Dockerfile`
2. 使用我已经构建好的 Docker 镜像: https://hub.docker.com/r/shine09/langdetect-api


使用方法：
```shell
docker run -d \
    --name langdect-api \
    -p 8899:8899/tcp \
    --restart always \
    shine09/langdetect-api
```

## API

**POST**  `http://127.0.0.1:8899`

**body:**
```json
[
    "你好，世界",
    "Returns the best results.",
    "You can specify the number of records to return. For example the following code will return the top three entries.",
    "Returns the result as an array."
]
```

**result:**
```json
{
    "code": 200,
    "msg": "ok",
    "data": [
        {
            "text": "你好，世界",
            "language": "zh-cn"
        },
        {
            "text": "Returns the best results.",
            "language": "en"
        },
        {
            "text": "You can specify the number of records to return. For example the following code will return the top three entries.",
            "language": "en"
        },
        {
            "text": "Returns the result as an array.",
            "language": "en"
        }
    ]
}
```

---

**cURL 命令运行:**
 ```shell
    curl --location --request POST 'http://127.0.0.1:8899' \
        --header 'Content-Type: application/json' \
        --data-raw '[
            "你好，世界",
            "Returns the best results.",
            "You can specify the number of records to return. For example the following code will return the top three entries.",
            "Returns the result as an array."
        ]'
 ```


## 缺点

识别会不太准确