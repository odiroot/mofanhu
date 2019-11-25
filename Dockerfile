## BUILD IMAGE ##
FROM python:3.8-alpine AS build

WORKDIR /app

COPY requirements.txt /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


## RUN IMAGE ##
FROM build

COPY . /app

# Run as non-root.
RUN \
  addgroup -S project && \
  adduser -S -H -G project project && \
  chown -R project:project /app
USER project

# No stdout buffering.
ENV PYTHONUNBUFFERED 1
# No pyc file writing.
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi", "--access-logfile", "-"]

