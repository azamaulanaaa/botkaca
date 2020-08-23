FROM python:3-alpine
WORKDIR /app
RUN apk update && apk add -u \
    aria2 \
    ffmpeg \
    build-base
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY bot bot
CMD ["python3", "-m", "bot"]
