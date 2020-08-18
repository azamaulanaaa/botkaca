FROM python:3-alpine
WORKDIR /app
RUN apk update && apk add -u -q \
    aria2 \
    ffmpeg \
    build-base
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "bot"]
