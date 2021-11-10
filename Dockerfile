FROM python:3.7-alpine

# 将工作目录设置为 /app
WORKDIR /app

RUN pip install --upgrade pip && \
    adduser -D langdetect \
USER langdetect

COPY --chown=langdetect:langdetect main.py main.py
COPY --chown=langdetect:langdetect requirements.txt requirements.txt

# 安装 requirements.txt 中指定的任何所需软件包
RUN pip install -r requirements.txt

# 定义环境变量
ENV VERSION 1.0.0

EXPOSE 8899

# 在容器启动时运行 main.py
CMD ["python", "/app/main.py"]

# 构建镜像命令：docker build -f Dockfile -t shine09/langdetect-python:1.0 .
# langdetect 是镜像名字
# 1.0      是版本号
# .        是指当前路径下的 Dockerfile 文件