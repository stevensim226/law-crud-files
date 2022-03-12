FROM python:3.9.10-alpine3.15

WORKDIR /crud_app/

COPY *.py ./
COPY requirements.txt requirements.txt

EXPOSE 8000

RUN pip3 install -r requirements.txt
CMD python3 crud.py