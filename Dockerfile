FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY shrek.avi /app

COPY . /app

EXPOSE 8000

ENV FLASK_APP=app.py

CMD ["gunicorn", "-b", ":8000", "app:app"]
