FROM python:3

WORKDIR /usr/src/app

COPY main.py .
COPY requirements.txt .
COPY ./weatherproject/ /weatherproject

RUN pip install --no-cache-dir -r requirements.txt

CMD python /weatherproject/manage.py runserver