FROM python:3.10.3-alpine

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Create a group and user to run the app
ARG APP_USER=appuser
RUN addgroup ${APP_USER} && adduser -D -G ${APP_USER} ${APP_USER}

RUN mkdir /home/appuser/app
WORKDIR /home/appuser/app

RUN apk update \
    && apk add nano postgresql-dev python3-dev musl-dev gcc libffi-dev rust cargo openssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /home/appuser/app

RUN pip install --upgrade pip \
    && pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev \
    && rm -rf /var/lib/apt/lists/*

ADD . /home/appuser/app/

EXPOSE 8000

# Change to a non-root user
USER ${APP_USER}

CMD ["gunicorn", "--bind", ":8000", "configure.wsgi:application"]
