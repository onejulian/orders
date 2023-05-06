FROM python:3.10-alpine as builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install virtualenv
RUN virtualenv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd
RUN pip install -r requirements.txt
FROM python:3.10-alpine
COPY --from=builder /opt/venv /opt/venv
WORKDIR /app
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
RUN apk add netcat-openbsd
ENV PATH="/opt/venv/bin:$PATH"
COPY . .
CMD python manage.py runserver 0.0.0.0:80