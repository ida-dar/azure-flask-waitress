FROM python:3-alpine

WORKDIR /usr/src/flask-gunicorn

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","app.py"]
