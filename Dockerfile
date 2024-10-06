FROM python:3

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

RUN pip install --upgrade pip

RUN apt update

WORKDIR bot

COPY . .

RUN pip install -r requirements.txt

CMD python __main__.py