FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install pipenv && \
    pipenv install --deploy --system

EXPOSE 5005

HEALTHCHECK CMD curl --fail http://localhost:5005/ || exit 1


ENTRYPOINT ["python", "./src/server.py"]