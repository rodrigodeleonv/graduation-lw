FROM python:3.10-slim-bullseye
WORKDIR /app_root

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements/production.txt ./requirements.txt
RUN apt-get update \
    && pip install -U pip \
    && pip install -r requirements.txt --no-cache-dir

COPY ./app ./
COPY ./entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "proj.wsgi", "--bind", "0.0.0.0:8000"]
