FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
ENTRYPOINT ["sh", "/entrypoint.sh"]
