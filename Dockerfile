FROM python:3.12
ENV PYTHONUNBUFFERED 1

RUN mkdir /shortener
COPY . /shortener/
WORKDIR /shortener

COPY start /usr/local/bin
RUN chmod +x /usr/local/bin/start

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["start"]
