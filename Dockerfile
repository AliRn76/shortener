FROM python:3.10
ENV PYTHONUNBUFFERED 1

RUN mkdir /shortener
COPY . /shortener/
WORKDIR /shortener

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["gunicorn", "-w", "4", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--log-level", "DEBUG"]
