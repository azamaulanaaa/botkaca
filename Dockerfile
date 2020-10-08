FROM alpine:latest as prepare_env
WORKDIR /app

RUN apk --no-cache -q add \
    python3 python3-dev py3-pip libffi libffi-dev musl-dev gcc
RUN pip3 install -q --ignore-installed distlib pipenv
RUN python3 -m venv /app/venv

ENV PATH="/app/venv/bin:$PATH" VIRTUAL_ENV="/app/venv"

COPY requirements.txt .
RUN pip3 install -q -r requirements.txt


FROM alpine:latest as execute
WORKDIR /app

ENV PATH="/app/venv/bin:$PATH" VIRTUAL_ENV="/app/venv"

RUN apk --no-cache -q add \
    python3 libffi \
    aria2 \
    ffmpeg

COPY --from=prepare_env /app/venv venv
COPY bot bot

CMD ["python3", "-m", "bot"]
