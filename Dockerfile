FROM python:3.11-alpine

ENV NUM_PROCESSES=1
ENV LISTEN_PORT=8899

# 将工作目录设置为 /app
WORKDIR /app

USER root

# 下载模型
ADD https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin /app/database/lid.176.bin

ADD . .

RUN apk add alpine-sdk \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

EXPOSE $LISTEN_PORT

# 构建镜像命令：docker build -f . -t shine09/langdetect-api:1.0 .
# langdetect 是镜像名字
# 1.0        是版本号
