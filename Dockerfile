FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add --no-cache make git build-base gcc abuild binutils \
    python3-dev libffi-dev openssl-dev linux-headers sqlite-dev postgresql-dev \
    # Needed by wait
    postgresql-client \
    && mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . .

RUN mv wait-for-db.sh django-cloudlaunch/ \
    && cd django-cloudlaunch \
    && chmod +x wait-for-db.sh

WORKDIR /code/django-cloudlaunch/

EXPOSE 8000

CMD ["./wait-for-db.sh", "db", "python", "manage.py" ,"runserver" , "0.0.0.0:8000"]


