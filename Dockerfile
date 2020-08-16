FROM python:3
WORKDIR /app
RUN apt-get update && apt-get install -y \
    aria2 \
    ffmpeg
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "-m", "bot"]
