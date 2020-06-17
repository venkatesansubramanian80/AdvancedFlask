FROM python:3.8

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
COPY app.py /app
COPY users /app/users
COPY models.py /app
COPY login.db /app

RUN pip install -r requirements.txt

CMD python app.py