# langdetect | 语言检测 API

基于 https://github.com/Mimino666/langdetect 制作，打包成了 Docker 镜像，便于线上使用

## 使用方法

1. 你可以自己构建镜像，本项目已经包含 `Dockerfile`
2. 使用我已经构建好的 Docker 镜像


使用方法：
```shell
docker run -d \
    --name langdect-api \
    -p 8899:8899/tcp \
    --restart always \
    shine09/langdect-api
```
