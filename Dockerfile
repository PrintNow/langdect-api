FROM python:3.11-alpine

ENV NUM_PROCESSES=4
ENV LISTEN_PORT=8899

# 将工作目录设置为 /app
WORKDIR /app

RUN pip install --upgrade pip \
    && adduser -D langdetect

COPY --chown=langdetect:langdetect main.py main.py
COPY --chown=langdetect:langdetect LangDetectHandler.py LangDetectHandler.py
COPY --chown=langdetect:langdetect requirements.txt requirements.txt

USER langdetect

RUN pip install -r requirements.txt

CMD ["python", "/app/main.py"]

EXPOSE $LISTEN_PORT

# 构建镜像命令：docker build -f . -t shine09/langdetect-api:1.0 .
# langdetect 是镜像名字
# 1.0        是版本号
